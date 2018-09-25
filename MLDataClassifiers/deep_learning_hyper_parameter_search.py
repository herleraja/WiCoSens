import time

import keras
import machine_learning_utils as ml_utils
import tensorflow as tf
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV


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


if __name__ == "__main__":
    start_time = time.time()

    (train_container_data, train_container_labels, train_container_labels_raw), (
        train_rack_data, train_rack_labels, train_rack_labels_raw) = ml_utils.get_trainig_data()
    (test_rack_data, test_rack_labels, test_rack_labels_raw), (
        test_container_data, test_container_labels, test_container_labels_raw) = ml_utils.get_testing_data()

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
