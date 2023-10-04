from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import math


def func(x, c, a, n):
    return c * (1 - np.exp(-a * np.power(x, n)))


xx = [21, 38, 59, 76]
xx2 = [x/100 for x in xx]
data = [0.038, 0.08, 0.126, 0.206]
# plt.scatter(xx2, data)
# plt.show()


popt, pcov = curve_fit(func, xx2, data, bounds=([0, 0, 0], [1., 5., 6.]))
perr = np.sqrt(np.diag(pcov))  # standard deviation error - nie zawsze pradziwe

print(popt)
print(perr)
plt.plot(xx2, [func(x, popt[0], popt[1], popt[2]) for x in xx2], 'g--', label='fit: c=%5.3f, a=%5.3f, n=%5.3f' % tuple(popt))
plt.scatter(xx2, data, label="data")
plt.legend()
plt.show()


xx = [42, 47, 57, 59, 63, 66, 80, 81, 88, 90, 91]
xx2 = [x/100 for x in xx]
data = [0.043, 0.089, 0.146, 0.203, 0.26, 0.327, 0.439, 0.551, 0.664, 0.776, 0.888]

popt, pcov = curve_fit(func, xx2, data, bounds=([0.5, 1, 1], [1., 5., 6.]))
perr = np.sqrt(np.diag(pcov))  # standard deviation error - nie zawsze pradziwe

print(popt)
print(perr)
plt.plot(xx2, [func(x, popt[0], popt[1], popt[2]) for x in xx2], 'g--', label='fit: c=%5.3f, a=%5.3f, n=%5.3f' % tuple(popt))
plt.scatter(xx2, data, label="data")
plt.legend()
plt.show()
