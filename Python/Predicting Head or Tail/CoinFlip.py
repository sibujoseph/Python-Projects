# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 11:30:34 2018

@author: sibuj
"""
import os, sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.metrics import classification_report

#Reading Data
PYTHON_PROJECT_PATH=os.environ['PYTHON_PROJECT_PATH']
CoinData = pd.read_csv(PYTHON_PROJECT_PATH+'\Predicting Head or Tail\Coin_Flips.csv')
print(CoinData.head())

#Missing Data Analysis
sns.heatmap(CoinData.isnull(),yticklabels=False,cbar=False,cmap='viridis')

#Plot to seerelationships
sns.pairplot(CoinData)
sns.distplot(CoinData['Coin_Result'])
CoinData.columns

#Training Data & Test Data
X = CoinData[['Thumb_Pressure', 'Ht_Coin_travelled', 'Flips']]
y = CoinData['Coin_Result']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#Applying Linear Regression model to learn by fitting training data 
lm = LinearRegression()
lm.fit(X_train,y_train)
predictions = lm.predict(X_test)
plt.scatter(y_test,predictions)
sns.distplot((y_test-predictions),bins=50)

#Evaluation Metrics 
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))



sns.set_style('whitegrid')
sns.countplot(x='Coin_Result',data=CoinData,palette='RdBu_r')
sns.countplot(x='Coin_Result',hue='Thumb_Pressure',data=CoinData,palette='RdBu_r')
sns.countplot(x='Coin_Result',hue='Ht_Coin_travelled',data=CoinData,palette='RdBu_r')
sns.countplot(x='Coin_Result',hue='Flips',data=CoinData,palette='RdBu_r')

plt.figure(figsize=(12, 7))
sns.boxplot(x='Thumb_Pressure',y='Flips',data=CoinData,palette='winter')
sns.boxplot(x='Thumb_Pressure',y='Ht_Coin_travelled',data=CoinData,palette='winter')
sns.boxplot(x='Ht_Coin_travelled',y='Flips',data=CoinData,palette='winter')
sns.boxplot(x='Coin_Result',y='Flips',data=CoinData,palette='winter')

#No categorical columns in data - so no dummies conversion
#? = pd.get_dummies(CoinData['?'],drop_first=True)

#Applying Logistic Regression
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)

predictions = logmodel.predict(X_test)

#Evaluation Metrics 
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
print(classification_report(y_test,predictions))


#Applying Clusterig Tehnique
kmeans = KMeans(n_clusters=4)
kmeans.fit(CoinData)

kmeans.cluster_centers_
kmeans.labels_

print(X_train[0])

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(10,6))
ax1.set_title('K Means')
ax1.scatter(data[0][:,0],data[0][:,1],c=kmeans.labels_,cmap='rainbow')
ax2.set_title("Original")
ax2.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')





