import time

import machine_learning_utils as machine_learning_utils
from sklearn import neighbors, svm, tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

n_neighbors = 7

(train_container_data, train_container_labels, train_container_labels_raw), (
    train_rack_data, train_rack_labels, train_rack_labels_raw) = machine_learning_utils.get_trainig_data()
(test_rack_data, test_rack_labels, test_rack_labels_raw), (
    test_container_data, test_container_labels, test_container_labels_raw) = machine_learning_utils.get_testing_data()

# we create an instance of Neighbours Classifier and fit the data.
#clf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance', n_jobs=-1)  # Accuracy = 83.33%
#clf = svm.SVC(kernel='linear')  # Accuracy = 86.66%
#clf = svm.LinearSVC()  # Accuracy = 76.66%
#clf = LogisticRegression(n_jobs=-1, random_state=0)  # Accuracy = 73.33%
#clf = tree.DecisionTreeClassifier()  # Accuracy = 76.66%
#clf = MLPClassifier()  # Accuracy = 76.66%
clf = RandomForestClassifier(n_jobs=-1)  # Accuracy = 86.66%

clf.fit(train_container_data, train_container_labels_raw)
start_time = time.time()
test_predicted_container_res = clf.predict(test_container_data)
elapsed_time = time.time() - start_time
print('\n****************RandomForestClassifier Classification result for container************************')
print('RandomForestClassifier Training time: {}'.format(elapsed_time))
machine_learning_utils.display_result(test_container_labels_raw, test_predicted_container_res,
                                      'RandomForestClassifier_container')
