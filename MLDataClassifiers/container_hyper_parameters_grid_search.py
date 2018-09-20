import time

import keras
import tensorflow as tf
from keras.wrappers.scikit_learn import KerasClassifier
from numpy import genfromtxt
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

# Configuration related inputs
color_space = 'HSV'  # HSV, Lab, YCbCr,HSVDegree, XYZ, RGB
source_dir_path = "./datarecording_discrete/" + color_space.lower() + "/"
config_save_load_dir_path = "./configs/container_24/" + color_space.lower() + "/"
loadConfigurationsFromFiles = False

scalar_rack = StandardScaler()
scalar_container = StandardScaler()


def build_model(optimizer):
    model = tf.keras.Sequential()
    # Must define the input shape in the first layer of the neural network
    model.add(tf.keras.layers.Dense(1024, input_shape=(36,), activation=tf.nn.relu,
                                    kernel_regularizer=keras.regularizers.l2(0.001)))
    model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(1024, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001)))
    model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(612, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001)))
    # model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(256, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001)))
    model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001)))
    # model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(25, activation='softmax'))
    # Take a look at the model summary
    model.summary()
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer=optimizer,  # rmsprop, adam
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
    train_container_labels = keras.utils.to_categorical(train_container_labels_raw, 25)

    return (train_container_data, train_container_labels, train_container_labels_raw), (
        train_rack_data, train_rack_labels, train_rack_labels_raw)


def get_testing_data():
    test_rack_data, test_rack_labels_raw = parse_file(source_dir_path + 'rack_test.csv')
    test_rack_data = scalar_rack.transform(test_rack_data)
    test_rack_labels = keras.utils.to_categorical(test_rack_labels_raw)

    test_container_data, test_container_labels_raw = parse_file(source_dir_path + 'container_test_4I.csv')
    test_container_data = scalar_container.transform(test_container_data)
    test_container_labels = keras.utils.to_categorical(test_container_labels_raw, 25)

    return (test_rack_data, test_rack_labels, test_rack_labels_raw), (
        test_container_data, test_container_labels, test_container_labels_raw)


if __name__ == "__main__":
    start_time = time.time()

    (train_container_data, train_container_labels, train_container_labels_raw), (
        train_rack_data, train_rack_labels, train_rack_labels_raw) = get_trainig_data()
    (test_rack_data, test_rack_labels, test_rack_labels_raw), (
        test_container_data, test_container_labels, test_container_labels_raw) = get_testing_data()

    # Fine tuning the parameters
    kerasClassifier = KerasClassifier(build_fn=build_model)
    param = {'epochs': [10, 20, 30, 40, 50],
             'batch_size': [500, 1000, 2000, 3000],
             'optimizer': ['SGD', 'RMSprop', 'Adagrad', 'Adadelta', 'Adam', 'Adamax', 'Nadam'],
             }

    grid_search = GridSearchCV(estimator=kerasClassifier, param_grid=param, scoring='accuracy', cv=10)
    grid_search.fit(train_container_data, train_container_labels_raw)
    print("Best: %f using %s" % (grid_search.best_score_, grid_search.best_params_))

    elapsed_time = time.time() - start_time
    print('Time taken for searching best parameter{}'.format(elapsed_time))
