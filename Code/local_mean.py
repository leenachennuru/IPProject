# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 20:30:17 2015

@author: faiz
"""
import numpy as np
import scipy as sci
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.pylab as lab

def local_mean(image, box_size =10):
    zone_mean = np.zeros((6,6))
    for i in range(0,6):
        for j in range(0,6):
            sliceNew = image[i*10:(i+1)*10,j*10:(j+1)*10]
            zone_mean[i, j] = np.mean(sliceNew)
    return zone_mean