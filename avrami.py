import math

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

# """

def function(x, c, a, n):
    return c * (1 - np.exp(-a * np.power(x, n)))


x1 = [21, 38, 59, 76]
x1_scaled = [x/10 for x in x1]
sd1 = [0.0377, 0.0545, 0.0685, 0.098]
data = [0.038, 0.08, 0.126, 0.206]

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

popt, pcov = curve_fit(function, x1_scaled, data, sigma=sd1, bounds=([0, 0, 0], [1, 5., 6.]))
perr = np.sqrt(np.diag(pcov))  # standard deviation error - nie zawsze prawdziwe
print(popt)
print(perr)
print(popt[1]/np.power(10, popt[2]))
a = math.sqrt((perr[1] * perr[1] + math.pow(math.log(10) * perr[2], 2))/ math.pow(10, 2 * popt[2]))
print("a ", popt[1]/np.power(10, popt[2]), " u(a) ", a)

residuals = data - function(x1_scaled, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((data-np.mean(data))**2)
r_squared = 1 - (ss_res / ss_tot)
print("r^2", r_squared)
print(type(popt))
ax[0].plot(x1, [function(x, popt[0], popt[1], popt[2]) for x in x1_scaled], 'g--', label='fit: c=%.3f, a=%.5f, n=%.3f' % (popt[0], popt[1]/np.power(10,popt[2]), popt[2]))
ax[0].errorbar(x1, data, yerr=sd1, fmt='o', label="data")
ax[0].legend()
ax[0].set_xlabel("time (weeks)")
ax[0].set_ylabel("carcinoma probability genotype 0")


xx2 = [42, 47, 57, 59, 63, 66, 80, 81, 88, 90, 91]
xx22 = [x/100 for x in xx2]
data2 = [0.043, 0.089, 0.146, 0.203, 0.26, 0.327, 0.439, 0.551, 0.664, 0.776, 0.888]
sd2 = [0.0425, 0.0601, 0.0788, 0.0919, 0.1014, 0.1123, 0.1387, 0.1496, 0.1484, 0.1348,0.1041]

popt2, pcov2 = curve_fit(function, xx22, data2, sigma=sd2, bounds=([0, 0, 1], [1., 5., 6.]))
perr2 = np.sqrt(np.diag(pcov2))  # standard deviation error - nie zawsze prawdziwe

print(popt2)
print(perr2)
print(1000000000*popt2[1]/np.power(100, popt2[2]))
a = math.sqrt((perr2[1] * perr2[1] + math.pow(math.log(100) * popt2[1] * perr2[2], 2))) / math.pow(100, popt2[2])

print("a ", popt2[1]/np.power(100, popt2[2]), " u(a) ", a)

residuals = data2 - function(xx22, *popt2)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((data2-np.mean(data2))**2)
r_squared = 1 - (ss_res / ss_tot)
print("r^2", r_squared)

ax[1].plot(xx2, [function(x, popt2[0], popt2[1], popt2[2]) for x in xx22], 'g--', label='fit: c=%.3f, a=%.3f*10^-9, n=%.3f' % (popt2[0], 1000000000*popt2[1]/np.power(100, popt2[2]), popt2[2]))
ax[1].errorbar(xx2, data2, yerr=sd2, fmt='o', label="data")
ax[1].legend()
ax[1].set_xlabel("time (weeks)")
ax[1].set_ylabel("carcinoma probability genotype 1")
plt.show()

# """
