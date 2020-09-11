
import os

import cv2
import numpy as np



def main():

    load_file_path = os.path.dirname(__file__) + "/image_test.jpg"
    save_file_path = os.path.dirname(__file__) + "/saved_image.jpg"

    print("The loaded file is located in {}".format(load_file_path))
    load_image = cv2.imread(load_file_path, cv2.IMREAD_UNCHANGED)
    load_image_shape = load_image.shape
    load_image_height = load_image_shape[0]
    load_image_width = load_image_shape[1]
    load_image_channel = load_image_shape[2]
    print("Load Image: Shape = {}, Width = {}, Height = {}, Channel = {}".format(load_image_shape, load_image_width, load_image_height, load_image_channel))

    save_image_shape = (load_image_shape[0], load_image_shape[1], 1)  # 1 channel image of the same width x height
    print("Save Image: Shape = {}".format(save_image_shape))
    save_image = np.zeros(save_image_shape)

    for i in range(load_image_height):
        for j in range(load_image_width):
            save_image[i, j, 0] = load_image[i, j, 1]       # only use the Green channel

    cv2.imwrite(save_file_path, save_image)
    
if __name__ == "__main__":
    main()