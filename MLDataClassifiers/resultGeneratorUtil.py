import ml_utils
from numpy import genfromtxt

"""
This File is used to generate the final confusion matrix.
Please add the  bottom_color,left_color,right_color,Predicted_boxNumber,Actual_boxNumber values in 'result_confusion_matrix'
file and then run the below code.
"""

if __name__ == "__main__":
    csv_path = "./resources/result_confusion_matrix.csv"
    dt = genfromtxt(csv_path, delimiter=',', skip_header=1)
    actual_labels = dt[:, -1]
    predicted_labels = dt[:, -2]

    ml_utils.display_result(actual_labels, predicted_labels, 'Real Time Prediction')
