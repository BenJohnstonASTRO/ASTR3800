import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import h5py
from glob import glob
from astropy.modeling import models, fitting
from scipy import optimize
from scipy.optimize import *

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


def Gaussian(x):
    return (x*336+x*335+x*334+x*333+x*332+x*331+x*330-+x*329+x*328+x*327+x*326+x*325+x*324+x)

def Gaussian2(lamb_array1, I_01,sigma1,lamb_01,I_C1):
    return ((I_01/(sigma1*(np.sqrt(2.0*np.pi))))*np.exp((-(lamb_array1-lamb_01)**2)/(2.0*sigma1**2))+I_C1)

x2 = np.arange(0,336)
def f(x, amp1,cen1,ht1, amp2,cen2,ht2, a):
    return (amp1*((-x-cen1)**2)+ht1) + (amp2*((-x-cen2)**2)+ht2) + (a)

params_1, extras_1 = curve_fit(Gaussian, x2, y_data)
# params_1, extras_1 = curve_fit(Gaussian2, x2, y_data, p0=(150,105,150,5))
fit = Gaussian(x2)
# fit = Gaussian2(x2, params_1[0], params_1[1], params_1[2], params_1[3])
# chi_square = np.sum((((y_data-fit)**2)/(fit**2)))
# nu = len(fit) - 3
# normalized_chi_square = chi_square/nu
# print normalized_chi_square

plt.figure()
# plt.plot(y_data, 'k.')
plt.plot(fit, 'r-')
plt.plot(data2, 'b--')
plt.show()