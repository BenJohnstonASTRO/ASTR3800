import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import h5py
from glob import glob
from astropy.modeling import models, fitting
from scipy import optimize
from scipy import signal
from scipy.optimize import *
import pylab
import scipy

# Getting our files with our images
files = glob('ESPC*fit')       # Finds list of all files in the directory using linux wildcard
files = np.array(files)
files.sort()                   # Sorts list of files
# Writing a function that will find the center of the star using a weighted average
def centroid(image):
    vertical_profile = np.sum(image, axis=1)
    horizontal_profile = np.sum(image, axis=0)
    y = np.sum(vertical_profile*np.arange(0,vertical_profile.size)) / np.sum(vertical_profile)
    x = np.sum(horizontal_profile*np.arange(0,horizontal_profile.size)) / np.sum(horizontal_profile)
    return int(round(y)),int(round(x))
# Writing a function that will define the aperture and "cut out" the corresponding data within it
def cookiecutter(image,radius,center):
    cutter = np.zeros(image.shape)
    for r in xrange(radius+1):
        for t in np.arange(0,np.pi/2.0+np.pi/100.0,step=np.pi/100.0):
            y = r*np.sin(t)
            x = r*np.cos(t)
            y = int(round(y))
            x = int(round(x))
            cutter[center[0]+y,center[1]+x]=1
            cutter[center[0]+y,center[1]-x]=1
            cutter[center[0]-y,center[1]-x]=1
            cutter[center[0]-y,center[1]+x]=1
    return cutter*image
# Writing a function that will cut a box around some position in an image
def find_star(img, center, width):
    return img[center[0]-width:center[0]+width, center[1]-width:center[1]+width]
# Writing a function that will perform aperture photometry on an image
def apeture_photometry(img, loc, width, radius):
    box = find_star(img, loc, width)
    center = centroid(box)
    cutter = cookiecutter(box, radius, center)
    return np.sum(cutter)
# Running the program for a real dataset
target_star = (596,339)
similar_star = (525,690)
target = []
similar = []
for f in files:
    image = fits.getdata(f)
    target.append(apeture_photometry(image, target_star, 25, 10))
    similar.append(apeture_photometry(image, similar_star, 25, 10))   
# Plotting our first stab at the transit
target = np.array(target)
similar = np.array(similar)
actual = target-similar
m,b = np.polyfit(np.arange(actual.size),actual,1)
# Detrending
y = m*np.arange(actual.size)+b
curve = actual-y
x_data = np.arange(0,336)
y_data = curve
data2 = curve
x2 = np.arange(0,336)

def SIN_WAVE(x, A,a,b,d):
    return A*(np.sin(a*x-b))+d

def SQUARE_WAVE(x, a2,b2,c2,d2):
    return a2*np.round((np.sin(b2*x-(c2))+1)/2)+d2

def SIN_SQUARE_WAVE(x, A,a,b,d, a2,b2,c2,d2):
    return (A*(np.sin(a*x-b))+d) + (a2*np.round((np.sin(b2*x-(c2))+1)/2)+d2)

params_1, extras_1 = curve_fit(SIN_WAVE, x2, y_data, p0=(-7600,0.018,1300,3000))
params_2, extras_2 = curve_fit(SQUARE_WAVE, x2, y_data, p0=(-1.01430459e+04,1.89000000e-02,1.39800000e+02,5.01114768e+03))
params_3, extras_3 = curve_fit(SIN_SQUARE_WAVE, x2, y_data, p0=(-7600,0.018,1300,3000, -1.01430459e+04,1.89000000e-02,1.39800000e+02,5.01114768e+03))

Sin_Fit = SIN_WAVE(x2, params_1[0], params_1[1], params_1[2], params_1[3])
Square_Wave_Fit = SQUARE_WAVE(x2, params_2[0], params_2[1], params_2[2], params_2[3])
Sin_Square_Wave_Fit = SIN_SQUARE_WAVE(x2, params_3[0], params_3[1], params_3[2], params_3[3], params_3[4], params_3[5], params_3[6], params_3[7])

plt.figure(figsize=(18,12))
plt.title('Transit of WASP-12b')
plt.plot(x2, Sin_Fit, 'navy', linewidth=2, label='Sin Wave Fit')
plt.plot(x2, Square_Wave_Fit, 'orange', linewidth=2, label='Square Wave Fit')
plt.plot(x2, Sin_Square_Wave_Fit, 'r-', linewidth=4.5, label='Sin+Square Wave Fit')
plt.plot(x2, data2, 'k--', linewidth=0.5, label='Data')
plt.plot(x2, data2, 'k.', linewidth=0.5)
plt.legend()
plt.savefig('Transit_of_WASP12b_With_Fitted_Model.png', dpi=300)
plt.show()
