# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 02:30:25 2018

@author: sibuj
"""

print(__doc__)

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_olivetti_faces

#import ConvertImgToArrays as CiA

# Load the faces datasets
data = fetch_olivetti_faces()
#data=CiA.main()
print(data.keys())
#print("---------data--------------")
#print(data)
print("----------len(data.images)-------------")
print(len(data.images))
print("--------data---------------")
targets = data.target

data = data.images.reshape((len(data.images), -1))
print(data)
print("----------train-------------")
train = data[targets*10]
print(train)
# Test on a subset of people
print("---------len(train)--------------")
print(len(train))
n_faces = 5
print("---------nPixels--------------")
n_pixels = data.shape[1]
print(n_pixels)

# Upper half of the faces
X_train = train[:, :(n_pixels + 1)]
# Lower half of the faces
y_train = train[:, n_pixels:]

print("-----------X_train ------------")
print(X_train)
print("-----------y_train ------------")
print(y_train)

image_shape = (64, 64)

n_cols = 1 #+ len(ESTIMATORS)
#plt.figure(figsize=(2. * n_cols, 2.26 * 5))
plt.figure(figsize=(5, 12))
plt.suptitle("Face completion with multi-output estimators", size=16)

i=1
true_face = np.hstack((X_train[i], y_train[i]))
sub = plt.subplot(5, 1, 2)
print("-------Alive----------------")
sub.axis("off")
sub.imshow(true_face.reshape(image_shape)#,
           #cmap=plt.cm.gray,
           #interpolation="nearest"
           )

plt.show()



"""import matplotlib.pyplot as plt
# plot a line, implicitly creating a subplot(111)
plt.plot([3,2,5,8,4,6])
# now create a subplot which represents the top plot of a grid
# with 2 rows and 1 column. Since this subplot will overlap the
# first, the plot (and its axes) previously created, will be removed
plt.subplot(2,1,1, facecolor='r')
plt.plot(range(12))
plt.subplot(212, facecolor='y') # creates 2nd subplot with yellow background
"""
