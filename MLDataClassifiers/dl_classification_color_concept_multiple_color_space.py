import dl_classification as dl_clf
import ml_utils
import numpy as np

# source_dir_path = ml_utils.get_source_dir_path()
source_dir_path_color_space_one = "./datarecording_discrete/color_concept_latest/xyz/"
source_dir_path_color_space_two = "./datarecording_discrete/color_concept_latest/hsv/"
source_dir_path_color_space_three = "./datarecording_discrete/color_concept_latest/rgb/"

config_save_load_dir_path = "./configs/color_concept_latest/multiple_color_space/"

input_shape = 18  # 18 for 3 color space, 12 for two color space

if __name__ == "__main__":
    train_bottom_data_color_space_one, train_bottom_labels_raw, train_bottom_labels = ml_utils.parse_file(
        source_dir_path_color_space_one + 'train_bottom.csv', start_column=4, end_column=10)
    train_left_data_color_space_one, train_left_labels_raw, train_left_labels = ml_utils.parse_file(
        source_dir_path_color_space_one + 'train_left.csv', start_column=7, end_column=13)
    train_right_data_color_space_one, train_right_labels_raw, train_right_labels = ml_utils.parse_file(
        source_dir_path_color_space_one + 'train_right.csv', start_column=7, end_column=13)

    test_bottom_data_color_space_one, test_bottom_labels_raw, test_bottom_labels = ml_utils.parse_file(
        source_dir_path_color_space_one + 'test_bottom.csv', start_column=4, end_column=10)
    test_left_data_color_space_one, test_left_labels_raw, test_left_labels = ml_utils.parse_file(
        source_dir_path_color_space_one + 'test_left.csv', start_column=7, end_column=13)
    test_right_data_color_space_one, test_right_labels_raw, test_right_labels = ml_utils.parse_file(
        source_dir_path_color_space_one + 'test_right.csv', start_column=7, end_column=13)

    train_bottom_data_color_space_two, train_bottom_labels_raw, train_bottom_labels = ml_utils.parse_file(
        source_dir_path_color_space_two + 'train_bottom.csv', start_column=4, end_column=10)
    train_left_data_color_space_two, train_left_labels_raw, train_left_labels = ml_utils.parse_file(
        source_dir_path_color_space_two + 'train_left.csv', start_column=7, end_column=13)
    train_right_data_color_space_two, train_right_labels_raw, train_right_labels = ml_utils.parse_file(
        source_dir_path_color_space_two + 'train_right.csv', start_column=7, end_column=13)

    test_bottom_data_color_space_two, test_bottom_labels_raw, test_bottom_labels = ml_utils.parse_file(
        source_dir_path_color_space_two + 'test_bottom.csv', start_column=4, end_column=10)
    test_left_data_color_space_two, test_left_labels_raw, test_left_labels = ml_utils.parse_file(
        source_dir_path_color_space_two + 'test_left.csv', start_column=7, end_column=13)
    test_right_data_color_space_two, test_right_labels_raw, test_right_labels = ml_utils.parse_file(
        source_dir_path_color_space_two + 'test_right.csv', start_column=7, end_column=13)

    if input_shape == 18:
        train_bottom_data_color_space_three, train_bottom_labels_raw, train_bottom_labels = ml_utils.parse_file(
            source_dir_path_color_space_three + 'train_bottom.csv', start_column=4, end_column=10)
        train_left_data_color_space_three, train_left_labels_raw, train_left_labels = ml_utils.parse_file(
            source_dir_path_color_space_three + 'train_left.csv', start_column=7, end_column=13)
        train_right_data_color_space_three, train_right_labels_raw, train_right_labels = ml_utils.parse_file(
            source_dir_path_color_space_three + 'train_right.csv', start_column=7, end_column=13)

        test_bottom_data_color_space_three, test_bottom_labels_raw, test_bottom_labels = ml_utils.parse_file(
            source_dir_path_color_space_three + 'test_bottom.csv', start_column=4, end_column=10)
        test_left_data_color_space_three, test_left_labels_raw, test_left_labels = ml_utils.parse_file(
            source_dir_path_color_space_three + 'test_left.csv', start_column=7, end_column=13)
        test_right_data_color_space_three, test_right_labels_raw, test_right_labels = ml_utils.parse_file(
            source_dir_path_color_space_three + 'test_right.csv', start_column=7, end_column=13)

        train_bottom_data = np.concatenate(
            (train_bottom_data_color_space_one, train_bottom_data_color_space_two, train_bottom_data_color_space_three),
            axis=1)
        train_left_data = np.concatenate(
            (train_left_data_color_space_one, train_left_data_color_space_two, train_left_data_color_space_three),
            axis=1)
        train_right_data = np.concatenate(
            (train_right_data_color_space_one, train_right_data_color_space_two, train_right_data_color_space_three),
            axis=1)

        test_bottom_data = np.concatenate(
            (test_bottom_data_color_space_one, test_bottom_data_color_space_two, test_bottom_data_color_space_three),
            axis=1)
        test_left_data = np.concatenate(
            (test_left_data_color_space_one, test_left_data_color_space_two, test_left_data_color_space_three), axis=1)
        test_right_data = np.concatenate(
            (test_right_data_color_space_one, test_right_data_color_space_two, test_right_data_color_space_three),
            axis=1)

    else:
        train_bottom_data = np.concatenate((train_bottom_data_color_space_one, train_bottom_data_color_space_two),
                                           axis=1)
        train_left_data = np.concatenate((train_left_data_color_space_one, train_left_data_color_space_two), axis=1)
        train_right_data = np.concatenate((train_right_data_color_space_one, train_right_data_color_space_two), axis=1)

        test_bottom_data = np.concatenate((test_bottom_data_color_space_one, test_bottom_data_color_space_two), axis=1)
        test_left_data = np.concatenate((test_left_data_color_space_one, test_left_data_color_space_two), axis=1)
        test_right_data = np.concatenate((test_right_data_color_space_one, test_right_data_color_space_two), axis=1)

    # earlyStopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, verbose=1, mode='auto')

    model_bottom = dl_clf.build_model(5, input_shape)
    history_bottom = model_bottom.fit(train_bottom_data, train_bottom_labels, epochs=20,
                                      validation_data=(test_bottom_data, test_bottom_labels), batch_size=500, verbose=2)

    model_left = dl_clf.build_model(7, input_shape)
    history_left = model_left.fit(train_left_data, train_left_labels, epochs=20,
                                  validation_data=(test_left_data, test_left_labels), batch_size=500, verbose=2)

    model_right = dl_clf.build_model(8, input_shape)
    history_right = model_right.fit(train_right_data, train_right_labels, epochs=20,
                                    validation_data=(test_right_data, test_right_labels), batch_size=500, verbose=2)

    ml_utils.save_model(model_bottom, 'model_bottom.h5', config_save_load_dir_path)
    ml_utils.save_model(model_left, 'model_left.h5', config_save_load_dir_path)
    ml_utils.save_model(model_right, 'model_right.h5', config_save_load_dir_path)

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
