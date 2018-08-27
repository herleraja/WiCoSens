import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

n_neighbors = 6

# import some data to play with
iris = datasets.load_iris()

# prepare data
X = iris.data
y = iris.target
class_names = iris.target_names
h = .02

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

print('Total sample size : {}'.format(X.size))
print('Training sample size : {0} \nTesting sample size : {1}'.format(X_train.size, X_test.size))

print('Training Data before pre processing\n {}'.format(X_train))
print('Testing Data before pre processing\n {}'.format(X_test))

# Preprocessing data for the better performence.
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

print('Training Data after pre processing\n {}'.format(X_train))
print('Testing Data after pre processing\n {}'.format(X_test))

# Pre Processing

# we create an instance of Neighbours Classifier and fit the data.
# clf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance', n_jobs=-1) #Accuracy = 83.33%
# clf = svm.SVC(kernel='linear') #Accuracy = 86.66%
# clf = svm.LinearSVC() #Accuracy = 76.66%
# clf = LogisticRegression(n_jobs=-1, random_state=0) #Accuracy = 73.33%
# clf = tree.DecisionTreeClassifier() #Accuracy = 76.66%
# clf = MLPClassifier() #Accuracy = 76.66%
clf = RandomForestClassifier(n_jobs=-1)  # Accuracy = 86.66%

clf.fit(X_train, y_train)

# predict class using data and kNN classifier
# predString = [[6.2,3.4,5.4,2.3], [5.9,3,5.1,1.8]]

prediction = clf.predict(X_test)

print('Predicted Class : {0}'.format(prediction))

print('Total Accuracy : {}'.format(accuracy_score(y_test, prediction) * 100))

print('Classification Report :\n{}'.format(classification_report(y_test, prediction)))

# Compute confusion matrix
cnf_matrix = confusion_matrix(y_test, prediction)
print('Confusion Matrix :\n{}'.format(cnf_matrix))

plt.figure()

plt.imshow(cnf_matrix, cmap=plt.cm.Blues)

plt.colorbar()

tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names, rotation=45)
plt.yticks(tick_marks, class_names)

# To change the text color of the elements printed inside the box
thresh = cnf_matrix.max() / 2.

for i in range(len(cnf_matrix)):
    for j in range(len(cnf_matrix[i])):
        plt.text(j, i, cnf_matrix[i, j], color="white" if cnf_matrix[i, j] > thresh else "black")

plt.title("Confusion Matrix")
plt.ylabel('True label')
plt.xlabel('Predicted label')

plt.tight_layout()
plt.show()
