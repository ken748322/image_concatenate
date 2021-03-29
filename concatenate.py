import cv2
import numpy as np
import glob


left_list = [i.split("/")[-1] for i in glob.glob("img_left/*")]
right_list = [i.split("/")[-1] for i in glob.glob("img_right/*")]


for img_name in left_list:
    if img_name in right_list:
        img = cv2.imread("img_left/" + img_name)
        img2 = cv2.imread("img_right/" + img_name)
        img_c = np.concatenate([img, img2], 1)

        cv2.imwrite("out/" + img_name, img_c)