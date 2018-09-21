import itertools
import os
import pickle

import keras
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix, accuracy_score, \
    classification_report
from sklearn.preprocessing import StandardScaler

# Configuration related inputs
color_space = 'HSV'  # HSV, Lab, YCbCr,HSVDegree, XYZ, RGB
source_dir_path = "./datarecording_discrete/" + color_space.lower() + "/"
config_save_load_dir_path = "./configs/container_24/" + color_space.lower() + "/"
loadConfigurationsFromFiles = False

scalar_rack = StandardScaler()
scalar_container = StandardScaler()


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

    os.makedirs(os.path.dirname(config_save_load_dir_path), exist_ok=True)
    pickle.dump(scalar_rack, open(config_save_load_dir_path + "scalar_rack.p", "wb"))
    pickle.dump(scalar_container, open(config_save_load_dir_path + "scalar_container.p", "wb"))

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


def save_model(model, model_name):
    os.makedirs(os.path.dirname(config_save_load_dir_path), exist_ok=True)
    model.save(config_save_load_dir_path + model_name)
    # model_rack.save(config_save_load_dir_path + 'model_rack.h5')
    # model_container.save(config_save_load_dir_path + 'model_container.h5')


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
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)


def display_result(actual, predicted, types,
                   classes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                            24]):
    mtx = confusion_matrix(actual, predicted)
    mtx = mtx[1:, 1:]  # remove class 0 - do nothing
    # print('Confusion matrix\n{}\n'.format(mtx))
    print('Precision : ', precision_score(actual, predicted, average="weighted"))
    print('Recall : ', recall_score(actual, predicted, average="weighted"))
    print('F1 Score : ', f1_score(actual, predicted, average="weighted"))
    print('Accuracy : {}'.format(accuracy_score(actual, predicted)))
    print('Classification Report :\n{}'.format(classification_report(actual, predicted, digits=5)))

    plt.figure(figsize=(12, 12))
    plot_confusion_matrix(mtx,
                          classes=classes, normalize=False, title=types + 'Identification (non normalized)')
    # plt.show()
    plt.savefig(config_save_load_dir_path + types + '_confusion_matrix.png')
    plt.clf()


def plot_history(history, types):
    # summarize history for accuracy
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.xlim([0, max(history.epoch)])
    plt.legend(['train', 'test'], loc='upper left')
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
    plt.savefig(config_save_load_dir_path + types + '_loss.png')
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.clf()


if __name__ == "__main__":
    print('Using machine learning utils')