import time

import deep_learning_classification as dl_clf
import machine_learning_plot_utils as ml_plot_utils
import machine_learning_utils as ml_utils
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier

n_neighbors = 7

(train_container_data, train_container_labels, train_container_labels_raw), (
    train_rack_data, train_rack_labels, train_rack_labels_raw) = ml_utils.get_trainig_data(False, 'raw')
(test_rack_data, test_rack_labels, test_rack_labels_raw), (
    test_container_data, test_container_labels, test_container_labels_raw) = ml_utils.get_testing_data(False, 'raw')

names = ["Nearest Neighbors", "Linear SVM",
         "RBF SVM",
         "Decision Tree", "Random Forest", "Neural Net",
         "Naive Bayes", "QDA", "Logistic Regression"]

classifiers = [
    KNeighborsClassifier(n_neighbors, weights='distance', n_jobs=-1),
    LinearSVC(),
    SVC(gamma=2, C=1),
    DecisionTreeClassifier(),
    RandomForestClassifier(n_jobs=-1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis(),
    LogisticRegression(random_state=0, n_jobs=-1)
]
'''
names = ["Nearest Neighbors", "Linear SVM", 'LinearSVC']

classifiers = [
    KNeighborsClassifier(n_neighbors, weights='distance', n_jobs=-1),
    SVC(kernel="linear", C=0.025),
    LinearSVC(C=0.025)
]
'''
precisions = {}
recalls = {}
f1scores = {}
accuracy_scores = {}
training_time = {}
prediction_time = {}

# iterate over classifiers
for name, clf in zip(names, classifiers):
    clf.fit(train_container_data, train_container_labels_raw)
    # score = clf.score(test_container_data, test_container_labels_raw)

    start_time = time.time()
    clf.fit(train_container_data, train_container_labels_raw)
    elapsed_time = time.time() - start_time
    training_time[name] = elapsed_time

    start_time = time.time()
    test_predicted_container_res = clf.predict(test_container_data)
    elapsed_time = time.time() - start_time
    prediction_time[name] = elapsed_time

    precision, recall, f1score, accuracy = ml_utils.display_result(test_container_labels_raw,
                                                                   test_predicted_container_res, name)
    precisions[name] = precision * 100
    recalls[name] = recall * 100
    f1scores[name] = f1score * 100
    accuracy_scores[name] = accuracy * 100

#  ------------------------------------------- Deep learning --------------------------------------------------

model_container = dl_clf.build_model(25)
start_time = time.time()
history_container = model_container.fit(train_container_data, train_container_labels, epochs=20,
                                        validation_data=(test_container_data, test_container_labels),
                                        batch_size=1000, verbose=2)
elapsed_time = time.time() - start_time
training_time['Deep Learning'] = elapsed_time

start_time = time.time()
test_predicted_container_res = model_container.predict(test_container_data, batch_size=1).argmax(axis=-1)
elapsed_time = time.time() - start_time
prediction_time['Deep Learning'] = elapsed_time

precision, recall, f1score, accuracy = ml_utils.display_result(test_container_labels_raw,
                                                               test_predicted_container_res, 'Deep Learning')
precisions['Deep Learning'] = precision * 100
recalls['Deep Learning'] = recall * 100
f1scores['Deep Learning'] = f1score * 100
accuracy_scores['Deep Learning'] = accuracy * 100

#  --------------------------------------------------------------------------------------------------------------

print(accuracy_scores)

# print(training_time)
# print(prediction_time)
# plt.show()

ml_plot_utils.draw_bar_chart(precisions, 'Precision', 'Classification Algorithms', 'Precision % ')
ml_plot_utils.draw_bar_chart(recalls, 'Recall', 'Classification Algorithms', 'Recall %')
ml_plot_utils.draw_bar_chart(f1scores, 'F1 Score', 'Classification Algorithms', 'F1 Score %')
ml_plot_utils.draw_bar_chart(accuracy_scores, 'Accuracy', 'Classification Algorithms', 'Accuracy %')
ml_plot_utils.draw_bar_chart(training_time, 'Training time', 'Classification Algorithms', 'Training time (seconds)')
ml_plot_utils.draw_bar_chart(prediction_time, 'Prediction time', 'Classification Algorithms',
                             'Prediction time (seconds)')
