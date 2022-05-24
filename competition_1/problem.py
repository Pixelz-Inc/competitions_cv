# -*- coding: utf-8 -*-
import numpy as np
# import matplotlib.pyplot as plt
import cv2
from input_generator import generate_input
from solution import fix_mask


if __name__ == "__main__":
    shape = (3000, 5000)
    bin_mask, bin_mask_labels, bin_mask_split = generate_input(shape)

    # plt.imshow(bin_mask)
    # plt.show()
    cv2.imwrite("bin_mask.png", bin_mask.astype(np.uint8) * 255)
    cv2.imwrite("bin_mask_split.png", bin_mask_split.astype(np.uint8) * 255)
    cv2.imwrite("bin_mask_labels.png", bin_mask_labels * 40)
    fixed_mask = fix_mask(bin_mask, bin_mask_split)
    cv2.imwrite("fixed_mask.png", fixed_mask.astype(np.uint8) * 255)
