# -*- coding: utf-8 -*-
"""IRIS DATASET IN KAGGLE.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IwKcL5IKzcIR4qbTRKj9ke6rRffQ16vM
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.preprocessing import StandardScaler

iris = pd.read_csv('/content/Iris.csv')

iris.head(10)

iris.shape

iris.size

iris.groupby('Species').mean()

iris['Species'].value_counts()

iris.describe()

iris.isnull().sum()

iris.info()

pyplot = iris.plot(kind = 'density', subplots = True, layout = (3,3), sharex = False)

plt.figure(figsize=(10,10))
plt.hist(iris['SepalLengthCm'])
plt.xlabel('SepalLengthCm')
plt.ylabel('Count')
plt.title('SepalLengthCm')
plt.show()

sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm', data=iris)

sns.pairplot(iris, hue='Species')

X = iris.drop(columns=['Species'])
Y = iris['Species']

print(X)

print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()

model.fit(X_train, Y_train)

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('The accuracy Score of the Training Data is : ', training_data_accuracy)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('The accuracy Score of the Test Data is : ', test_data_accuracy)

input_data = (123,7.7,2.8,6.7,2.0)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
input_df = pd.DataFrame(input_data_reshaped, columns=X.columns)
std_data = scaler.transform(input_df)
prediction = model.predict(std_data)
print(prediction)

