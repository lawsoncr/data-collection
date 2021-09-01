# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:21:07 2021

@author: claws
"""

import matplotlib.pyplot as plt
import numpy as np


im = plt.imread('USGS_NED_1_n36w082_IMG.tif')
print(type(im))
print(im.shape)

plt.imshow(im)
plt.show()

def construct_file_name(lat, lon):

    return file_name

def load_trim_image(lat, lon):

    return image
