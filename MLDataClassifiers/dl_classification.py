import time

import keras
import ml_plots_utils
import ml_utils
import tensorflow as tf
from keras.utils.vis_utils import plot_model

"""
This file consist of handcrafted ML Model. The all ML model uses this 'build_model' to create a model.

The main method does not work due to the change in the implementation.
 
Please use 'dl_classification_color_concept.py' file to run the following model. 
"""

def build_model(number_class, input_shape=36, plot_model_arch=False):
    model = tf.keras.Sequential()
    # Must define the input shape in the first layer of the neural network
    # model.add(tf.keras.layers.Dense(1024, input_shape=(36,), activation=tf.nn.relu,kernel_regularizer=keras.regularizers.l2(0.001)))
    # model.add(tf.keras.layers.Dropout(0.3))
    # model.add(tf.keras.layers.Dense(1024, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001)))
    # model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(512, input_shape=(input_shape,), activation=tf.nn.relu,
                                    kernel_regularizer=keras.regularizers.l2(0.001)))
    # model.add(tf.keras.layers.Flatten())
    # model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(256, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001)))
    # model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001)))
    model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(number_class, activation='softmax'))
    # Take a look at the model summary
    model.summary()
    model.compile(loss='categorical_crossentropy',
                  optimizer='Adamax',  # rmsprop, adam, Adamax
                  metrics=['accuracy'])
    if plot_model_arch:
        plot_model(model, show_shapes=True, to_file=ml_utils.get_dir_path() + 'color_classifier_model.png')

    return model


if __name__ == "__main__":
    (train_container_data, train_container_labels, train_container_labels_raw), (
        train_rack_data, train_rack_labels, train_rack_labels_raw) = ml_utils.get_trainig_data(
        ml_utils.get_start_column(), ml_utils.get_feature_type())
    (test_rack_data, test_rack_labels, test_rack_labels_raw), (
        test_container_data, test_container_labels,
        test_container_labels_raw) = ml_utils.get_testing_data(ml_utils.get_start_column(),
                                                               ml_utils.get_feature_type())

    # if ml_utils.load_configurations_from_files():
    if False:  # remove the default fault operation and enable above statement
        model_rack = keras.models.load_model(ml_utils.get_dir_path() + 'model_rack.h5')
        model_container = keras.models.load_model(ml_utils.get_dir_path() + 'model_container.h5')
        print("Loaded configurations from files !! ")

    else:

        earlyStopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, verbose=1, mode='auto')

        model_rack = build_model(5)
        history_rack = model_rack.fit(train_rack_data, train_rack_labels, epochs=10,
                                      validation_data=(test_rack_data, test_rack_labels), batch_size=500, verbose=2,
                                      callbacks=[earlyStopping])
        ml_utils.save_model(model_rack, 'model_rack.h5')

        model_container = build_model(25)
        start_time = time.time()
        history_container = model_container.fit(train_container_data, train_container_labels, epochs=50,
                                                validation_data=(test_container_data, test_container_labels),
                                                batch_size=1000, verbose=2, callbacks=[earlyStopping])
        elapsed_time = time.time() - start_time
        print('Deep Learning Training time: {}'.format(elapsed_time))
        ml_utils.save_model(model_container, 'model_container.h5')

    test_predicted_container_res = model_container.predict(test_container_data, batch_size=1)

    test_predicted_rack_res = model_rack.predict(test_rack_data, batch_size=1).argmax(axis=-1)

    # print('Color Space: {}'.format(color_space))
    print('\n****************Classification result for rack************************')
    ml_utils.display_result(test_rack_labels_raw, test_predicted_rack_res, 'rack')  # Print the classification result

    print('\n****************Classification result for container************************')
    ml_utils.display_result(test_container_labels_raw, test_predicted_container_res.argmax(axis=1),
                            'container')  # Print the classification result
    # for result in test_predicted_container_res:
    # ml_utils.display_confidence(result)

    if not ml_utils.load_configurations_from_files():  # If parameters are loaded from file then we can not get history.
        ml_plots_utils.plot_history(history_rack, 'rack')
        ml_plots_utils.plot_history(history_container, 'container')
