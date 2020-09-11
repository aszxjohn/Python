#! python3

import os
from PIL import Image
import numpy as np


def turn_right(array):
    global image_array, trial_array

    trial_array = image_array[::-1]
    
    h, w, c = image_array.shape             # 列出陣列維度並回傳給長, 寬, 深度

    h = h -1
    w = w -1
    i, j = h, w


    for i in range(h):
        for j in range(w):
            array[j, i] = trial_array[i, j]

    return array


def turn_left(array):
    global image_array, trial_array


    h, w, c = image_array.shape             # 列出陣列維度並回傳給長, 寬, 深度
    h = h -1
    w = w -1
    i, j = h, w

    for i in range(h):
        for j in range(w):
            array[j, i] = image_array[i, j]

    array = array[::-1]

    return array


def rotate_180_degrees(array):
    global image_array, trial_array


    h, w, c = image_array.shape             # 列出陣列維度並回傳給長, 寬, 深度
    h = h -1
    w = w -1
    i, j = h, w

    for i in range(h):
        for j in range(w):
            array[h-i, w-j] = image_array[i, j]

    return array

def image_show(array):

    array = array.astype(np.uint8)   # 因現在array2的格式不能直接做fromarry，所以先將他轉成uint8
    image_array = Image.fromarray(array)    # image2 is a PIL image
    
    image_array.show()              # 顯示圖片


def main():
    global image, load_file_path, image_array, trial_array

    load_file_path = os.path.dirname(__file__) + "/sample.jpg"
    image = Image.open(load_file_path, mode='r')     # image is a PIL image 

    image_array = np.array(image) # 將讀到的Image轉成numpy的陣列方便運算

    trial_array = np.zeros((image_array.shape[0],image_array.shape[1],image_array.shape[2]))
    horizontal_array = np.zeros((image_array.shape[0], image_array.shape[1], image_array.shape[2])) # 最後成品是橫向的則使用此陣列
    upright_array = np.zeros((image_array.shape[1], image_array.shape[0], image_array.shape[2]))  # 最後成品是直向的需要使用此陣列


    upright_array = turn_right(upright_array)
    image_show(upright_array)

    upright_array = turn_left(upright_array)
    image_show(upright_array)

    horizontal_array = rotate_180_degrees(horizontal_array)
    image_show(horizontal_array)



if __name__ == "__main__":
    main()



