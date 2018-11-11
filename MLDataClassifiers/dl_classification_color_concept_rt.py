import traceback
from collections import Counter

import keras
import ml_utils
import numpy as np
import serial as serial
from sklearn.preprocessing import StandardScaler

import colorSpaceUtil

scalar_rack = StandardScaler()
scalar_container = StandardScaler()

if __name__ == "__main__":
    model_bottom = keras.models.load_model(ml_utils.get_dir_path() + 'model_bottom.h5')
    model_left = keras.models.load_model(ml_utils.get_dir_path() + 'model_left.h5')
    model_right = keras.models.load_model(ml_utils.get_dir_path() + 'model_right.h5')
    text_class_model = keras.models.load_model(ml_utils.get_dir_path() + 'text_class_model.h5')

    # device="/dev/tty.usbmodem2853891"
    port = "COM3"  # COM for windows, it changes when we use unix system
    ser = serial.Serial(port, 115200, timeout=None)

    bottom_color = 0.0
    left_color = 0.0
    right_color = 0.0

    bottom_color_list = [0]
    left_color_list = [0]
    right_color_list = [0]

    isBottomPredicted = False

    no_records = 100

    try:
        while True:

            frame_raw = ser.readline().decode('utf-8').rstrip()

            ## frame contains accel+ color data
            dt = frame_raw.split(',')
            if dt.__len__() != 52:
                continue

            colorSpaceConversionFunction = colorSpaceUtil.switcher.get(ml_utils.get_color_space())

            frame = np.asarray([])
            for i in np.arange(4, 52, 4):
                frame = np.append(frame, colorSpaceConversionFunction(float(dt[i]), float(dt[i + 1]), float(dt[i + 2]),
                                                                      float(dt[i + 3])))

            frame = frame.reshape(1, 36)

            frame_bottom = np.append(frame[:, 0:6], frame[:, 30:36]).reshape(1, 12)  # R4, R5 and L4, L5
            frame_left = frame[:, 18:30].reshape(1, 12)  # middle, L1, L2, L3
            frame_right = frame[:, 6:18].reshape(1, 12)  # R3, R2, R1, R0

            result_bottom = model_bottom.predict(frame_bottom, batch_size=1)
            result_left = model_left.predict(frame_left, batch_size=1)
            result_right = model_right.predict(frame_right, batch_size=1)

            result_bottom_predicted = result_bottom.argmax(axis=-1)[0]
            result_left_predicted = result_left.argmax(axis=-1)[0]
            result_right_predicted = result_right.argmax(axis=-1)[0]

            # confidence greater than 50% then only append the data
            if result_bottom_predicted != 0 and (result_bottom[0][result_bottom_predicted] * 100) > 50:
                bottom_color_list.append(result_bottom_predicted)

            if result_left_predicted != 0 and (result_left[0][result_left_predicted] * 100) > 50:
                left_color_list.append(result_left_predicted)

            if result_right_predicted != 0 and (result_right[0][result_right_predicted] * 100) > 50:
                right_color_list.append(result_right_predicted)

            # print("\nBottom Color: ", result_bottom_predicted, " Left Color: ",
            #     result_left_predicted, " Right Color: ", result_right_predicted, )

            # predicted result is nd array of predictions. for single input it is result[0]
            # ml_utils.display_confidence(result_bottom[0])
            # ml_utils.display_confidence(result_left[0])
            # ml_utils.display_confidence(result_right[0])

            if no_records != 0:
                no_records -= 1
            else:

                #  Majority voting
                bottom_color_list_vote = Counter(bottom_color_list)
                left_color_list_vote = Counter(left_color_list)
                right_color_list_vote = Counter(right_color_list)

                bottom_color = float(bottom_color_list_vote.most_common(1)[0][0])
                left_color = float(left_color_list_vote.most_common(1)[0][0])
                right_color = float(right_color_list_vote.most_common(1)[0][0])

                print("\nBottom Vote: ", bottom_color_list_vote)
                print("Left Vote: ", left_color_list_vote)
                print("Right Vote: ", right_color_list_vote)

                #  Text classification
                test_data = np.asarray([bottom_color, left_color, right_color]).reshape(1, 3)
                result_text_class = text_class_model.predict(test_data, batch_size=1)
                print("Box Number: ", result_text_class.argmax(axis=-1))
                # ml_utils.display_confidence(result_text_class[0])

                #  Reset the parameters
                no_records = 100
                bottom_color_list = [0]
                left_color_list = [0]
                right_color_list = [0]

    except:
        traceback.print_exc()
        ser.close()
