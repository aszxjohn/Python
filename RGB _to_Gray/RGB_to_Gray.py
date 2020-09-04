#! python3
from PIL import Image
import numpy as np


image = Image.open('C:\Workspace\Python\RGB _to_Gray\sample.jpg', mode='r')     # image is a PIL image 

array1 = np.array(image)          # array is a numpy array 
array2 = np.array(image)
array3 = np.array(image)
L, W, H= array1.shape             #列出陣列維度並回傳給長, 寬, 深度
X, Y, Z = L, W, H


for X in range(0, L):
    for Y in range(0, W): #BGR
        array1[X, Y] = array1[X, Y] * [0.114, 0.299, 0.587]
        array2[X, Y] = array2[X, Y] * [0.299, 0.587, 0.114]
        array3[X, Y] = array3[X, Y] * [0.587, 0.114, 0.299]

image2 = Image.fromarray(array1)    # image2 is a PIL image
image3 = Image.fromarray(array2)
image4 = Image.fromarray(array3)

image2.show()
image3.show()
image4.show()
