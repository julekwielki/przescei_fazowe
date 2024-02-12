from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np


def function(x, a, b, c):
    return np.exp(- a * x**2 * np.exp(-b * x)) + c * x


dose = [3, 6, 12, 24, 60]  #, 30000]
data3 = [1.02, 0.66, 1.61, 1.57, 4.86] # , 5.59]  # Imaoka 19

popt3, pcov3 = curve_fit(function, dose, data3, bounds=([-0, 0, 0], [2., 2., 0.5]))
print(popt3)

plt.plot(range(60), [function(x, popt3[0], popt3[1], popt3[2]) for x in range(60)], 'g--', label='fit: a=%.3f, b=%.3f, c=%.6f' % tuple(popt3))
plt.xlabel("dose rate [mGy/h]")
plt.ylabel("hazard ratio")
# plt.xscale("log")
plt.scatter(dose, data3, label="data")
plt.legend()
plt.show()
