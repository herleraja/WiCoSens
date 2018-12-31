import itertools
import os

import matplotlib.pyplot as plt
import ml_utils
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from numpy import genfromtxt


def plot_confusion_matrix(con_matx,
                          normalize=False,
                          title='Confusion matrix', removeNullClass=True,
                          cmap=plt.cm.OrRd):  # Blues,OrRd, YlOrRd
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if removeNullClass:
        con_matx = con_matx[1:, 1:]  # remove class 0 - do nothing
        classes = np.arange(1, len(con_matx[0]) + 1)
    else:
        classes = np.arange(0, len(con_matx[0]) + 1)

    # plt.figure(figsize=(12, 12))

    plt.imshow(con_matx, interpolation='nearest', cmap=cmap)

    if normalize:
        updated_title = title + ' Identification (normalized)'
    else:
        updated_title = title + ' Identification (non normalized)'

    plt.title(updated_title)
    plt.colorbar()

    tick_marks = np.arange(len(con_matx[0]))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        con_matx = con_matx.astype('float') / con_matx.sum(axis=1)[:, np.newaxis] * 100.0
        for x in range(0, len(con_matx[0, :])):
            xv = con_matx[x, :]
            for y in range(0, len(xv)):
                vv = xv[y]

                con_matx[x, y] = int(np.round(vv * 10.0)) / 10.0

    thresh = con_matx.max() / 2.
    for i, j in itertools.product(range(con_matx.shape[0]), range(con_matx.shape[1])):
        plt.text(j, i, con_matx[i, j],
                 horizontalalignment="center",
                 color="white" if con_matx[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.1)

    # plt.show()
    os.makedirs(os.path.dirname(ml_utils.get_dir_path()), exist_ok=True)
    plt.savefig(ml_utils.get_dir_path() + title + '_confusion_matrix.png')
    plt.clf()


def plot_history(history, types):
    # summarize history for accuracy
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.xlim([0, max(history.epoch)])
    plt.legend(['train', 'test'], loc='upper left')
    os.makedirs(os.path.dirname(ml_utils.get_dir_path()), exist_ok=True)
    plt.savefig(ml_utils.get_dir_path() + types + '_accuracy.png')
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.clf()

    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.xlim([0, max(history.epoch)])
    plt.legend(['train', 'test'], loc='upper left')
    os.makedirs(os.path.dirname(ml_utils.get_dir_path()), exist_ok=True)
    plt.savefig(ml_utils.get_dir_path() + types + '_loss.png')
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.clf()


def auto_label(rects):
    for rect in rects:
        width = rect.get_width()
        height = rect.get_height()
        xloc = rect.get_x() + width / 4.0
        yloc = 1.02 * height
        plt.text(xloc, yloc, "%0.2f" % float(height), fontsize=8)


def draw_bar_chart(dictionary, title, x_label, y_label):
    bar_chart = plt.bar(range(len(dictionary)), dictionary.values(), align='center',
                        color=cm.OrRd(np.linspace(.4, .8, 10)),
                        zorder=3)
    value_list = list(dictionary.values())
    high = max(value_list)
    plt.ylim([0, high + 10])
    plt.title(title)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    ax = plt.gca()
    ax.grid()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    for tick in ax.xaxis.get_major_ticks() + ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(8)

    plt.tick_params(top=False, bottom=False, left=False, right=False, labelleft=True, labelbottom=True)
    plt.xticks(range(len(dictionary)), list(dictionary.keys()), rotation=90)
    plt.tight_layout()
    # plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.25)
    auto_label(bar_chart)
    plt.savefig(ml_utils.get_dir_path() + title + '.png')
    plt.clf()


def plot_color_separation(data_x, data_y, data_z, color, title, x_label='X', y_label='Y', z_label='Z'):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(data_x, data_y, data_z, c=color, s=50, edgecolors='black', alpha=0.8, marker='s')  # linestyle='dotted',
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)
    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    os.makedirs(os.path.dirname(ml_utils.get_dir_path()), exist_ok=True)
    plt.title(title)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.savefig(ml_utils.get_dir_path() + title + '.png')
    # plt.show()
    plt.clf()


if __name__ == "__main__":
    data = genfromtxt('./resources/color_separation.csv', delimiter=',', skip_header=1, dtype=None,
                      names=['Color', 'H', 'S', 'V', 'X', 'Y', 'Z', 'R', 'G', 'B', 'L', 'A', 'B', 'H_Degree',
                             'S_Degree', 'V_Degree', 'Y', 'Cb', 'Cr'], encoding="utf-8")
    plot_color_separation(data['H'], data['S'], data['V'], data['Color'], 'HSV Color Space', 'H', 'S', 'V')
    plot_color_separation(data['X'], data['Y'], data['Z'], data['Color'], 'XYZ Color Space', 'X', 'Y', 'Z')
    plot_color_separation(data['R'], data['G'], data['B'], data['Color'], 'RGB Color Space', 'R', 'G', 'B')
    plot_color_separation(data['L'], data['A'], data['B'], data['Color'], 'LAB Color Space', 'H', 'S', 'V')
    plot_color_separation(data['H_Degree'], data['S_Degree'], data['V_Degree'], data['Color'], 'HSV Degree Color Space',
                          'H_Degree', 'S_Degree', 'V_Degree')
    plot_color_separation(data['Y'], data['Cb'], data['Cr'], data['Color'], 'YCbCr Color Space', 'Y', 'Cb', 'Cr')
