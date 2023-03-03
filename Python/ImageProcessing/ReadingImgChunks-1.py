# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:02:45 2018

@author: sibuj
"""
import os, sys
PYTHON_PROJECT_PATH=os.environ['PYTHON_PROJECT_PATH']
PROJECT_PATH=PYTHON_PROJECT_PATH+"\ImageProcessing\\"
print(PROJECT_PATH)
print(os.getcwd())

import numpy as np
import matplotlib.pyplot as plt
#import Image
from PIL import Image

#Generate sample images
num_images = 3

x=range(0,num_images)
print(x)

for i in range(0,num_images):
    print(i)
    Z = np.random.rand(2000, 2000)
    plt.imsave(PROJECT_PATH+'%02i.png'%i, Z)
    snipZ = Z[200:300, 200:300]
    plt.imsave(PROJECT_PATH+'%02i.snip.png'%i, snipZ)

#load the images
for i in range(0,num_images):
    im = Image.open(PROJECT_PATH+'%02i.snip.png'%i)
    
    #convert them to numpy arrays
    data = np.array(im)
    
print(data)