import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
from astropy.io import fits
from scipy import optimize
from scipy.optimize import *

# Get Quasar Spectrum data
data = fits.getdata('quasar.fits')
flux = data['flux']                      
waves = 10**data['loglam'] 
err = np.sqrt(data['ivar'])**-1

wavs_1 = waves[np.logical_and(waves>=3574, waves<10350)]
flux_1 = flux[np.logical_and(waves>=3574, waves<10350)]


def Voigt(lamb_array1, I_C, lamb_01, sigma, alpha):
	sigma_g = (sigma/(np.sqrt(2*np.log(2))))
	return ((((1-alpha)*I_C)/(sigma_g*(np.sqrt(2*np.pi))))*np.exp((-(lamb_array1-lamb_01)**2)/(2*(sigma_g**2))))+((alpha*I_C)/np.pi)*(sigma/(((lamb_array1-lamb_01)**2)+sigma**2))

def Gaussian(lamb_array1, I_01,sigma1,lamb_01,I_C1):
    return ((I_01/(sigma1*(np.sqrt(2.0*np.pi))))*np.exp((-(lamb_array1-lamb_01)**2)/(2.0*sigma1**2))+I_C1)

def Quasar_SDSS_J003312(lamb_array1, I_01,sigma1,lamb_01,I_C1, I_02,sigma2,lamb_02,I_C2, I_03,sigma3,lamb_03,I_C3, I_04,sigma4,lamb_04,I_C4, test1,test2,test3,test4, I_05,sigma5,lamb_05,I_C5, I_06,sigma6,lamb_06,I_C6, I_07,sigma7,lamb_07,I_C7, I_08,sigma8,lamb_08,I_C8, I_09,sigma9,lamb_09,I_C9, I_010,sigma10,lamb_010,I_C10, I_011,sigma11,lamb_011,I_C11):
    return ((I_01/(sigma1*(np.sqrt(2.0*np.pi))))*np.exp((-(lamb_array1-lamb_01)**2)/(2.0*sigma1**2))+I_C1) + ((I_02/(sigma2*(np.sqrt(2.0*np.pi))))*np.exp((-(lamb_array1-lamb_02)**2)/(2.0*sigma2**2))+I_C2) + ((I_03/(sigma3*(np.sqrt(2.0*np.pi))))*np.exp((-(lamb_array1-lamb_03)**2)/(2.0*sigma3**2))+I_C3) + ((I_04/(sigma4*(np.sqrt(2.0*np.pi))))*np.exp((-(lamb_array1-lamb_04)**2)/(2.0*sigma4**2))+I_C4) + (Voigt(lamb_array1, test1,test2,test3,test4)) + ((I_05/(sigma5*(np.sqrt(2.0*np.pi))))*np.exp((-(lamb_array1-lamb_05)**2)/(2.0*sigma5**2))+I_C5) + ((I_06/(sigma6*(np.sqrt(2.0*np.pi))))*np.exp((-(lamb_array1-lamb_06)**2)/(2.0*sigma6**2))+I_C6) + ((I_07/(sigma7*(np.sqrt(2.0*np.pi))))*np.exp((-(lamb_array1-lamb_07)**2)/(2.0*sigma7**2))+I_C7) + ((I_08/(sigma8*(np.sqrt(2.0*np.pi))))*np.exp((-(lamb_array1-lamb_08)**2)/(2.0*sigma8**2))+I_C8) + ((I_09/(sigma9*(np.sqrt(2.0*np.pi))))*np.exp((-(lamb_array1-lamb_09)**2)/(2.0*sigma9**2))+I_C9) + ((I_010/(sigma10*(np.sqrt(2.0*np.pi))))*np.exp((-(lamb_array1-lamb_010)**2)/(2.0*sigma10**2))+I_C10) + ((I_011/(sigma11*(np.sqrt(2.0*np.pi))))*np.exp((-(lamb_array1-lamb_011)**2)/(2.0*sigma11**2))+I_C11)


params_1, extras_1 = curve_fit(Quasar_SDSS_J003312, wavs_1, flux_1, p0=(260,35,5110,5, 260,35,4630,5, 290,50,5500,4, 100,40,4400,80, 1,4011.5,20,1300, 260,3700,20,5, 200,50,6299.4,4, 260,35,4600,5, 160,15,9300,2.5, 160,15,9300,5, 250,55,4600,4, 50,10,4000,9))

fit = Quasar_SDSS_J003312(wavs_1, params_1[0], params_1[1], params_1[2], params_1[3], params_1[4], params_1[5], params_1[6], params_1[7], params_1[8], params_1[9], params_1[10], params_1[11], params_1[12], params_1[13], params_1[14], params_1[15], params_1[16], params_1[17], params_1[18], params_1[19], params_1[20], params_1[21], params_1[22], params_1[23], params_1[24], params_1[25], params_1[26], params_1[27], params_1[28], params_1[29], params_1[30], params_1[31], params_1[32], params_1[33], params_1[34], params_1[35], params_1[36], params_1[37], params_1[38], params_1[39], params_1[40], params_1[41], params_1[42], params_1[43], params_1[44], params_1[45], params_1[46], params_1[47])

chi_square = np.sum((((flux[:-4]-fit)**2)/(err[:-4])**2))
nu = len(fit) - 48
normalized_chi_square = chi_square/nu
print normalized_chi_square


plt.figure(figsize=(15,10))
plt.title('Quasar SDSS J003312.80+003434.9 Spectrum Fit')
plt.plot(wavs_1, fit, 'r', linewidth=3.0, label='Fitted model\nnormalized chi square = 1.2')
plt.plot(waves, flux, 'k--', linewidth=0.5, label='Data')
plt.xlabel('Wavelength (Angstroms)')
plt.ylabel('Flux (erg/s/cm^2/Angstrom)')
plt.legend()
plt.savefig('Quasar SDSS J003312.80+003434.9 Spectrum Fit.png', dpi=350)
plt.show()