import os
import pickle

import keras
import machine_learning_plot_utils as ml_plot_utils
from numpy import genfromtxt
from sklearn import decomposition
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix, accuracy_score, \
    classification_report
from sklearn.preprocessing import StandardScaler

# Configuration related inputs
color_space = 'HSV'  # HSV, Lab, YCbCr,HSVDegree, XYZ, RGB
feature_type = 'LCA'  # RAW, PREPROCESSED, PCA, LDA, LCA
sensor_fusion = False  # True, False
loadConfigurationsFromFiles = False  # True, False
source_dir_path = "./datarecording_discrete/" + color_space.lower() + "/"
config_save_load_dir_path = "./configs/container_24/" + feature_type + "/" + color_space.lower() + "/"

scalar_rack = StandardScaler()
scalar_container = StandardScaler()

pca = decomposition.PCA(n_components=10)
lda = LinearDiscriminantAnalysis(n_components=10)
ica = decomposition.FastICA(n_components=10)


def parse_file(csv_path, sensor_fusion=False):
    dt = genfromtxt(csv_path, delimiter=',')
    labels_raw = dt[:, -1]

    if sensor_fusion:
        # All sensor data, accelerometer and color sensor.
        data = dt[:, range(1, len(dt[0]) - 1)]
    else:
        # Ignore accelerometer data.
        data = dt[:, range(4, len(dt[0]) - 1)]

    labels_one_hot = keras.utils.to_categorical(labels_raw)

    return data, labels_raw, labels_one_hot


def get_trainig_data(sensor_fusion=False, feature_type='PREPROCESSED'):
    train_rack_data, train_rack_labels_raw, train_rack_labels = parse_file(source_dir_path + 'rack_train_2I_4I.csv',
                                                                           sensor_fusion)
    train_container_data, train_container_labels_raw, train_container_labels = parse_file(
        source_dir_path + 'container_train_2I_4I.csv', sensor_fusion)

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
    test_rack_data, test_rack_labels_raw, test_rack_labels = parse_file(source_dir_path + 'rack_test_2I_4I.csv',
                                                                        sensor_fusion)
    test_container_data, test_container_labels_raw, test_container_labels = parse_file(
        source_dir_path + 'container_test_2I_4I.csv', sensor_fusion)

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


def display_result(actual, predicted, title,
                   classes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                            24]):
    mtx = confusion_matrix(actual, predicted)
    mtx = mtx[1:, 1:]  # remove class 0 - do nothing
    # print('Confusion matrix\n{}\n'.format(mtx))
    precision = precision_score(actual, predicted, average="weighted")
    recall = recall_score(actual, predicted, average="weighted")
    f1score = f1_score(actual, predicted, average="weighted")
    accuracy = accuracy_score(actual, predicted)

    print('Result for : ', title)
    print('Precision : ', precision)
    print('Recall : ', recall)
    print('F1 Score : ', f1score)
    print('Accuracy : {}'.format(accuracy))
    print('Classification Report :\n{}'.format(classification_report(actual, predicted, digits=5)))

    ml_plot_utils.plot_confusion_matrix(mtx, normalize=False, title=title)

    return precision, recall, f1score, accuracy


def display_confidence(array, n=3):
    if array.size < n:
        n = array.size

    top_n_element_index = (-array).argsort()[:n]

    print('\n')
    for index in range(n):
        print(
            '{} : {}%'.format(top_n_element_index[index], "%.3f" % (array[top_n_element_index[index]] * 100)))

    return top_n_element_index


def get_source_dir_path():
    return source_dir_path


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
