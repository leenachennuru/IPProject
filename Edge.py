# -*- coding: utf-8 -*-

"""
Created on Sat Nov 29 21:39:10 2014

@author: Leena Chennuru Vankadara, Abhilash Chandran, Mansoure Ziaei
"""

#Importing the modules
import numpy as np
from scipy import ndimage as nd
from scipy import misc as msc
import time

image = msc.lena()  #Reading the image
shp = image.shape   #Shape of the array of the image

#Robert Operator without using a convolution function
def robert(image):
    rob_mag = image.copy()
    rob_dir = image.copy()
    for i in range(shp[0]):
        for j in range(shp[1]):
            #Computing the gradient
            rob_mag[i,j] = np.sqrt(np.square(image[i,j-1] - image[i-1,j]) + np.square(image[i,j] - image[i-1,j-1]))
            if (float(image[i,j-1] - image[i-1,j])) == 0:
                rob_dir[i,j] = np.pi/float(2)
            else:
                rob_dir[i,j] = np.arctan(float(image[i,j] - image[i-1,j-1])/float(image[i,j-1] - image[i-1,j]))
    return rob_mag, rob_dir

#Robert Operator using the convolve method 
def robertker(image):
    rob = image.copy()
    #Robert Convolution mask in x direction
    rob_kerx = np.array([[0,-1,0],[1,0,0],[0,0,0]])
    #Robert Convolution mask in Y direction
    rob_kery = np.array([[-1,0,0],[0,1,0],[0,0,0]])
    #Convolving with x and y direction masks
    robx = nd.convolve(rob,rob_kerx)
    roby = nd.convolve(rob,rob_kery)
    #Magnitude
    rob_mag = np.sqrt(np.square(robx) + np.square(roby))
    #Direction
    rob_dir = np.arctan(np.divide(robx.astype(float),roby.astype(float)))
    #Handling division by zero
    nans = np.isnan(rob_dir)
    rob_dir[nans] = np.pi/float(2)
    return rob_mag, rob_dir
           

#Sobel Operator without a built in convolve operator

def sobel(image): 
    sobel_mag = image.copy()
    sobel_dir = image.copy()
    for i in range(shp[0] - 1):
        for j in range(shp[1] - 1):
            sobel_mag[i,j] = np.sqrt(np.square(image[i+1,j+1] + 2*image[i,j+1] + image[i-1,j+1] - image[i+1,j-1] - 2*image[i,j-1] - image[i-1,j-1]) + np.square(image[i+1,j+1] + 2*image[i+1,j] + image[i+1,j-1] - image[i-1,j-1] - 2*image[i-1,j] - image[i-1,j+1]))
            if (float(image[i+1,j+1] + 2*image[i,j+1] + image[i-1,j+1] - image[i+1,j-1] - 2*image[i,j-1] - image[i-1,j-1]) == 0):
                sobel_dir[i,j]  = np.pi/float(2)
            else:
                sobel_dir[i,j] = np.arctan(float(image[i+1,j+1] + 2*image[i+1,j] + image[i+1,j-1] - image[i-1,j+1] - 2*image[i-1,j] - image[i-1,j-1])/float(image[i+1,j+1] + 2*image[i,j+1] + image[i-1,j+1] - image[i+1,j-1] - 2*image[i,j-1] - image[i-1,j-1]))
    sobel_dir = sobel_dir[0:shp[0] - 1,0:shp[1] - 1]
    return sobel_mag,sobel_dir



#Sobel with convolve method
def sobelker(image):
    #Copy of the image
    sob = image.copy()
    #X and Y gradients
    Sob_Kerx = np.matrix([[-1,0,1],[-2,0,2],[-1,0,1]])
    Sob_Kery = np.matrix([[-1,-2,-1],[0,0,0],[1,2,1]])
    #Convolution with X and Y convolution masks
    sobx = nd.convolve(sob,Sob_Kerx)
    soby = nd.convolve(sob,Sob_Kery)
    #Magnitude and the direction computing
    sob_mag = np.sqrt(np.square(sobx) + np.square(soby))
    sob_dir = np.arctan(np.divide(sobx.astype(float),soby.astype(float)))
    #Handling division by zero
    nans = np.isnan(sob_dir)
    sob_dir[nans] = np.pi/float(2)
    return sob_mag,sob_dir


#Laplacian Operator
def Laplacian(image):
    Lap = image.copy()
    for i in range(shp[0] - 1):
        for j in range(shp[1] - 1):
            Lap[i,j] = image[i+1,j] +image[i-1,j] + image[i,j+1] + image[i,j-1] - 4*image[i,j]
    Lap = Lap[0:shp[0] - 1,0:shp[1] - 1]
    return Lap

