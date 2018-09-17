import itertools
import os
import pickle
import traceback

import keras
import matplotlib.pyplot as plt
import numpy as np
import serial as serial
import tensorflow as tf
from numpy import genfromtxt
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix, accuracy_score, \
    classification_report
from sklearn.preprocessing import StandardScaler

from sklearn import datasets,neighbors,svm, tree
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression

import colorSpaceUtil

import time

# Configuration related inputs
color_space = 'XYZ'  # HSV, Lab, YCbCr,HSVDegree, XYZ, RGB
source_dir_path = "./datarecording_discrete/" + color_space.lower() + "/"
config_save_load_dir_path = "./configs/container_24/" + color_space.lower() + "/"
loadConfigurationsFromFiles = False

scalar_rack = StandardScaler()
scalar_container = StandardScaler()


def build_model(number_class):
    model = tf.keras.Sequential()
    # Must define the input shape in the first layer of the neural network
    model.add(tf.keras.layers.Dense(1024, input_shape=(36,), activation=tf.nn.relu))
    #model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(1024, activation=tf.nn.relu))
    #model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(612, activation=tf.nn.relu))
    # model.add(tf.keras.layers.Flatten())
    #model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(256, activation=tf.nn.relu))
    #model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    #model.add(tf.keras.layers.Dropout(0.3))
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


def save_configurations():
    os.makedirs(os.path.dirname(config_save_load_dir_path), exist_ok=True)

    #model_rack.save(config_save_load_dir_path + 'model_rack.h5')
    model_container.save(config_save_load_dir_path + 'model_container.h5')
    pickle.dump(scalar_rack, open(config_save_load_dir_path + "scalar_rack.p", "wb"))
    pickle.dump(scalar_container, open(config_save_load_dir_path + "scalar_container.p", "wb"))

    print("Saved machine learning models and scalar configuration into files !!")


def get_trainig_data():
    train_rack_data, train_rack_labels_raw = parse_file(source_dir_path + 'rack_train.csv')
    scalar_rack.fit(train_rack_data)
    train_rack_data = scalar_rack.transform(train_rack_data)
    train_rack_labels = keras.utils.to_categorical(train_rack_labels_raw)

    train_container_data, train_container_labels_raw = parse_file(source_dir_path + 'container_train.csv')
    scalar_container.fit(train_container_data)
    train_container_data = scalar_container.transform(train_container_data)
    train_container_labels = keras.utils.to_categorical(train_container_labels_raw)

    return (train_container_data, train_container_labels, train_container_labels_raw), (
        train_rack_data, train_rack_labels, train_rack_labels_raw)


def get_testing_data():
    test_rack_data, test_rack_labels_raw = parse_file(source_dir_path + 'rack_test.csv')
    test_rack_data = scalar_rack.transform(test_rack_data)
    test_rack_labels = keras.utils.to_categorical(test_rack_labels_raw)

    test_container_data, test_container_labels_raw = parse_file(source_dir_path + 'container_test.csv')
    test_container_data = scalar_container.transform(test_container_data)
    test_container_labels = keras.utils.to_categorical(test_container_labels_raw)

    return (test_rack_data, test_rack_labels, test_rack_labels_raw), (
        test_container_data, test_container_labels, test_container_labels_raw)


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.OrRd):  # Blues,OrRd, YlOrRd
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100.0
        for x in range(0, len(cm[0, :])):
            xv = cm[x, :]
            for y in range(0, len(xv)):
                vv = xv[y]

                cm[x, y] = int(np.round(vv * 10.0)) / 10.0

        #print("Normalized confusion matrix")
    #else:
        #print('Confusion matrix, without normalization')

    # print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def display_result(actual, predicted, type):
    mtx = confusion_matrix(actual, predicted)
    mtx = mtx[1:, 1:]  # remove class 0 - do nothing
    #print('Confusion matrix\n{}\n'.format(mtx))
    print('Precision : ', precision_score(actual, predicted, average="weighted"))
    print('Recall : ', recall_score(actual, predicted, average="weighted"))
    print('F1 Score : ', f1_score(actual, predicted, average="weighted"))
    print('Accuracy : {}'.format(accuracy_score(actual, predicted)))
    print('Classification Report :\n{}'.format(classification_report(actual, predicted, digits=5)))

    plt.figure(figsize=(12, 12))
    plot_confusion_matrix(mtx, classes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], normalize=False, title='Box Identification (non normalized)')
    #plt.show()
    plt.savefig(config_save_load_dir_path + type + '_confusion_matrix.png')
    plt.clf()


def plot_history(history, type):
    # summarize history for accuracy
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.savefig(config_save_load_dir_path + type + '_accuracy.png')
    plt.clf()

    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.savefig(config_save_load_dir_path + type + '_loss.png')
    plt.clf()

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

        #model_rack = build_model(2)
        #model_rack.fit(train_rack_data, train_rack_labels, epochs=10, validation_data=(test_rack_data, test_rack_labels),  batch_size=500)

        model_container = build_model(25)

        start_time = time.time()
        history_container = model_container.fit(train_container_data, train_container_labels, epochs=5, validation_data=(test_container_data, test_container_labels), batch_size=1000)
        elapsed_time = time.time() - start_time
        print('Deep Learning Training time: {}'.format(elapsed_time))
        #save_configurations()

    test_predicted_container_res = model_container.predict(test_container_data, batch_size=1).argmax(axis=-1)

    #test_predicted_rack_res = model_rack.predict(test_rack_data, batch_size=1).argmax(axis=-1)

    print('Color Space: {}'.format(color_space))
    #print('\n****************Classification result for rack************************')
    #display_result(test_rack_labels_raw, test_predicted_rack_res, 'rack')  #Print the classification result

    print('\n****************Classification result for container************************')
    display_result(test_container_labels_raw, test_predicted_container_res, 'container')  #Print the classification result
    plot_history(history_container, 'container')

    # we create an instance of Neighbours Classifier and fit the data.
    # clf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance', n_jobs=-1) #Accuracy = 83.33%
    # clf = svm.SVC(kernel='linear') #Accuracy = 86.66%
    # clf = svm.LinearSVC() #Accuracy = 76.66%
    # clf = LogisticRegression(n_jobs=-1, random_state=0) #Accuracy = 73.33%
    # clf = tree.DecisionTreeClassifier() #Accuracy = 76.66%
    # clf = MLPClassifier() #Accuracy = 76.66%
    clf = RandomForestClassifier(n_jobs=-1)  # Accuracy = 86.66%

    clf.fit(train_container_data, train_container_labels_raw)
    start_time = time.time()
    test_predicted_container_res = clf.predict(test_container_data)
    elapsed_time = time.time() - start_time
    print('\n****************RandomForestClassifier Classification result for container************************')
    print('RandomForestClassifier Training time: {}'.format(elapsed_time))
    display_result(test_container_labels_raw, test_predicted_container_res, 'RandomForestClassifier_container')


    '''
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
    
    
    #Fine tuning the parameters
    kerasClassifier = KerasClassifier(build_fn=build_model)
    param = {'epochs': [10, 20],
             'batch_size': [500, 200],
             'optimizer': ['adam', 'rmsprop'],
             }
    
    grid_search = GridSearchCV(estimator=kerasClassifier, param_grid=param, scoring='accuracy', cv=10)
    grid_search.fit(train_container_data, train_container_labels_raw)
    print(grid_search.best_params_)
    
    
    '''
