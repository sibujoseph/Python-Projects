# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 13:53:11 2018

@author: sibuj
"""

import numpy as np    
arrays = np.array([[[255,255,255],[255,255,255],[255,255,255]],
          [[255,255,0],[255,255,0],[255,255,0]],
          [[255,255,0],[255,255,0],[255,255,0]]])
print(arrays.shape)
print('------------------------------------')
#arr_Y_state = np.array(([1,1,1],[1,1,1],[1,1,1]), dtype=int)
arr_Y_state = np.ones((3,3,3), dtype=int)
#print(arr_Y_state)
print(arr_Y_state.shape)
x=np.stack((arrays, arr_Y_state))
print('------------------------------------')
print(x.shape)
print('------------------------------------')
print(x)
print('------------------------------------')
                                                                                                                print(x[:-1])
#x=Image.fromarray(arrays, 'RGB')
#x.save('./images/x.png')
#print(sum(x))