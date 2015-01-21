# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 20:53:02 2015

@author: faiz
"""

import numpy as np
import scipy as sci
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.pylab as lab

def global_mean(image):
    imageNew = image.copy()
    image_mean = np.mean(imageNew)
    return image_mean