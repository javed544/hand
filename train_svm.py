import numpy as np
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
import cv2
import joblib

digits = datasets.load_digits()
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# x_train, x_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.5, shuffle=False)
x_train, x_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.5, random_state=42)

clf = svm.LinearSVC()
clf.fit(x_train, y_train)
joblib.dump(clf, 'svm_digit_recognizer.pkl')

y_pred = clf.predict(x_test)
print(f"Classification report:\n{metrics.classification_report(y_test, y_pred)}")

accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("Confusion matrix:\n", metrics.confusion_matrix(y_test, y_pred))
