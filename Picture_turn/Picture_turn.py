#! python3

import os
from PIL import Image
import numpy as np







load_file_path = os.path.dirname(__file__) + "/sample.jpg"
image = Image.open(load_file_path, mode='r')     # image is a PIL image 

array1 = np.array(image)          # array is a numpy array 
array2 = np.zeros((array1.shape[0],array1.shape[1],array1.shape[2])) # 建立一個空的三維陣列使他與原本的一樣大小
array3 = np.zeros((array1.shape)) # 建立一個空的三維陣列使他與原本的一樣大小
array4 = np.zeros((array1.shape[1],array1.shape[0],array1.shape[2])) 
array5 = np.zeros((array1.shape[1],array1.shape[0],array1.shape[2])) 

print(array1.shape)
print(array2.shape)
print(array3.shape)

h, w, c = array1.shape             # 列出陣列維度並回傳給長, 寬, 深度
i, j = h, w
h = h -1
w = w -1

for i in range(h):
    for j in range(w):
        array2[h-i, w-j] = array1[i, j]



array3 = array1[::-1]

for i in range(h):
    for j in range(w):
        array4[j, i] = array3[i, j]


for i in range(h):
    for j in range(w):
        array5[j, i] = array1[i, j]

array5 = array5[::-1]

array2 = array2.astype(np.uint8)   # 因現在array2的格式不能直接做fromarry，所以先將他轉成uint8
image2 = Image.fromarray(array2)    # image2 is a PIL image

array3 = array3.astype(np.uint8)   # 因現在array2的格式不能直接做fromarry，所以先將他轉成uint8
array3 = Image.fromarray(array3)    # image2 is a PIL image

array4 = array4.astype(np.uint8)   # 因現在array2的格式不能直接做fromarry，所以先將他轉成uint8
array4 = Image.fromarray(array4)    # image2 is a PIL image

array5 = array5.astype(np.uint8)   # 因現在array2的格式不能直接做fromarry，所以先將他轉成uint8
array5 = Image.fromarray(array5)    # image2 is a PIL image

image.show()
image2.show()
#array3.show()
array4.show()
array5.show()