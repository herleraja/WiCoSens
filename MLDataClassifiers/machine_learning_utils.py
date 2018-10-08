import itertools
import os
import pickle

import keras
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
from sklearn import decomposition
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix, accuracy_score, \
    classification_report
from sklearn.preprocessing import StandardScaler

# Configuration related inputs
color_space = 'YCbCr'  # HSV, Lab, YCbCr,HSVDegree, XYZ, RGB
source_dir_path = "./datarecording_discrete/" + color_space.lower() + "/"
config_save_load_dir_path = "./configs/container_24/" + color_space.lower() + "/"
feature_type = 'RAW'  # RAW, PREPROCESSED, PCA, LDA, LCA
sensor_fusion = False  # True, False
loadConfigurationsFromFiles = False  # True, False

scalar_rack = StandardScaler()
scalar_container = StandardScaler()

pca = decomposition.PCA(n_components=10)
lda = LinearDiscriminantAnalysis(n_components=10)
ica = decomposition.FastICA(n_components=10)


def parse_file(csv_path, sensor_fusion=False):
    dt = genfromtxt(csv_path, delimiter=',')
    labels = dt[:, -1]

    if sensor_fusion:
        # All sensor data, accelerometer and color sensor.
        data = dt[:, range(1, len(dt[0]) - 1)]
    else:
        # Ignore accelerometer.
        data = dt[:, range(4, len(dt[0]) - 1)]

    return data, labels


def get_trainig_data(sensor_fusion=False, feature_type='PREPROCESSED'):
    train_rack_data, train_rack_labels_raw = parse_file(source_dir_path + 'rack_train.csv', sensor_fusion)
    train_container_data, train_container_labels_raw = parse_file(source_dir_path + 'container_train_2I_4I.csv',
                                                                  sensor_fusion)

    train_rack_labels = keras.utils.to_categorical(train_rack_labels_raw)
    train_container_labels = keras.utils.to_categorical(train_container_labels_raw)

    if feature_type == 'PREPROCESSED':
        scalar_rack.fit(train_rack_data)
        train_rack_data = scalar_rack.transform(train_rack_data)
        scalar_container.fit(train_container_data)
        train_container_data = scalar_container.transform(train_container_data)
        os.makedirs(os.path.dirname(config_save_load_dir_path), exist_ok=True)
        pickle.dump(scalar_rack, open(config_save_load_dir_path + "scalar_rack.p", "wb"))
        pickle.dump(scalar_container, open(config_save_load_dir_path + "scalar_container.p", "wb"))
    elif feature_type == 'PCA':
        pca.fit(train_container_data)
        train_container_data = pca.transform(train_container_data)

    elif feature_type == 'LDA':
        train_container_data = lda.fit(train_container_data, train_container_labels_raw).transform(train_container_data)

    elif feature_type == 'ICA':
        train_container_data = ica.fit(train_container_data).transform(train_container_data)

    return (train_container_data, train_container_labels, train_container_labels_raw), (
        train_rack_data, train_rack_labels, train_rack_labels_raw)


def get_testing_data(sensor_fusion, feature_type='PREPROCESSED'):
    test_rack_data, test_rack_labels_raw = parse_file(source_dir_path + 'rack_test.csv', sensor_fusion)
    test_container_data, test_container_labels_raw = parse_file(source_dir_path + 'container_test_2I_4I.csv',
                                                                sensor_fusion)

    test_rack_labels = keras.utils.to_categorical(test_rack_labels_raw)
    test_container_labels = keras.utils.to_categorical(test_container_labels_raw)

    if feature_type == 'PREPROCESSED':
        test_container_data = scalar_container.transform(test_container_data)
        test_rack_data = scalar_rack.transform(test_rack_data)
    elif feature_type == 'PCA':
        test_container_data = pca.transform(test_container_data)
    elif feature_type == 'LDA':
        test_container_data = lda.transform(test_container_data)
    elif feature_type == 'ICA':
        test_container_data = ica.transform(test_container_data)

    return (test_rack_data, test_rack_labels, test_rack_labels_raw), (
        test_container_data, test_container_labels, test_container_labels_raw)


def save_model(model, model_name):
    os.makedirs(os.path.dirname(get_dir_path()), exist_ok=True)
    model.save(get_dir_path() + model_name)


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

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.1)


def display_result(actual, predicted, types,
                   classes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                            24]):
    mtx = confusion_matrix(actual, predicted)
    mtx = mtx[1:, 1:]  # remove class 0 - do nothing
    # print('Confusion matrix\n{}\n'.format(mtx))
    precision = precision_score(actual, predicted, average="weighted")
    recall = recall_score(actual, predicted, average="weighted")
    f1score = f1_score(actual, predicted, average="weighted")
    accuracy = accuracy_score(actual, predicted)

    print('Result for : ', types)
    print('Precision : ', precision)
    print('Recall : ', recall)
    print('F1 Score : ', f1score)
    print('Accuracy : {}'.format(accuracy))
    print('Classification Report :\n{}'.format(classification_report(actual, predicted, digits=5)))

    plt.figure(figsize=(12, 12))
    plot_confusion_matrix(mtx,
                          classes=classes, normalize=False, title=types + ' Identification (non normalized)')
    # plt.show()
    os.makedirs(os.path.dirname(config_save_load_dir_path), exist_ok=True)
    plt.savefig(config_save_load_dir_path + types + '_confusion_matrix.png')
    plt.clf()

    return precision, recall, f1score, accuracy


def plot_history(history, types):
    # summarize history for accuracy
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.xlim([0, max(history.epoch)])
    plt.legend(['train', 'test'], loc='upper left')
    os.makedirs(os.path.dirname(config_save_load_dir_path), exist_ok=True)
    plt.savefig(config_save_load_dir_path + types + '_accuracy.png')
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.clf()

    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.xlim([0, max(history.epoch)])
    plt.legend(['train', 'test'], loc='upper left')
    os.makedirs(os.path.dirname(config_save_load_dir_path), exist_ok=True)
    plt.savefig(config_save_load_dir_path + types + '_loss.png')
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.clf()


def display_confidence(array, n=3):
    if array.size < n:
        n = array.size

    top_n_element_index = (-array).argsort()[:n]

    print('\n')
    for index in range(n):
        print(
            '{} : {}%'.format(top_n_element_index[index], "%.3f" % (array[top_n_element_index[index]] * 100)))

    return top_n_element_index


def get_dir_path():
    return config_save_load_dir_path


def get_color_space():
    return color_space


def get_feature_type():
    return feature_type


def get_sensor_fusion():
    return sensor_fusion


def load_configurations_from_files():
    return loadConfigurationsFromFiles


if __name__ == "__main__":
    print('Using machine learning utils')
