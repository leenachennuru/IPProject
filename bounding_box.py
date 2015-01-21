# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 14:40:46 2015

@author: macbook
"""

import numpy as np
from scipy import ndimage
from scipy import misc as msc
from skimage.morphology import medial_axis
import matplotlib.pyplot as plt
import matplotlib.mlab as ml

img = msc.lena()

def bounding_box(image):
    min_x, min_y = np.min(image[0], axis=0)
    max_x, max_y = np.max(image[0], axis=0)
    return np.array([(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)])
    
def aspect_ratio(image):
    bbox = bounding_box(image)
    return np.abs(bbox[0,0] - bbox[0,1])/np.abs(bbox[1,0] - bbox[1,1])
    
def area(image):
    bbox = bounding_box(image)
    return np.abs(bbox[0,0] - bbox[0,1])*np.abs(bbox[1,0] - bbox[1,1])

# Compute the medial axis (skeleton) and the distance transform
skel, distance = medial_axis(img, return_distance=True)

# Distance to the background for pixels of the skeleton
dist_on_skel = distance * skel

def pca(image):
    
    


    