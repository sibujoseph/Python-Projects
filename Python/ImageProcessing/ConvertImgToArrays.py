"""
Accepts an image input
Assess if it is 'A', returns True if so
Also if it is 'A', adds it to the training library of 'A' images (only if it is non-existent)
"""

import os 
from PIL import Image
import numpy as np

def setTrainData():
    # Path where images are stored
    img_folder = os.path.join(os.getcwd(), 'As')
    # Read all .JPG filenames for the images to process 
    # from the given folder
    imageFiles = [os.path.join(img_folder,f) 
            for f in os.listdir(img_folder)
            if '.JPG' in f.upper()]
    return imageFiles


def setTestData():
    # Path where images are stored
    img_folder = os.path.join(os.getcwd(), 'A_Test')
    # Read all .JPG filenames for the images to process 
    # from the given folder
    imageFiles = [os.path.join(img_folder,f) 
            for f in os.listdir(img_folder)
            if '.JPG' in f.upper()]
    return imageFiles


#Func: Create an image from the array 
def createImageFromArray(arr,i):  
    data = arr['img_data'][:-1]
    img = Image.fromarray(data, 'RGB')
    #img.save('alphabet_A_{}.png'.format(i))
    img.save('./images/alphabet_A_%02i.png' % i)
    #print(i)

#Func: Convert image into arrays
def convertImageToArray(filename):  
    d = dict()
    objImage = Image.open(filename)
    w,h = objImage.size
    print(w,h)
    #create a one dim array with ones. All Ones represent a state of 'Truth' or 'Existence'
    arrYstate = np.ones((h,w,3), dtype=int)
    arrImage = np.array(objImage)
    d['train_data'] = np.stack((arrImage, arrYstate))
    d['img_data'] = arrImage 
    d['img_dim'] = [h,w]
    #print(d['data'].shape)
    #print(d['img_data'].shape)
    #print(d['dim'])
    return d

#Func: main
def main():
    np_arrays = map(convertImageToArray, setTrainData())    
    return np_arrays

#Start
if __name__ == '__main__':

    #Declaration
    i=1
    
    #Get the array of images
    arrOfImages=main()
    
    for eachImg in arrOfImages:
        createImageFromArray(eachImg,i)
        i=i+1
        #break;
