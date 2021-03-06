import os
import pickle

import keras
import ml_plots_utils
from numpy import genfromtxt
from sklearn import decomposition
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix, accuracy_score, \
    classification_report
from sklearn.preprocessing import StandardScaler

"""
This is an utility file. Here we can change the configuration related settings. 
The data to be loaded from the file path can be specified here.

To translate the color space from RGB to any other color format please look into the " colorSpaceUtil.py " file. 


The below configuration setting loads the 'XYZ' color space data as input with 'RAW' features from 
"./datarecording_discrete/color_concept_latest/"  folder.


Once the ML training is done, the configuration setting stored in location specified in 'config_save_load_dir_path' variable.

"""

# Configuration related inputs
color_space = 'XYZ'  # HSV, Lab, YCbCr,HSVDegree, XYZ, RGB
feature_type = 'RAW'  # RAW, PREPROCESSED, PCA, LDA, ICA
start_column = 4  # starting column is 4 then we get only color sensor data data, 1 - which include accelerometer
loadConfigurationsFromFiles = False  # True, False
source_dir_path = "./datarecording_discrete/color_concept_latest/" + color_space.lower() + "/"
config_save_load_dir_path = "./configs/color_concept_latest/" + feature_type + "/" + color_space.lower() + "/"

scalar_rack = StandardScaler()
scalar_container = StandardScaler()

pca = decomposition.PCA(n_components=10)
lda = LinearDiscriminantAnalysis(n_components=10)
ica = decomposition.FastICA(n_components=10)


def parse_file(csv_path, start_column=4, end_column=-1, skip_header=0):
    dt = genfromtxt(csv_path, skip_header=skip_header, delimiter=',')
    labels_raw = dt[:, -1]

    # Ignore accelerometer data if start_column = 4.
    if end_column == -1:
        end_column = len(dt[0]) - 1

    data = dt[:, range(start_column, end_column)]

    labels_one_hot = keras.utils.to_categorical(labels_raw)

    return data, labels_raw, labels_one_hot


def get_trainig_data(start_column, feature_type='PREPROCESSED'):
    train_rack_data, train_rack_labels_raw, train_rack_labels = parse_file(source_dir_path + 'rack_train_2I_4I.csv',
                                                                           start_column)
    train_container_data, train_container_labels_raw, train_container_labels = parse_file(
        source_dir_path + 'container_train_2I_4I.csv', start_column)

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


def get_testing_data(start_column, feature_type='PREPROCESSED'):
    test_rack_data, test_rack_labels_raw, test_rack_labels = parse_file(source_dir_path + 'rack_test_2I_4I.csv',
                                                                        start_column)
    test_container_data, test_container_labels_raw, test_container_labels = parse_file(
        source_dir_path + 'container_test_2I_4I.csv', start_column)

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


def save_model(model, model_name, dir_path=config_save_load_dir_path):
    os.makedirs(os.path.dirname(dir_path), exist_ok=True)
    model.save(dir_path + model_name)


def display_result(actual, predicted, title,
                   classes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                            24]):
    mtx = confusion_matrix(actual, predicted)

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
    print('{:.3f}\t{:.3f} \t{:.3f} \t{:.3f}'.format(precision * 100, recall * 100, f1score * 100, accuracy * 100))
    print('Classification Report :\n{}'.format(classification_report(actual, predicted, digits=5)))

    ml_plots_utils.plot_confusion_matrix_2(mtx, normalize=False, title=title, removeNullClass=False)

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
    print('File loaded from : {}'.format(source_dir_path))
    return source_dir_path


def get_dir_path():
    return config_save_load_dir_path


def get_color_space():
    return color_space


def get_feature_type():
    return feature_type


def get_start_column():
    return start_column


def load_configurations_from_files():
    return loadConfigurationsFromFiles


if __name__ == "__main__":
    print('Using machine learning utils')
