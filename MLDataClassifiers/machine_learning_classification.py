import time

import machine_learning_utils as machine_learning_utils
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

n_neighbors = 7

(train_container_data, train_container_labels, train_container_labels_raw), (
    train_rack_data, train_rack_labels, train_rack_labels_raw) = machine_learning_utils.get_trainig_data()
(test_rack_data, test_rack_labels, test_rack_labels_raw), (
    test_container_data, test_container_labels, test_container_labels_raw) = machine_learning_utils.get_testing_data()

'''
# we create an instance of Neighbours Classifier and fit the data.
#clf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance', n_jobs=-1)  # Accuracy = 81.07396275524432%
#clf = svm.SVC(kernel='linear')  # Accuracy = 82.15846063272704%
#clf = svm.LinearSVC()  # Accuracy = 79.05059957239799%
#clf = LogisticRegression( random_state=0)  # Accuracy = 79.52468007312615%
#clf = tree.DecisionTreeClassifier()  # Accuracy = 81.0987512781582%
#clf = MLPClassifier()  # Accuracy = 82.43113438477985%
#clf = RandomForestClassifier(n_jobs=-1)  # Accuracy = 84.609425835838%

clf.fit(train_container_data, train_container_labels_raw)
start_time = time.time()
test_predicted_container_res = clf.predict(test_container_data)
elapsed_time = time.time() - start_time
print('\n****************RandomForestClassifier Classification result for container************************')
print('RandomForestClassifier Training time: {}'.format(elapsed_time))
machine_learning_utils.display_result(test_container_labels_raw, test_predicted_container_res,
                                      'RandomForestClassifier_container')

'''
'''
names = ["Nearest Neighbors", "Linear SVM",
         # "RBF SVM",
         "Decision Tree", "Random Forest", "Neural Net",
         "Naive Bayes", "QDA", "LinearSVC"]

classifiers = [
    KNeighborsClassifier(n_neighbors, weights='distance', n_jobs=-1),
    SVC(kernel="linear", C=0.025),
    #SVC(gamma=2, C=1),
    #GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(),
    RandomForestClassifier(n_jobs=-1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis(), LinearSVC()]
'''
names = ["Nearest Neighbors", "Linear SVM"]

classifiers = [
    KNeighborsClassifier(n_neighbors, weights='distance', n_jobs=-1),
    SVC(kernel="linear", C=0.025),
]

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

    precision, recall, f1score, accuracy = machine_learning_utils.display_result(test_container_labels_raw,
                                                                                 test_predicted_container_res, name)
    precisions[name] = precision * 100
    recalls[name] = recall * 100
    f1scores[name] = f1score * 100
    accuracy_scores[name] = accuracy * 100

print(accuracy_scores)


# print(training_time)
# print(prediction_time)
# plt.show()


def auto_label(rects):
    for rect in rects:
        width = rect.get_width()
        height = rect.get_height()
        xloc = rect.get_x() + width / 4.0
        yloc = 1.02 * height
        plt.text(xloc, yloc, "%0.2f" % float(height), fontsize=6)


def draw_bar_chart(dictionary, file_name):
    bar_chart = plt.bar(range(len(dictionary)), dictionary.values(), align='center', color=plt.cm.OrRd, zorder=3)
    value_list = list(dictionary.values())
    high = max(value_list)
    plt.ylim([0, high + 10])
    ax = plt.gca()
    ax.grid()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    for tick in ax.xaxis.get_major_ticks() + ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(6)
    plt.tick_params(top=False, bottom=False, left=False, right=False, labelleft=True, labelbottom=True)
    plt.xticks(range(len(dictionary)), list(dictionary.keys()), rotation=90)
    plt.tight_layout()
    plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.2)
    auto_label(bar_chart)
    plt.savefig(machine_learning_utils.get_dir_path() + file_name)
    plt.clf()


draw_bar_chart(precisions, 'precision.png')
draw_bar_chart(recalls, 'recall.png')
draw_bar_chart(f1scores, 'f1score.png')
draw_bar_chart(accuracy_scores, 'accuracy.png')
draw_bar_chart(training_time, 'training_time.png')
draw_bar_chart(prediction_time, 'prediction_time.png')
