import colorsys
import os
import traceback

import numpy as np
from numpy import genfromtxt


def rgbc2YCbCr(r, g, b, c=0):
    if c != 0:
        r, g, b = r / c, g / c, b / c  # Normalising the rgb data by dividing by clear bit

    # Conversion Matrix
    matrix = [[65.481, 128.553, 24.966],
              [-37.797, -74.203, 112],
              [112, -93.786, -18.214]]

    # RGB values lie between 0 to 1.0
    rgb = [r, g, b]  # RGB

    cie = np.dot(matrix, rgb);

    cie = cie * 1 / 255

    cie = cie + [16, 128, 128]

    return cie[0], cie[1], cie[2]


def rgbc2lab(r, g, b, c=0):
    if c != 0:
        r, g, b = r / c, g / c, b / c  # Normalising the rgb data by dividing by clear bit

    # Conversion Matrix
    matrix = [[0.412453, 0.357580, 0.180423],
              [0.212671, 0.715160, 0.072169],
              [0.019334, 0.119193, 0.950227]]

    # RGB values lie between 0 to 1.0
    rgb = [r, g, b]  # RGB

    cie = np.dot(matrix, rgb);

    cie[0] = cie[0] / 0.950456;
    cie[2] = cie[2] / 1.088754;

    # Calculate the L
    L = 116 * np.power(cie[1], 1 / 3.0) - 16.0 if cie[1] > 0.008856 else 903.3 * cie[1];

    # Calculate the a
    a = 500 * (lab_func(cie[0]) - lab_func(cie[1]));

    # Calculate the b
    b = 200 * (lab_func(cie[1]) - lab_func(cie[2]));

    return L, a, b


def lab_func(t):
    if t > 0.008856:
        return np.power(t, 1 / 3.0);
    else:
        return 7.787 * t + 16 / 116.0;


def rgbc2hsvDegree(r, g, b, c=0):
    if c != 0:
        r, g, b = r / c, g / c, b / c  # Normalising the rgb data by dividing by clear bit

    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r and g >= b:
        h = (60 * ((g - b) / df) + 0) % 360
    elif mx == r and g < b:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360

    if mx == 0:
        s = 0
    else:
        s = df / mx
    v = mx
    return h, s, v


def rgbc2hsv(r, g, b, c=0):
    if c != 0:
        r, g, b = r / c, g / c, b / c  # Normalising the rgb data by dividing by clear bit
    hsv = colorsys.rgb_to_hsv(r, g, b)
    return hsv[0], hsv[1], hsv[2]


def rgbc2rgb(r, g, b, c=0):
    if c != 0:
        r, g, b = r / c, g / c, b / c  # Normalising the rgb data by dividing by clear bit
    return r, g, b


def rgbc2CieXYZ(r, g, b, c=0):
    if c != 0:
        r, g, b = r / c, g / c, b / c  # Normalising the rgb data by dividing by clear bit

    # Conversion Matrix
    matrix = [[0.49, 0.31, 0.20],
              [0.17697, 0.81240, 0.01063],
              [0.0, 0.01, 0.99]]

    matrix = np.array(matrix)
    matrix = matrix / 0.17697

    # RGB values lie between 0 to 1.0
    rgb = [r, g, b]  # RGB

    cie = np.dot(matrix, rgb);

    return cie[0], cie[1], cie[2]


switcher = {
    'YCbCr': rgbc2YCbCr,
    'XYZ': rgbc2CieXYZ,
    'Lab': rgbc2lab,
    'HSVDegree': rgbc2hsvDegree,
    'HSV': rgbc2hsv,
    'RGB': rgbc2rgb
}


def fileColorSpaceConversionFunction(current_csv_file_path, new_converted_csv_file_path=None, color_Space='HSV'):
    colorSpaceConversionFunction = switcher.get(color_Space)

    dt = genfromtxt(current_csv_file_path, delimiter=',')
    labels = dt[:, -1]

    # For now, ignore accelerometer.
    dt_all_colors = dt[:, range(4, len(dt[0]) - 1)]

    if new_converted_csv_file_path is None:
        current_csv_file_path_split = current_csv_file_path.split('.csv')
        new_converted_csv_file_path = current_csv_file_path_split[0] + '_' + color_Space.lower() + '.csv'
    new_converted_csv_file = open(new_converted_csv_file_path, 'a')

    for i in range(len(dt_all_colors)):
        new_line = str(dt[i][0]) + ',' + str(dt[i][1]) + ',' + str(dt[i][2]) + ',' + str(dt[i][3])

        for j in np.arange(0, len(dt_all_colors[i]), 3):
            converted_value = colorSpaceConversionFunction(float(dt_all_colors[i][j]), float(dt_all_colors[i][j + 1]),
                                                           float(dt_all_colors[i][j + 2]))
            new_line += ',' + str(converted_value[0]) + ',' + str(converted_value[1]) + ',' + str(converted_value[2])

        new_line = new_line + ',' + str(int(dt[i][-1])) + '\n'

        new_converted_csv_file.write(new_line)
        new_converted_csv_file.flush()

    new_converted_csv_file.close()


if __name__ == "__main__":
    try:

        # To test the file conversion method.

        color_Space = 'XYZ'  # HSV, Lab, YCbCr,HSVDegree, XYZ, RGB
        source_dir_path = "./MLDataClassifiers/data1/rgb/"
        destination_dir_path = "./MLDataClassifiers/data1/" + color_Space.lower() + "/"
        os.makedirs(os.path.dirname(destination_dir_path), exist_ok=True)

        fileColorSpaceConversionFunction(source_dir_path + 'rack_test.csv', destination_dir_path + 'rack_test.csv',
                                         color_Space=color_Space)
        fileColorSpaceConversionFunction(source_dir_path + 'rack_train.csv', destination_dir_path + 'rack_train.csv',
                                         color_Space=color_Space)
        fileColorSpaceConversionFunction(source_dir_path + 'container_test.csv',
                                         destination_dir_path + 'container_test.csv',
                                         color_Space=color_Space)
        fileColorSpaceConversionFunction(source_dir_path + 'rack2_container_train.csv',
                                         destination_dir_path + 'rack2_container_train.csv',
                                         color_Space=color_Space)

        print("The files are converted to ***", color_Space, "*** color space")


    except:
        traceback.print_exc()
