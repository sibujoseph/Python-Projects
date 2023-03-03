import cv2
import numpy as np
from matplotlib import pyplot as plt

picpath='C:/Users/sibuj/Pictures/'

img1 = cv2.imread(picpath+'vivbin.jpg',1)      #cv2.IMREAD_UNCHANGED = -1
img2 = img1.copy()
face_template = cv2.imread(picpath+'viv.jpg',1)    #cv2.IMREAD_UNCHANGED = -1
#w, h = face_template.shape[::-1]

#Show the image read
cv2.namedWindow('vivbin image', cv2.WINDOW_NORMAL)
cv2.imshow('vivbin image',img1)
cv2.imshow('viv image',face_template)
k = cv2.waitKey(0) & 0xFF #For 64-bit machine
if k == 27:         # wait for ESC key to exit
    #cv2.destroyWindow('viv image') #use the exact image name to close the window
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    print('saving new image......')
    cv2.imwrite(picpath+'vivbin_new.jpg',img1)
    cv2.destroyAllWindows()

print(w)
print(h)

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for EachMethod in methods:
    img = img2.copy()
    method = eval(EachMethod)

    # Apply template Matching
    MatchResult = cv2.matchTemplate(img, face_template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(MatchResult)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(MatchResult,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(EachMethod)

    plt.show()
