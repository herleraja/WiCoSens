import os
import pickle

import dl_classification as dl_clf
import ml_utils
from sklearn.preprocessing import StandardScaler

"""
We build handcrafted ML model and train the model using data from left, right and bottom color sensors. 
The data loaded form 'source_dir_path' which is a configuration setting in 'ml_utils.py' file.

"""

source_dir_path = ml_utils.get_source_dir_path()

if __name__ == "__main__":

    train_bottom_data, train_bottom_labels_raw, train_bottom_labels = ml_utils.parse_file(
        source_dir_path + 'train_bottom.csv', start_column=4, end_column=10)
    train_left_data, train_left_labels_raw, train_left_labels = ml_utils.parse_file(
        source_dir_path + 'train_left.csv', start_column=7, end_column=13)
    train_right_data, train_right_labels_raw, train_right_labels = ml_utils.parse_file(
        source_dir_path + 'train_right.csv', start_column=7, end_column=13)

    test_bottom_data, test_bottom_labels_raw, test_bottom_labels = ml_utils.parse_file(
        source_dir_path + 'test_bottom.csv', start_column=4, end_column=10)
    test_left_data, test_left_labels_raw, test_left_labels = ml_utils.parse_file(
        source_dir_path + 'test_left.csv', start_column=7, end_column=13)
    test_right_data, test_right_labels_raw, test_right_labels = ml_utils.parse_file(
        source_dir_path + 'test_right.csv', start_column=7, end_column=13)

    if ml_utils.get_feature_type() == 'PREPROCESSED':
        bottom_preprocessor = StandardScaler()
        left_preprocessor = StandardScaler()
        right_preprocessor = StandardScaler()

        bottom_preprocessor.fit(train_bottom_data)
        left_preprocessor.fit(train_left_data)
        right_preprocessor.fit(train_right_data)

        os.makedirs(os.path.dirname(ml_utils.get_dir_path()), exist_ok=True)
        pickle.dump(bottom_preprocessor, open(ml_utils.get_dir_path() + "bottom_preprocessor.p", "wb"))
        pickle.dump(left_preprocessor, open(ml_utils.get_dir_path() + "left_preprocessor.p", "wb"))
        pickle.dump(right_preprocessor, open(ml_utils.get_dir_path() + "right_preprocessor.p", "wb"))

        train_bottom_data = bottom_preprocessor.transform(train_bottom_data)
        train_left_data = left_preprocessor.transform(train_left_data)
        train_right_data = right_preprocessor.transform(train_right_data)

        test_bottom_data = bottom_preprocessor.transform(test_bottom_data)
        test_left_data = left_preprocessor.transform(test_left_data)
        test_right_data = right_preprocessor.transform(test_right_data)

    # earlyStopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, verbose=1, mode='auto')

    model_bottom = dl_clf.build_model(5, 6)
    history_bottom = model_bottom.fit(train_bottom_data, train_bottom_labels, epochs=10,
                                      validation_data=(test_bottom_data, test_bottom_labels), batch_size=500, verbose=2)

    model_left = dl_clf.build_model(7, 6)
    history_left = model_left.fit(train_left_data, train_left_labels, epochs=10,
                                  validation_data=(test_left_data, test_left_labels), batch_size=500, verbose=2)

    model_right = dl_clf.build_model(8, 6)
    history_right = model_right.fit(train_right_data, train_right_labels, epochs=10,
                                    validation_data=(test_right_data, test_right_labels), batch_size=500, verbose=2)

    ml_utils.save_model(model_bottom, 'model_bottom.h5')
    ml_utils.save_model(model_left, 'model_left.h5')
    ml_utils.save_model(model_right, 'model_right.h5')

test_predicted_bottom_res = model_bottom.predict(test_bottom_data, batch_size=1)
print('\n****************Classification result for Bottom************************')
ml_utils.display_result(test_bottom_labels_raw, test_predicted_bottom_res.argmax(axis=1),
                        'Bottom')  # Print the classification result

# for result in test_predicted_bottom_res:
#    ml_utils.display_confidence(result)

test_predicted_left_res = model_left.predict(test_left_data, batch_size=1)
print('\n****************Classification result for Left************************')
ml_utils.display_result(test_left_labels_raw, test_predicted_left_res.argmax(axis=1),
                        'Left')  # Print the classification result
# for result in test_predicted_left_res:
#    ml_utils.display_confidence(result)

test_predicted_right_res = model_right.predict(test_right_data, batch_size=1)
print('\n****************Classification result for Right************************')
ml_utils.display_result(test_right_labels_raw, test_predicted_right_res.argmax(axis=1),
                        'Right')  # Print the classification result
# for result in test_predicted_right_res:
#    ml_utils.display_confidence(result)
