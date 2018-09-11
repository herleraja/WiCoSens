import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets,neighbors,svm, tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression

import main_rack_container as main_rack_container

n_neighbors = 7

(train_container_data, train_container_labels, train_container_labels_raw), (
    train_rack_data, train_rack_labels, train_rack_labels_raw) = main_rack_container.get_trainig_data()
(test_rack_data, test_rack_labels, test_rack_labels_raw), (
    test_container_data, test_container_labels, test_container_labels_raw) = main_rack_container.get_testing_data()

# Pre Processing

# we create an instance of Neighbours Classifier and fit the data.
#clf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance', n_jobs=-1) #Accuracy = 83.33%
#clf = svm.SVC(kernel='linear') #Accuracy = 86.66%
#clf = svm.LinearSVC() #Accuracy = 76.66%
#clf = LogisticRegression(n_jobs=-1, random_state=0) #Accuracy = 73.33%
#clf = tree.DecisionTreeClassifier() #Accuracy = 76.66%
#clf = MLPClassifier() #Accuracy = 76.66%
clf = RandomForestClassifier(n_jobs=-1)  # Accuracy = 86.66%

clf.fit(train_container_data, train_container_labels_raw)

# predict class using data and kNN classifier
# predString = [[6.2,3.4,5.4,2.3], [5.9,3,5.1,1.8]]

test_predicted_container_res = clf.predict(test_container_data)

main_rack_container.display_result(test_container_labels_raw, test_predicted_container_res, 'container')