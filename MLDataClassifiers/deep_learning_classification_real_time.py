import pickle
import traceback

import deep_learning_classification as dl_clf
import keras
import machine_learning_utils as ml_utils
import numpy as np
import serial as serial
from sklearn.preprocessing import StandardScaler

import colorSpaceUtil

# Configuration related inputs
color_space = 'HSV'  # HSV, Lab, YCbCr,HSVDegree, XYZ, RGB
source_dir_path = "./datarecording_discrete/" + color_space.lower() + "/"
config_save_load_dir_path = "./configs/container_24/" + color_space.lower() + "/"
loadConfigurationsFromFiles = False

scalar_rack = StandardScaler()
scalar_container = StandardScaler()

if __name__ == "__main__":
    (train_container_data, train_container_labels, train_container_labels_raw), (
        train_rack_data, train_rack_labels, train_rack_labels_raw) = ml_utils.get_trainig_data(False, 'raw')
    (test_rack_data, test_rack_labels, test_rack_labels_raw), (
        test_container_data, test_container_labels,
        test_container_labels_raw) = ml_utils.get_testing_data(False, 'raw')

    if loadConfigurationsFromFiles:
        model_rack = keras.models.load_model(ml_utils.get_dir_path() + 'model_rack.h5')
        model_container = keras.models.load_model(ml_utils.get_dir_path() + 'model_container.h5')

        scalar_rack = pickle.load(open(ml_utils.get_dir_path() + "scalar_rack.p", "rb"))
        scalar_container = pickle.load(open(ml_utils.get_dir_path() + "scalar_container.p", "rb"))

        print("Loaded configurations from files !! ")

    else:

        model_rack = dl_clf.build_model(2)
        model_rack.fit(train_rack_data, train_rack_labels, epochs=10,
                       validation_data=(test_rack_data, test_rack_labels), batch_size=500, verbose=2)
        ml_utils.save_model(model_rack, 'model_rack.h5')

        model_container = dl_clf.build_model(25)

        history_container = model_container.fit(train_container_data, train_container_labels, epochs=20,
                                                validation_data=(test_container_data, test_container_labels),
                                                batch_size=1000, verbose=2)
        ml_utils.save_model(model_container, 'model_container.h5')

    # device="/dev/tty.usbmodem2853891"
    port = "COM3"  # COM for windows, it changes when we use unix system
    ser = serial.Serial(port, 115200, timeout=None)

    isRackPredicted = False
    isContainerPredicted = False

    container_predicted = None
    rack_predicted = None

    try:
        while True:

            frame_raw = ser.readline().decode('utf-8').rstrip()

            ## frame contains accel+ color data
            dt = frame_raw.split(',')
            if dt.__len__() != 52:
                continue

            colorSpaceConversionFunction = colorSpaceUtil.switcher.get(color_space)

            frame = np.asarray([])
            for i in np.arange(4, 52, 4):
                frame = np.append(frame, colorSpaceConversionFunction(float(dt[i]), float(dt[i + 1]), float(dt[i + 2]),
                                                                      float(dt[i + 3])))

            frame = frame.reshape(1, 36)

            if not isRackPredicted:
                frame = scalar_rack.transform(frame)
                rack_predicted = model_rack.predict(frame, batch_size=1).argmax(axis=-1)
                if rack_predicted != 0:
                    isRackPredicted = True
                    continue
            elif not isContainerPredicted:
                frame = scalar_container.transform(frame)
                container_predicted = model_container.predict(frame, batch_size=1).argmax(axis=-1)
                if container_predicted != 0:
                    isContainerPredicted = True
                    continue
            elif isContainerPredicted:
                frame = scalar_rack.transform(frame)
                rack_predicted_new = model_rack.predict(frame, batch_size=1).argmax(axis=-1)
                if rack_predicted == rack_predicted_new:
                    isRackPredicted = False
                    isContainerPredicted = False
                    print("Rack Number", rack_predicted, "Container Number", container_predicted)
                    continue
    except:
        traceback.print_exc()
        ser.close()
