import keras
import ml_utils
import dl_classification as dl_clf
import numpy as np

#source_dir_path = ml_utils.get_source_dir_path()
source_dir_path_hsv = "./datarecording_discrete/color_concept/hsv/"
source_dir_path_xyz = "./datarecording_discrete/color_concept/xyz/"


if __name__ == "__main__":
    train_bottom_data_hsv, train_bottom_labels_raw, train_bottom_labels = ml_utils.parse_file(
        source_dir_path_hsv + 'train_bottom.csv')
    train_left_data_hsv, train_left_labels_raw, train_left_labels = ml_utils.parse_file(
        source_dir_path_hsv + 'train_left.csv')
    train_right_data_hsv, train_right_labels_raw, train_right_labels = ml_utils.parse_file(
        source_dir_path_hsv + 'train_right.csv')

    test_bottom_data_hsv, test_bottom_labels_raw, test_bottom_labels = ml_utils.parse_file(
        source_dir_path_hsv + 'test_bottom.csv')
    test_left_data_hsv, test_left_labels_raw, test_left_labels = ml_utils.parse_file(
        source_dir_path_hsv + 'test_left.csv')
    test_right_data_hsv, test_right_labels_raw, test_right_labels = ml_utils.parse_file(
        source_dir_path_hsv + 'test_right.csv')

    train_bottom_data_xyz, train_bottom_labels_raw, train_bottom_labels = ml_utils.parse_file(
        source_dir_path_xyz + 'train_bottom.csv')
    train_left_data_xyz, train_left_labels_raw, train_left_labels = ml_utils.parse_file(
        source_dir_path_xyz + 'train_left.csv')
    train_right_data_xyz, train_right_labels_raw, train_right_labels = ml_utils.parse_file(
        source_dir_path_xyz + 'train_right.csv')

    test_bottom_data_xyz, test_bottom_labels_raw, test_bottom_labels = ml_utils.parse_file(
        source_dir_path_xyz + 'test_bottom.csv')
    test_left_data_xyz, test_left_labels_raw, test_left_labels = ml_utils.parse_file(
        source_dir_path_xyz + 'test_left.csv')
    test_right_data_xyz, test_right_labels_raw, test_right_labels = ml_utils.parse_file(
        source_dir_path_xyz + 'test_right.csv')

    train_bottom_data = np.concatenate((train_bottom_data_hsv, train_bottom_data_xyz), axis=1)
    train_left_data = np.concatenate((train_left_data_hsv, train_left_data_xyz), axis=1)
    train_right_data = np.concatenate((train_right_data_hsv, train_right_data_xyz), axis=1)

    test_bottom_data = np.concatenate((test_bottom_data_hsv, test_bottom_data_xyz), axis=1)
    test_left_data = np.concatenate((test_left_data_hsv, test_left_data_xyz), axis=1)
    test_right_data = np.concatenate((test_right_data_hsv, test_right_data_xyz), axis=1)

    # earlyStopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, verbose=1, mode='auto')

    model_bottom = dl_clf.build_model(5, 24)
    history_bottom = model_bottom.fit(train_bottom_data, train_bottom_labels, epochs=10,
                                      validation_data=(test_bottom_data, test_bottom_labels), batch_size=500, verbose=2)

    model_left = dl_clf.build_model(7, 24)
    history_left = model_left.fit(train_left_data, train_left_labels, epochs=10,
                                  validation_data=(test_left_data, test_left_labels), batch_size=500, verbose=2)

    model_right = dl_clf.build_model(8, 24)
    history_right = model_right.fit(train_right_data, train_right_labels, epochs=10,
                                    validation_data=(test_right_data, test_right_labels), batch_size=500, verbose=2)

    ml_utils.save_model(model_bottom, 'model_bottom.h5')
    ml_utils.save_model(model_left, 'model_left.h5')
    ml_utils.save_model(model_right, 'model_right.h5')

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
