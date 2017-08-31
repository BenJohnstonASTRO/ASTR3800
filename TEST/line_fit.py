import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
from scipy import optimize
from scipy.optimize import *
import scipy

def LINE(x, m,b):
    return np.exp((((m*x)+b)))

x = np.arange(0,11)
y = np.random.normal(size=len(x)) + LINE(x,10,12)

params_1, extras_1 = curve_fit(LINE, x, y, p0=(10,12))
Line_Fit = LINE(x, params_1[0], params_1[1])

plt.figure(figsize=(18,12))
plt.title('Line Fit Test')
plt.plot(x, Line_Fit, 'navy', linewidth=2, label='Line Fit')
plt.plot(x, y, 'k--', linewidth=0.5, label='Data')
plt.plot(x, y, 'k.', linewidth=0.5)
plt.legend()
# plt.savefig('Line_Fit_Test.png', dpi=300)
plt.show()