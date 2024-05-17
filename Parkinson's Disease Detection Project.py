# -*- coding: utf-8 -*-
"""Parkinson's Disease Detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18t5-cBKyqx-tSi6_6Ii028nSJl_f94Rv
"""

from google.colab import drive
drive.mount('/content/drive')
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import tree, svm, linear_model, naive_bayes
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, ConfusionMatrixDisplay
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/CSE422/parkinsons.data')
# df = pd.read_csv('/content/parkinsons.csv')
df.head()

# print(df.shape)
# df.describe()
# df.isnull().sum().sum()
# df.info()

#Checking for missing values in each column
df.isnull().sum()

#correlation
corr = df.corr()
# print(corr)
plt.figure(figsize = (20,10), dpi=130)
sns.heatmap(df.corr(), annot=True)
plt.show()

#distribution of label
# df['status'].value_counts()
df['status'].value_counts().plot(kind='bar', xlabel='status', ylabel='Count', rot=0) # 0 for healthy, 1 for pd
# df['status'].plot(kind = 'hist')
# plt.pie(df.status.value_counts(), labels = [1,0])
# plt.legend()
# plt.title('Outcome Proportionality')
# plt.show()

"""Dataset Preprocessing"""

#separate x(features) and y(label)
X = df.drop(columns=['name','status'], axis=1)
Y = df['status']

#split dataset into train and test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=5)

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

"""Model Training"""

model = tree.DecisionTreeClassifier()
model.fit(X_train, Y_train)

model2 = svm.SVC(kernel='linear')
model2.fit(X_train, Y_train)

model3 = linear_model.LogisticRegression()
model3.fit(X_train, Y_train)

model4 = naive_bayes.BernoulliNB()
model4.fit(X_train, Y_train)

model5 = KNeighborsClassifier()
model5.fit(X_train, Y_train)

"""Model Evaluation"""

# accuracy score on testing data
dt_prediction = model.predict(X_test)
# print(dt_prediction)
dt_accuracy = accuracy_score(Y_test, dt_prediction)*100
print(f'Accuracy score of the Decision Tree Model : {dt_accuracy}%')

print()
svm_prediction = model2.predict(X_test)
svm_accuracy = accuracy_score(Y_test, svm_prediction)*100
print(f'Accuracy score of the SVM : {svm_accuracy}%')

print()
lr_prediction = model3.predict(X_test)
lr_accuracy = accuracy_score(Y_test, lr_prediction)*100
print(f'Accuracy score of the Logistic Regression Model : {lr_accuracy}%')

print()
b_NB_prediction = model4.predict(X_test)
b_NB_accuracy = accuracy_score(Y_test, b_NB_prediction)*100
print(f'Accuracy score of the Bernoulli Naive Bayes Model : {b_NB_accuracy}%')

print()
knn_prediction = model5.predict(X_test)
knn_accuracy=accuracy_score(Y_test, knn_prediction)*100
print(f'Accuracy score of the KNN Model : {knn_accuracy}%')

dt_precision = precision_score(Y_test, dt_prediction)
dt_recall = recall_score(Y_test, dt_prediction)
print(f"Precision score of the Decision Tree Model : {dt_precision}")
print(f"Recall score of the Decision Tree Model : {dt_recall}")

print()
svm_precision = precision_score(Y_test, svm_prediction)
svm_recall = recall_score(Y_test, svm_prediction)
print(f"Precision score of the SVM : {svm_precision}")
print(f"Recall score of the SVM : {svm_recall}")

print()
lr_precision = precision_score(Y_test, lr_prediction)
lr_recall = recall_score(Y_test, lr_prediction)
print(f"Precision score of the Logistic Regression Model : {lr_precision}")
print(f"Recall score of the Logistic Regression Model : {lr_recall}")

print()
b_NB_precision = precision_score(Y_test, b_NB_prediction)
b_NB_recall = recall_score(Y_test, b_NB_prediction)
print(f"Precision score of the Bernoulli Naive Bayes Model : {b_NB_precision}")
print(f"Recall score of the Bernoulli Naive Bayes Model : {b_NB_recall}")

print()
knn_precision = precision_score(Y_test, knn_prediction)
knn_recall = recall_score(Y_test, knn_prediction)
print(f"Precision score of the KNN  Model : {knn_precision}")
print(f"Recall score of the KNN Model : {knn_recall}")

print('Decision Tree')
dt_cm = confusion_matrix(Y_test, dt_prediction)
# print(dt_cm)
cm_display = ConfusionMatrixDisplay(confusion_matrix = dt_cm, display_labels = [False, True])

cm_display.plot()
plt.show()

print()
print('SVM')
svm_cm = confusion_matrix(Y_test, svm_prediction)
cm_display2 = ConfusionMatrixDisplay(confusion_matrix = svm_cm, display_labels = [False, True])

cm_display2.plot()
plt.show()

print()
print('LR')
lr_cm = confusion_matrix(Y_test, lr_prediction)
cm_display3 = ConfusionMatrixDisplay(confusion_matrix = lr_cm, display_labels = [False, True])

cm_display3.plot()
plt.show()

print()
print('Bernoulli_NB')
b_NB_cm = confusion_matrix(Y_test, b_NB_prediction)
cm_display4 = ConfusionMatrixDisplay(confusion_matrix = b_NB_cm, display_labels = [False, True])

cm_display4.plot()
plt.show()

print()
print('KNN')
knn_cm = confusion_matrix(Y_test, knn_prediction)
cm_display5 = ConfusionMatrixDisplay(confusion_matrix = knn_cm, display_labels = [False, True])

cm_display5.plot()
plt.show()

#Accuracy comparison
x = ['Decision Tree', 'SVM', 'LR', 'Bernoulli NB', 'KNN']
y = [dt_accuracy, svm_accuracy, lr_accuracy, b_NB_accuracy, knn_accuracy]
plt.bar(x,y)
plt.show()