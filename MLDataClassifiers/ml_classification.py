import time

import dl_classification as dl_clf
import ml_plots_utils
import ml_utils
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier

"""
The following file used to compare or analyze multiple ML algorithm and out machine learning model.
"""

n_neighbors = 7

source_dir_path = ml_utils.get_source_dir_path()

train_left_data, train_left_labels_raw, train_left_labels = ml_utils.parse_file(
    source_dir_path + 'train_left.csv', start_column=7, end_column=13)
test_left_data, test_left_labels_raw, test_left_labels = ml_utils.parse_file(
    source_dir_path + 'test_left.csv', start_column=7, end_column=13)

left_preprocessor = StandardScaler()
left_preprocessor.fit(train_left_data)
train_left_data = left_preprocessor.transform(train_left_data)
test_left_data = left_preprocessor.transform(test_left_data)

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

precisions = {}
recalls = {}
f1scores = {}
accuracy_scores = {}
training_time = {}
prediction_time = {}

# iterate over classifiers
for name, clf in zip(names, classifiers):
    clf.fit(train_left_data, train_left_labels_raw)
    # score = clf.score(test_container_data, test_container_labels_raw)

    start_time = time.time()
    clf.fit(train_left_data, train_left_labels_raw)
    elapsed_time = time.time() - start_time
    training_time[name] = elapsed_time

    start_time = time.time()
    test_predicted_left_res = clf.predict(test_left_data)
    elapsed_time = time.time() - start_time
    prediction_time[name] = elapsed_time

    precision, recall, f1score, accuracy = ml_utils.display_result(test_left_labels_raw,
                                                                   test_predicted_left_res, name)
    precisions[name] = precision * 100
    recalls[name] = recall * 100
    f1scores[name] = f1score * 100
    accuracy_scores[name] = accuracy * 100

#  ------------------------------------------- Deep learning --------------------------------------------------


model_left = dl_clf.build_model(7, 6)

start_time = time.time()
history_left = model_left.fit(train_left_data, train_left_labels, epochs=10,
                              validation_data=(test_left_data, test_left_labels), batch_size=500, verbose=2)
elapsed_time = time.time() - start_time
training_time['Deep Learning'] = elapsed_time

start_time = time.time()
test_predicted_left_res = model_left.predict(test_left_data)
elapsed_time = time.time() - start_time
prediction_time['Deep Learning'] = elapsed_time

precision, recall, f1score, accuracy = ml_utils.display_result(test_left_labels_raw,
                                                               test_predicted_left_res.argmax(axis=-1), 'Deep Learning')
precisions['Deep Learning'] = precision * 100
recalls['Deep Learning'] = recall * 100
f1scores['Deep Learning'] = f1score * 100
accuracy_scores['Deep Learning'] = accuracy * 100

#  --------------------------------------------------------------------------------------------------------------

print(accuracy_scores)

# print(training_time)
# print(prediction_time)
# plt.show()

ml_plots_utils.draw_bar_chart(precisions, 'Precision', 'Classification Algorithms', 'Precision % ')
ml_plots_utils.draw_bar_chart(recalls, 'Recall', 'Classification Algorithms', 'Recall %')
ml_plots_utils.draw_bar_chart(f1scores, 'F1 Score', 'Classification Algorithms', 'F1 Score %')
ml_plots_utils.draw_bar_chart(accuracy_scores, 'Accuracy', 'Classification Algorithms', 'Accuracy %')
ml_plots_utils.draw_bar_chart(training_time, 'Training time', 'Classification Algorithms', 'Training time (seconds)')
ml_plots_utils.draw_bar_chart(prediction_time, 'Prediction time', 'Classification Algorithms',
                              'Prediction time (seconds)')
