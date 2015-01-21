# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 14:38:04 2015

@author: faiz
"""
import numpy as np
import scipy as sci
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.pylab as lab
from skimage.filter import threshold_adaptive

def binarizer(image, block_size, offset):
    image_New = image.copy()
    binarized_image = threshold_adaptive(image_New, block_size, offset)
    return binarized_image
    
    
    