#Laplacian Operator with the convolve method
def Laplacianker(image):
    im = image.copy()
    #Convolution mask Laplacian
    Lap_ker = np.array([[0,1,0],[1,-4,1],[0,1,0]])
    #Convolving the image with the mask
    lap_conv = nd.convolve(im,Lap_ker)
    return lap_conv
    
#Kirsch Operator

def Kirsch(image):
    kir = image.copy()
    #Creating the convolution masks
    A = [[-5,-5,-5],[3,0,3],[3,3,3]]
    A1 = [[3,-5,-5],[3,0,-5],[3,3,3]]
    #All 8 convolution masks
    Ker_mat = [np.rot90(np.rot90(np.rot90(np.rot90(A)))),np.rot90(np.rot90(np.rot90(np.rot90(A1)))),np.rot90(np.rot90(np.rot90(A))),np.rot90(np.rot90(np.rot90(A1))),np.rot90(np.rot90(A)),np.rot90(np.rot90(A1)),np.rot90(A),np.rot90(A1)]        
    im_mat = {}
    #Convolving the image and storing them in a dictionary
    for i in range(8):
        im_mat[str(i)] = nd.convolve(kir, Ker_mat[i])
    #Getting the values of the dictionary in a list
    kir_val = im_mat.values()
    #Initializing the magnitude 
    kir_mag = kir_val[0]
    kir_mag_index = np.zeros(shp)
    #Computing the maximum
    for i in range(8):
        kir_mag_copy = kir_mag
        kir_mag = np.maximum(kir_mag,kir_val[i])
        kir_mag_index = np.maximum(np.abs(kir_mag_index), np.ceil(np.abs((kir_mag_copy - kir_mag)/np.max(np.abs(kir_mag_copy - kir_mag)))) * i)
        #Computing the direction matrix
        kir_dir = np.mod((np.pi*np.ones(shp)/2 + (kir_mag_index)*(np.pi/4)),(np.pi*2))
    return kir_mag, kir_dir


rob_mag, rob_dir = robertker(image)
#
start_time = time.time()
kir_mag, kir_dir = Kirsch(image)
end_time = time.time()
#        
sob_mag, sob_ker = sobelker(image) 
msc.imsave('sobkir.png',sob_mag-kir_mag)
#
lap_conv = Laplacianker(image)
#
rob_mag = rob_mag/float(np.max(rob_mag))
msc.imsave('robertmag.png',rob_mag)
#
kir_mag = kir_mag/float(np.max(kir_mag))
msc.imsave('kirschmag.png',kir_mag)
#
sob_mag = sob_mag/float(np.max(sob_mag))
msc.imsave('sobelmag.png',(sob_mag))
#
lap_conv = lap_conv/float(np.max(lap_conv))
msc.imsave('laplacianmag.png',(lap_conv)/np.max(lap_conv))


'''
Laplacian doesn't seem to show any differences between the strong and the weak edges.
So, its not a good idea to be used for segmentation of this image. 

Roberts operator seems to be able to differentiate the edges in the 
diagonal gradients(edges not vertical or horizontal) perfectly well but its ineffective when it comes to 
infact it detects the edges much better if the gradient direction is 
closer to 45

Plot all the values that are closer to 1 abs(angle) 

'''

msc.imsave('robdir.png',np.abs(rob_dir)/np.max(rob_dir))

rob_indices = np.logical_and(np.abs(rob_dir) > 0.5, np.abs(rob_dir) < 1.2)

rob_mag_45 = rob_mag.copy()
not_indices = np.logical_not(rob_indices)
rob_mag_45[(rob_indices)] = 0
msc.imsave('rob45.png',rob_mag_45)
msc.imsave('lena.png',image)

'''-------------------- Analysis of operator effect on lena -------------------------

Robert's operator clearly shows high gradient when the edges are diagonally oriented.
The direction showed in the direction matrix shows the edge direction rotated by 45
So plotting the values between 45 + 45 = 90 and 45 - 45 = 0 (near 0 and pi/2)
We can see that the strongest edges appear in this region. 
Also, the high frequency information is not effectively supressed in Robert's 
Operator. 


Laplacian amplifies the noise to a great extent and hence can not be used for 
effective segmentation. Usage of techniques like thresholding to seperate out
the edges for segmentation can not be useful

Both sobel and Kirsch operators seem to be producing very similar effect on lena.
They differentiate the weak and the strong edges considerably better than robert
or laplacian but none of them eliminate the noise or even highlight he disparity
between the strong and the weak edges to the extent that we can use thresholding
to eliminate the weak edges completely. However among the 4 operators used here
they both seem to fare better than the rest

'''

