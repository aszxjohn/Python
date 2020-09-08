#! python3
from PIL import Image
import numpy as np


image = Image.open('C:\Workspace\Python\RGB _to_Gray\sample.jpg', mode='r')     # image is a PIL image 

array1 = np.array(image)          # array is a numpy array 
array2 = np.zeros((array1.shape)) # 建立一個空的三維陣列使他與原本的一樣大小

l, w, h = array1.shape             # 列出陣列維度並回傳給長, 寬, 深度
i, j, k = l, w, h                  # 因需要做迴圈所以將長, 寬, 深度 都在給i, j, k
  
r, g, b, gr = 0, 0, 0, 0           # 先定義RGB與灰色的參數，在計算中就可以直接使用


for i in range(0, l):
    for j in range(0, w): #BGR
        r = array1[i, j, 0]        # 將R提出
        g = array1[i, j, 1]        # 將G提出
        b = array1[i, j, 2]        # 將B提出
        gr = (r*38 + g*75 + b*15) >> 7      # 著名轉灰公式
        array2[i, j, 0] = gr       # 將GR 數值回傳進RGB的原位
        array2[i, j, 1] = gr
        array2[i, j, 2] = gr

array2 = array2.astype(np.uint8)   # 因現在array2的格式不能直接做fromarry，所以先將他轉成uint8
image2 = Image.fromarray(array2)    # image2 is a PIL image

image2.show()

