import numpy as np
import tensorflow as tf
import keras
import pickle
import os
import time
import serial as serial
import traceback
import colorSpaceUtil

from sklearn.metrics import precision_score, recall_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from numpy import genfromtxt

#device="/dev/tty.usbmodem2853891"
port = "COM3"  # COM for windows, it changes when we use unix system
ser = serial.Serial(port, 115200, timeout=None)
scalar_rack = StandardScaler()
scalar_container = StandardScaler()

loadConfigurationsFromFiles = False

def build_model(n_classes):
    model = tf.keras.Sequential()
    # Must define the input shape in the first layer of the neural network
    model.add(tf.keras.layers.Dense(10, input_shape=(36,), activation='relu'))
    #model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(1024, activation='relu'))
    #model.add(tf.keras.layers.Dropout(0.3))
    #model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(256, activation='relu'))
    #model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(n_classes, activation='softmax'))
    # Take a look at the model summary
    model.summary()

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    return model


def parse_file(csv_path):
    dt = genfromtxt(csv_path, delimiter=',')
    labels = dt[:, -1]
    # For now, ignore accelerometer.
    dt_all_colors = dt[:, range(4, len(dt[0])-1)]
    return dt_all_colors, labels

def saveConfigurations(model_rack, model_container):

    os.makedirs(os.path.dirname("./configs/"), exist_ok=True)
    '''
    model_json = model_rack.to_json()
    with open("./configs/model_rack.json", "w") as json_file:
        json_file.write(model_json)
    model_rack.save_weights("./configs/model_rack_weights.h5")  # serialize weights to HDF5

    model_json = model_container.to_json()
    with open("./configs/model_container.json", "w") as json_file:
        json_file.write(model_json)
    model_container.save_weights("./configs/model_container_weights.h5")  # serialize weights to HDF5
    '''
    model_rack.save('./configs/model_rack.h5')
    model_container.save('./configs/model_container.h5')
    pickle.dump(scalar_rack, open("./configs/scalar_rack.p", "wb"))
    pickle.dump(scalar_container, open("./configs/scalar_container.p", "wb"))

    print("Saved machine learning models and scalar configuration into files !!")


def get_trainig_data():
    train_rack_data, train_rack_labels_raw = parse_file('./data/rack_red_train_hsv.csv')
    scalar_rack.fit(train_rack_data)
    train_rack_data = scalar_rack.transform(train_rack_data)
    train_rack_labels = keras.utils.to_categorical(train_rack_labels_raw, 2)

    train_container_data, train_container_labels_raw = parse_file('./data/container_train_hsv.csv')
    scalar_container.fit(train_container_data)
    train_container_data = scalar_container.transform(train_container_data)
    train_container_labels = keras.utils.to_categorical(train_container_labels_raw, 5)

    return (train_container_data, train_container_labels, train_container_labels_raw), (train_rack_data, train_rack_labels, train_rack_labels_raw)


def get_testing_data():
    test_rack_data, test_rack_labels_raw = parse_file('./data/rack_red_test_hsv.csv')
    test_rack_data = scalar_rack.transform(test_rack_data)
    test_rack_labels = keras.utils.to_categorical(test_rack_labels_raw, 2)

    test_container_data, test_container_labels_raw = parse_file('./data/container_test_hsv.csv')
    test_container_data = scalar_container.transform(test_container_data)
    test_container_labels = keras.utils.to_categorical(test_container_labels_raw, 5)

    return (test_rack_data, test_rack_labels, test_rack_labels_raw), (test_container_data, test_container_labels, test_container_labels_raw)


(train_container_data, train_container_labels, train_container_labels_raw), (
    train_rack_data, train_rack_labels, train_rack_labels_raw) = get_trainig_data()
(test_rack_data, test_rack_labels, test_rack_labels_raw), (
    test_container_data, test_container_labels, test_container_labels_raw) = get_testing_data()

if loadConfigurationsFromFiles:
    '''
    json_file = open("./configs/model_rack.json", 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model_rack = model_from_json(loaded_model_json)
    model_rack.load_weights("./configs/model_rack_weights.h5")

    json_file = open("./configs/model_container.json", 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model_container = model_from_json(loaded_model_json)
    model_container.load_weights("./configs/model_container_weights.h5")
    '''
    model_rack = keras.models.load_model('./configs/model_rack.h5')
    model_container = keras.models.load_model('./configs/model_container.h5')

    scalar_rack = pickle.load(open("./configs/scalar_rack.p", "rb"))
    scalar_container = pickle.load(open("./configs/scalar_container.p", "rb"))

    print("Loaded configurations from files !! ")

else:
    model_rack = build_model(2)
    model_rack.fit(train_rack_data, train_rack_labels, epochs=20, validation_data=(test_rack_data, test_rack_labels),
               batch_size=500)

    model_container = build_model(5)
    model_container.fit(train_container_data, train_container_labels, epochs=20,
               validation_data=(test_container_data, test_container_labels), batch_size=500)

    saveConfigurations(model_rack, model_container)

labels_test_raw = [int(v) for v in train_rack_labels_raw]

x = train_rack_data[0:1]
x = scalar_rack.transform(x)
start_time = time.time()
p = model_rack.predict(x, batch_size=1).argmax(axis=-1)
print(p)
elapsed_time = time.time() - start_time
print(elapsed_time)

test_predicted_res = model_container.predict(test_container_data, batch_size= 1).argmax(axis=-1)

mtx = confusion_matrix(test_container_labels_raw, test_predicted_res)
mtx = mtx[1:, 1:]   # remove class 0 - do nothing
print(mtx)
print(precision_score(test_container_labels_raw, test_predicted_res, average="weighted"))
print(recall_score(test_container_labels_raw, test_predicted_res, average="weighted"))

isRackPredicted = False
try:
    while True:

        frame_raw = ser.readline().decode('utf-8').rstrip()

        ## frame contains accel+ color data
        dt = frame_raw.split(',')
        if dt.__len__() != 54:
            continue

        frame = np.asarray([])

        for i in np.arange(6, 54, 4):
            frame = np.append(frame, colorSpaceUtil.rgbc2hsv(float(dt[i]), float(dt[i+1]), float(dt[i+2]), float(dt[i+3])))

        frame = frame.reshape(1, 36)

        if not isRackPredicted:
            frame = scalar_rack.transform(frame)
            rack_predicted = model_rack.predict(frame, batch_size=1).argmax(axis=-1)
            if rack_predicted != 0:
                isRackPredicted = True
                continue
        else:
            frame = scalar_container.transform(frame)
            container_prediction = model_container.predict(frame, batch_size=1).argmax(axis=-1)
            if container_prediction != 0:
                print("Rack Number", rack_predicted, "Container Number", container_prediction)
                isRackPredicted = False
                continue
except:
    traceback.print_exc()
    ser.close()



