#! python3
from PIL import Image
import numpy as np


image = Image.open('C:\Workspace\Python\RGB _to_Gray\sample.jpg', mode='r')     # image is a PIL image 

array = np.array(image)          # array is a numpy array 
L, W, H= array.shape             #列出陣列維度並回傳給長, 寬, 深度



for L in range(L):
    for W in range(W): #BGR
        array[L, W] = array[L, W] * [0.114, 0.299, 0.587]
       


image2 = Image.fromarray(array)    # image2 is a PIL image


image2.show()
