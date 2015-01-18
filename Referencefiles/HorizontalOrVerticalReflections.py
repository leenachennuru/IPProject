# -*- coding: utf-8 -*-

"""
Created on Fri Oct 17 15:15:56 2014


@author: Leena Suresh, Abhilash Chandran
"""
# A function to obtain horizontal or vertical reflections of an image

def mirror(image, horizontal=True, vertical=False):
    
    #Importing Numpy and Scipy modules
    import numpy as npy
    from scipy import misc as msc
    import os.path as osp
    
    #Exception Handling to check if the input is an image
    while True:
        try: 
            img = msc.imread(image)
            fileName = osp.basename(image)
            fileDir = osp.dirname(image)
        except: 
            print "That is not an image file. Please try again with an image"
            break
        
        #Size of the image    
        nRow, nCol = img.shape[0], img.shape[1]
        
        #Reflections for a point or a pixel sized image        
        if len(img.shape) == 1:
            print "The horizontal and the vertical reflections of a point (Single Pixel) sized image coincide with the original image"
            msc.imsave("%s/Horizontal reflection of %s" %(fileDir,fileName),img)
            msc.imsave("%s/Vertical reflection of %s" %(fileDir,fileName) ,img)
            break
        
        #initializing the matrix representing the output image
        imHrzRt = imVert = npy.zeros(img.shape)
            
        #Horizontal Reflection of an image    
        if horizontal:
            for col in range(nCol):
                imHrzRt[:,col] = img[:,nCol-col-1]
            msc.imsave("%s/Horizontal reflection of %s" %(fileDir,fileName) ,imHrzRt)
        
        #Vertical Reflection of an image
        if vertical:        
            for row in range(nRow):
                imVert[row,:] = img[nRow-row-1,:]
            msc.imsave("%s/Vertical reflection of %s" %(fileDir,fileName) ,imVert)
            
        break
        
    return None;




