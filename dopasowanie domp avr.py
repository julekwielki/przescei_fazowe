from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

"""

def func(x, c, a, n):
    return c * (1 - np.exp(-a * np.power(x, n)))


xx1 = [0, 21, 38, 59, 76]
xx12 = [x/10 for x in xx1]
data = [0, 0.038, 0.08, 0.126, 0.206]

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

popt, pcov = curve_fit(func, xx12, data, bounds=([0, 0, 0], [1, 5., 6.]))
perr = np.sqrt(np.diag(pcov))  # standard deviation error - nie zawsze prawdziwe
print(popt)
print(perr)

residuals = data - func(xx12, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((data-np.mean(data))**2)
r_squared = 1 - (ss_res / ss_tot)
print(r_squared)

ax[0].plot(xx12, [func(x, popt[0], popt[1], popt[2]) for x in xx12], 'g--', label='fit: c=%.3f, a=%.3f, n=%.3f' % tuple(popt))
ax[0].scatter(xx12, data, label="data")
ax[0].legend()


xx2 = [0, 42, 47, 57, 59, 63, 66, 80, 81, 88, 90, 91]
xx22 = [x/100 for x in xx2]
data2 = [0, 0.043, 0.089, 0.146, 0.203, 0.26, 0.327, 0.439, 0.551, 0.664, 0.776, 0.888]

popt2, pcov2 = curve_fit(func, xx22, data2, bounds=([0, 1, 1], [1., 5., 6.]))
perr2 = np.sqrt(np.diag(pcov2))  # standard deviation error - nie zawsze prawdziwe
print(popt2)
print(perr2)

residuals = data2 - func(xx22, *popt2)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((data2-np.mean(data2))**2)
r_squared = 1 - (ss_res / ss_tot)
print(r_squared)

ax[1].plot(xx22, [func(x, popt2[0], popt2[1], popt2[2]) for x in xx22], 'g--', label='fit: c=%.3f, a=%.3f, n=%.3f' % tuple(popt2))
ax[1].scatter(xx22, data2, label="data")
ax[1].legend()
plt.show()

"""


def Pa(x, a, b):
    return a * x * np.exp(-b * x)


def RR(x, a, b, c):
    return np.exp(- a * x**2 * np.exp(-b * x)) + c * x


dose = [3, 6, 12, 24, 60]  # , 30000]
data3 = [1.02, 0.66, 1.61, 1.57, 4.86]  #, 5.59]

popt3, pcov3 = curve_fit(RR, dose, data3, bounds=([-0, 0, 0], [2., 2., 0.5]))

print(popt3)


plt.plot(range(60), [RR(x, popt3[0], popt3[1], popt3[2]) for x in range(60)], 'g--', label='fit: a=%.3f, b=%.3f, c=%.6f' % tuple(popt3))
plt.xlabel("dose rate [mGy/h]")
plt.ylabel("hazard ratio")
# plt.xscale("log")
plt.scatter(dose, data3, label="data")
plt.legend()
plt.show()
