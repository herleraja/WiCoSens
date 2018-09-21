import os
import pickle
import traceback

import keras
import numpy as np
import serial as serial
import tensorflow as tf
from numpy import genfromtxt
from sklearn.preprocessing import StandardScaler

import colorSpaceUtil

# Configuration related inputs
color_space = 'HSV'  # HSV, Lab, YCbCr,HSVDegree, XYZ, RGB
source_dir_path = "./datarecording_discrete/" + color_space.lower() + "/"
config_save_load_dir_path = "./configs/container_24/" + color_space.lower() + "/"
loadConfigurationsFromFiles = False

scalar_rack = StandardScaler()
scalar_container = StandardScaler()


def build_model(number_class):
    model = tf.keras.Sequential()
    # Must define the input shape in the first layer of the neural network
    model.add(tf.keras.layers.Dense(1024, input_shape=(36,), activation=tf.nn.relu,
                                    kernel_regularizer=keras.regularizers.l2(0.001)))
    model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(1024, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001)))
    model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(612, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001)))
    # model.add(tf.keras.layers.Flatten())
    # model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(256, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001)))
    model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001)))
    # model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(number_class, activation='softmax'))
    # Take a look at the model summary
    model.summary()
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',  # rmsprop, adam
                  metrics=['accuracy'])
    return model


def parse_file(csv_path):
    dt = genfromtxt(csv_path, delimiter=',')
    labels = dt[:, -1]
    # For now, ignore accelerometer.
    dt_all_colors = dt[:, range(4, len(dt[0]) - 1)]
    return dt_all_colors, labels


def get_trainig_data():
    train_rack_data, train_rack_labels_raw = parse_file(source_dir_path + 'rack_train.csv')
    scalar_rack.fit(train_rack_data)
    train_rack_data = scalar_rack.transform(train_rack_data)
    train_rack_labels = keras.utils.to_categorical(train_rack_labels_raw)

    train_container_data, train_container_labels_raw = parse_file(source_dir_path + 'container_train_4I.csv')
    scalar_container.fit(train_container_data)
    train_container_data = scalar_container.transform(train_container_data)
    train_container_labels = keras.utils.to_categorical(train_container_labels_raw)

    return (train_container_data, train_container_labels, train_container_labels_raw), (
        train_rack_data, train_rack_labels, train_rack_labels_raw)


def get_testing_data():
    test_rack_data, test_rack_labels_raw = parse_file(source_dir_path + 'rack_test.csv')
    test_rack_data = scalar_rack.transform(test_rack_data)
    test_rack_labels = keras.utils.to_categorical(test_rack_labels_raw)

    test_container_data, test_container_labels_raw = parse_file(source_dir_path + 'container_test_4I.csv')
    test_container_data = scalar_container.transform(test_container_data)
    test_container_labels = keras.utils.to_categorical(test_container_labels_raw)

    return (test_rack_data, test_rack_labels, test_rack_labels_raw), (
        test_container_data, test_container_labels, test_container_labels_raw)


def save_configurations():
    os.makedirs(os.path.dirname(config_save_load_dir_path), exist_ok=True)

    # model_rack.save(config_save_load_dir_path + 'model_rack.h5')
    model_container.save(config_save_load_dir_path + 'model_container.h5')
    pickle.dump(scalar_rack, open(config_save_load_dir_path + "scalar_rack.p", "wb"))
    pickle.dump(scalar_container, open(config_save_load_dir_path + "scalar_container.p", "wb"))

    print("Saved machine learning models and scalar configuration into files !!")


if __name__ == "__main__":
    (train_container_data, train_container_labels, train_container_labels_raw), (
        train_rack_data, train_rack_labels, train_rack_labels_raw) = get_trainig_data()
    (test_rack_data, test_rack_labels, test_rack_labels_raw), (
        test_container_data, test_container_labels, test_container_labels_raw) = get_testing_data()

    if loadConfigurationsFromFiles:
        model_rack = keras.models.load_model(config_save_load_dir_path + 'model_rack.h5')
        model_container = keras.models.load_model(config_save_load_dir_path + 'model_container.h5')

        scalar_rack = pickle.load(open(config_save_load_dir_path + "scalar_rack.p", "rb"))
        scalar_container = pickle.load(open(config_save_load_dir_path + "scalar_container.p", "rb"))

        print("Loaded configurations from files !! ")

    else:

        model_rack = build_model(2)
        model_rack.fit(train_rack_data, train_rack_labels, epochs=10,
                       validation_data=(test_rack_data, test_rack_labels), batch_size=500)

        model_container = build_model(25)
        history_container = model_container.fit(train_container_data, train_container_labels, epochs=20,
                                                validation_data=(test_container_data, test_container_labels),
                                                batch_size=1000)

        save_configurations()

    # device="/dev/tty.usbmodem2853891"
    port = "COM3"  # COM for windows, it changes when we use unix system
    ser = serial.Serial(port, 115200, timeout=None)

    isRackPredicted = False
    isContainerPredicted = False

    container_predicted = None
    rack_predicted = None

    try:
        while True:

            frame_raw = ser.readline().decode('utf-8').rstrip()

            ## frame contains accel+ color data
            dt = frame_raw.split(',')
            if dt.__len__() != 52:
                continue

            colorSpaceConversionFunction = colorSpaceUtil.switcher.get(color_space)

            frame = np.asarray([])
            for i in np.arange(4, 52, 4):
                frame = np.append(frame, colorSpaceConversionFunction(float(dt[i]), float(dt[i + 1]), float(dt[i + 2]),
                                                                      float(dt[i + 3])))

            frame = frame.reshape(1, 36)

            if not isRackPredicted:
                frame = scalar_rack.transform(frame)
                rack_predicted = model_rack.predict(frame, batch_size=1).argmax(axis=-1)
                if rack_predicted != 0:
                    isRackPredicted = True
                    continue
            elif not isContainerPredicted:
                frame = scalar_container.transform(frame)
                container_predicted = model_container.predict(frame, batch_size=1).argmax(axis=-1)
                if container_predicted != 0:
                    isContainerPredicted = True
                    continue
            elif isContainerPredicted:
                frame = scalar_rack.transform(frame)
                rack_predicted_new = model_rack.predict(frame, batch_size=1).argmax(axis=-1)
                if rack_predicted == rack_predicted_new:
                    isRackPredicted = False
                    isContainerPredicted = False
                    print("Rack Number", rack_predicted, "Container Number", container_predicted)
                    continue
    except:
        traceback.print_exc()
        ser.close()
