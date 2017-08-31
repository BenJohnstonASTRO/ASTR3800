from astropy.io import fits
from numpy import sqrt, pi, exp, linspace, loadtxt
from lmfit.models import GaussianModel
import matplotlib.pyplot as plt
import numpy as np 


data = fits.getdata('quasar.fits')
flux = data['flux']                      
waves = 10**data['loglam'] 
wavelengths = waves[np.logical_and(waves>5000, waves<5250)]
fluxes = flux[np.logical_and(waves>5000, waves<5250)]

def Gaussian(lamb_array, I_0, sigma, lamb_0, I_C):
    return (I_0/(sigma*(np.sqrt(2.0*np.pi)))) * np.exp((-(lamb_array-lamb_0)**2)/(2.0*sigma**2)) + I_C 
     


mod = GaussianModel()

pars = mod.guess(fluxes, x=wavelengths)
out  = mod.fit(fluxes, pars, x=wavelengths)
print (out.fit_report(min_correl=0.25))

plt.plot(wavelengths, fluxes, 'bo')
plt.plot(wavelengths, Gaussian(wavelengths, 264.131234, 35, 5114.52965, 5.3057085416), 'r-')
plt.show()