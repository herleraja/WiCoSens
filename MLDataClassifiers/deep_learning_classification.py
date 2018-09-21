import os
import pickle
import time

import keras
import machine_learning_utils as machine_learning_utils
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

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


def save_configurations():
    os.makedirs(os.path.dirname(config_save_load_dir_path), exist_ok=True)

    # model_rack.save(config_save_load_dir_path + 'model_rack.h5')
    model_container.save(config_save_load_dir_path + 'model_container.h5')
    pickle.dump(scalar_rack, open(config_save_load_dir_path + "scalar_rack.p", "wb"))
    pickle.dump(scalar_container, open(config_save_load_dir_path + "scalar_container.p", "wb"))

    print("Saved machine learning models and scalar configuration into files !!")


if __name__ == "__main__":
    (train_container_data, train_container_labels, train_container_labels_raw), (
        train_rack_data, train_rack_labels, train_rack_labels_raw) = machine_learning_utils.get_trainig_data()
    (test_rack_data, test_rack_labels, test_rack_labels_raw), (
        test_container_data, test_container_labels,
        test_container_labels_raw) = machine_learning_utils.get_testing_data()

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
        machine_learning_utils.save_model(model_rack, 'model_rack.h5')

        model_container = build_model(25)
        start_time = time.time()
        history_container = model_container.fit(train_container_data, train_container_labels, epochs=20,
                                                validation_data=(test_container_data, test_container_labels),
                                                batch_size=1000)
        elapsed_time = time.time() - start_time
        print('Deep Learning Training time: {}'.format(elapsed_time))
        machine_learning_utils.save_model(model_container, 'model_container.h5')

    test_predicted_container_res = model_container.predict(test_container_data, batch_size=1).argmax(axis=-1)

    test_predicted_rack_res = model_rack.predict(test_rack_data, batch_size=1).argmax(axis=-1)

    print('Color Space: {}'.format(color_space))
    print('\n****************Classification result for rack************************')
    machine_learning_utils.display_result(test_rack_labels_raw, test_predicted_rack_res, 'rack')  # Print the classification result

    print('\n****************Classification result for container************************')
    machine_learning_utils.display_result(test_container_labels_raw, test_predicted_container_res,
                                          'container')  # Print the classification result
    machine_learning_utils.plot_history(history_container, 'container')
