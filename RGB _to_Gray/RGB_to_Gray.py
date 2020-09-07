#! python3
from PIL import Image
import numpy as np


image = Image.open('C:\Workspace\Python\RGB _to_Gray\sample.jpg', mode='r')     # image is a PIL image 

array1 = np.array(image)          # array is a numpy array 
array2 = np.zeros((array1.shape))

l, w, h = array1.shape             #列出陣列維度並回傳給長, 寬, 深度
i, j, k = l, w, h

a, b, c = array2.shape   
r, g, b, gr = 0, 0, 0,0

for i in range(0, l):
    for j in range(0, w): #BGR
        r = array1[i, j, 0]
        g = array1[i, j, 1]
        b = array1[i, j, 2]
        gr = (r*38 + g*75 + b*15) >> 7
        array2[i, j, 0] = gr
        array2[i, j, 1] = gr
        array2[i, j, 2] = gr

array2 = array2.astype(np.uint8)
image2 = Image.fromarray(array2)    # image2 is a PIL image

image2.show()

