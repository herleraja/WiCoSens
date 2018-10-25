import keras
import ml_utils
import tensorflow as tf
from keras.utils.vis_utils import plot_model
from sklearn.preprocessing import StandardScaler

scalar_rack = StandardScaler()
scalar_container = StandardScaler()

source_dir_path = "./datarecording_discrete/color_concept/"


def build_model(number_class):
    model = tf.keras.Sequential()
    # Must define the input shape in the first layer of the neural network
    # model.add(tf.keras.layers.Dense(1024, input_shape=(36,), activation=tf.nn.relu,kernel_regularizer=keras.regularizers.l2(0.001)))
    # model.add(tf.keras.layers.Dropout(0.3))
    # model.add(tf.keras.layers.Dense(1024, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001)))
    # model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(612, input_shape=(12,), activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001)))
    # model.add(tf.keras.layers.Flatten())
    # model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(256, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001)))
    model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001)))
    # model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(number_class, activation='softmax'))
    # Take a look at the model summary
    #model.summary()
    #plot_model(model, show_shapes=True, to_file=source_dir_path+'color_model.png')
    model.compile(loss='categorical_crossentropy',
                  optimizer='Adamax',  # rmsprop, adam, Adamax
                  metrics=['accuracy'])
    return model

if __name__ == "__main__":
    train_bottom_data, train_bottom_labels_raw, train_bottom_labels = ml_utils.parse_file(
        source_dir_path + 'train_bottom.csv')
    train_left_data, train_left_labels_raw, train_left_labels = ml_utils.parse_file(
        source_dir_path + 'train_left.csv')
    train_right_data, train_right_labels_raw, train_right_labels = ml_utils.parse_file(
        source_dir_path + 'train_right.csv')

    test_bottom_data, test_bottom_labels_raw, test_bottom_labels = ml_utils.parse_file(
        source_dir_path + 'test_bottom.csv')
    test_left_data, test_left_labels_raw, test_left_labels = ml_utils.parse_file(
        source_dir_path + 'test_left.csv')
    test_right_data, test_right_labels_raw, test_right_labels = ml_utils.parse_file(
        source_dir_path + 'test_right.csv')

    # earlyStopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, verbose=1, mode='auto')

    model_bottom = build_model(5)
    history_bottom = model_bottom.fit(train_bottom_data, train_bottom_labels, epochs=10,
                                      validation_data=(test_bottom_data, test_bottom_labels), batch_size=500, verbose=2)

    model_left = build_model(7)
    history_left = model_left.fit(train_left_data, train_left_labels, epochs=10,
                                  validation_data=(test_left_data, test_left_labels), batch_size=500, verbose=2)

    model_right = build_model(8)
    history_right = model_right.fit(train_right_data, train_right_labels, epochs=10,
                                    validation_data=(test_right_data, test_right_labels), batch_size=500, verbose=2)

    ml_utils.save_model(model_bottom, 'model_bottom.h5', source_dir_path)
    ml_utils.save_model(model_left, 'model_left.h5', source_dir_path)
    ml_utils.save_model(model_right, 'model_right.h5', source_dir_path)

test_predicted_bottom_res = model_bottom.predict(test_bottom_data, batch_size=1)
print('\n****************Classification result for Bottom************************')
ml_utils.display_result(test_bottom_labels_raw, test_predicted_bottom_res.argmax(axis=1),
                        'Bottom')  # Print the classification result

#for result in test_predicted_bottom_res:
#    ml_utils.display_confidence(result)

test_predicted_left_res = model_left.predict(test_left_data, batch_size=1)
print('\n****************Classification result for Left************************')
ml_utils.display_result(test_left_labels_raw, test_predicted_left_res.argmax(axis=1),
                        'Left')  # Print the classification result
#for result in test_predicted_left_res:
#    ml_utils.display_confidence(result)

test_predicted_right_res = model_right.predict(test_right_data, batch_size=1)
print('\n****************Classification result for Right************************')
ml_utils.display_result(test_right_labels_raw, test_predicted_right_res.argmax(axis=1),
                        'Right')  # Print the classification result
#for result in test_predicted_right_res:
#    ml_utils.display_confidence(result)
