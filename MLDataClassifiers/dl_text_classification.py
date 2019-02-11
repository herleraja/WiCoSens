import keras
import ml_utils
import tensorflow as tf

"""
The following file is used to create a text classification model. 
The input for the text classification is in  folder ' /datarecording_discrete/text/ '
"""

source_dir_path = "./datarecording_discrete/text/"

train_data, train_labels_raw, train_labels = ml_utils.parse_file(
    source_dir_path + 'text_train.csv', start_column=0, skip_header=1)

test_data, test_labels_raw, test_labels = ml_utils.parse_file(
    source_dir_path + 'text_test.csv', start_column=0, skip_header=1)


def build_model(number_class=169):
    # 1-Red, 2-Yellow, 3-Light Green, 4-Light Blue, 5-Magenta, 6-Orange, 7-Purple and 0- Unknown color.
    # So total of 8 colors so vocab_size  = 8.
    vocab_size = 8
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Embedding(vocab_size, 16, input_length=3))
    model.add(tf.keras.layers.LSTM(100))
    model.add(tf.keras.layers.Dense(number_class, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # model.summary()
    # plot_model(model, show_shapes=True, to_file=source_dir_path + 'text_class_model.png')

    return model


text_class_model = build_model(113)

earlyStopping = keras.callbacks.EarlyStopping(monitor='loss', patience=10, verbose=1, mode='auto')

text_class_model.fit(train_data, train_labels, epochs=50, batch_size=5, callbacks=[earlyStopping])

ml_utils.save_model(text_class_model, 'text_class_model.h5')

test_predicted_res = text_class_model.predict(test_data, batch_size=1)

print('\n****************Classification result for text classification************************')
ml_utils.display_result(test_labels_raw, test_predicted_res.argmax(axis=1),
                        'text classification')  # Print the classification result

# for result in test_predicted_res:
#    ml_utils.display_confidence(result)
