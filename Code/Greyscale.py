# -*- coding: utf-8 -*-
"""
Spyder Editor

This file iterates over a given folder --> srcdir and converts all the images(.png) into its corresponding greyscale images..
"""

import numpy as npy
from scipy import misc as msc 
import os as os
from PIL import Image

srcdir = 'D:\Google Drive\Intelligent Adaptive Systems\Image Processing\chara'
graysc(srcdir);

"""
file - is a string containing the current dile name beinf used in the loop.
srcdir - the source directory where to look for image files or other folders.
fullfile - holds the complete path of the image file including the directory being currently iterted over.


As of now this fuction simply creates the greyscale images and saves it in the same location.
"""
def graysc(srcdir):
    for file in os.listdir(srcdir):
        fullfile=os.path.join(srcdir,file);
        if os.path.isdir(fullfile):
            print fullfile;
            graysc(fullfile);
        elif os.path.isfile(fullfile) and not file.startswith('grey'):
            img = Image.open(fullfile).convert('LA');
            tempname = os.path.basename(fullfile);
            img.save('%s//grey_%s.png'%(srcdir,tempname));            