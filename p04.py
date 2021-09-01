# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:21:07 2021

@author: Connor Lawson
"""

import matplotlib.pyplot as plt
import numpy as np


im = plt.imread('USGS_NED_1_n36w082_IMG.tif')
print(type(im))
print(im.shape)

plt.imshow(im)
plt.show()

def construct_file_name(lat, lon):
    img1 = 'USGS_NED_1_n' + str(abs(lat)) + 'e' + str(abs(lon)) + '_IMG.tif'
    img2 = 'USGS_NED_1_n' + str(abs(lat)) + 'e0' + str(abs(lon)) + '_IMG.tif'
    img3 = 'USGS_NED_1_n' + str(abs(lat)) + 'w' + str(abs(lon)) + '_IMG.tif'
    img4 = 'USGS_NED_1_n' + str(abs(lat)) + 'w0' + str(abs(lon)) + '_IMG.tif'
    
    if lat > 0 and lon > 0 or lat < 0 and lon > 0:
        if lon >= 99:
            file_name = img1
            return file_name
        else:
            file_name = img2
            return file_name

    if lat > 0 and lon < 0 or lat < 0 and lon < 0:
        if lon >= -99:
            file_name = img4
            return file_name
        else:
            file_name = img3
            return file_name
        
def load_trim_image(lat, lon):
    file_name = construct_file_name(lat, lon)
    img = plt.imread(file_name)
    image = img[6:-6, 6:-6]
    return image

def stitch_four(lat, lon):
    img1 = load_trim_image(lat, lon)
    img2 = load_trim_image(lat, lon + 1)
    img3 = load_trim_image(lat - 1, lon)
    img4 = load_trim_image(lat - 1, lon + 1)
    image = np.concatenate([np.concatenate([img1, img3, img2, img4])], axis=1)
    return image

def get_row(lat, lon_min, num_tiles):
    x = 0
    image_rows = []
    for x in range(num_tiles):
        image_row = load_trim_image(lat, lon_min + x)
        image_rows.append(image_row)
        image = np.concatenate(image_rows, axis=1)
    return image

def get_tile_grid(lat_max, lon_min, num_lat, num_lon):
    x = 0
    rows = []
    for x in range(num_lat):
        row = get_row(lat_max - x, lon_min, num_lon)
        rows.append(row)
        image = np.concatenate(rows)
    return image

def get_northwest(lat, lon):
    return np.ceil(lat), np.floor(lon)


def get_tile_grid_decimal(northwest, southeast):
    """ Construct the tiled grid of TIF images that contains these
    northwest and southeast decimal coordinates. Each corner
    is a tuple, (lat, lon). """
    return image
