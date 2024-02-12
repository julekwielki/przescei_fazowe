import math

from matplotlib import animation
from matplotlib.animation import PillowWriter
from matplotlib.widgets import Slider,  Button
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np


def function(x, a, b, c):
    return np.exp(- a * x**2 * np.exp(-b * x)) + c * x


def function_sig(x, b, c):
    return 1 / (1 + np.exp(-b * (x - c)))


def animate_one_set(datax, datay, minim=20, xlab="dose rate", ylab="relative risk"):  # slider datay (datax)

    fig = plt.figure(3)
    ax1 = fig.add_subplot()
    ax1.plot(datax, datay[minim])

    plt.subplots_adjust(bottom=0.25)  # making space for slider
    ax1.set_title("week: " + str(minim))
    lim = [0, max(max(p) for p in datay[minim:])*1.1]
    ax1.set_ylim(lim)
    ax1.set_xlabel(xlab)
    ax1.set_ylabel(ylab)

    axt = plt.axes([0.1, 0.07, 0.8, 0.02])  # współrzędne slidera
    st = Slider(axt, 't', minim, len(datay), valstep=1)

    def update2(val):  #
        ax1.clear()
        ax1.plot(datax, datay[st.val - 1])
        ax1.set_ylim(lim)
        ax1.set_title("week: " + str(st.val))
        ax1.set_xlabel(xlab)
        ax1.set_ylabel(ylab)

    st.on_changed(update2)
    plt.show()


def zapis(datax, datay, minim=20, xlab="dose rate", ylab="relative risk", title="one data set"):

    fig = plt.figure()
    ax1 = fig.add_subplot()
    ax1.plot(datax, datay[minim])

    ax1.set_title("week: " + str(minim))
    lim = [0, max(max(p) for p in datay[minim:])*1.1]
    ax1.set_ylim(lim)
    ax1.plot(datax, np.ones_like(datax))
    ax1.set_title("week: " + str(minim))
    ax1.set_xlabel(xlab)
    ax1.set_ylabel(ylab)

    def updatefig(x):
        ax1.clear()
        ax1.set_ylim(lim)
        ax1.set_title("week: " + str(x))
        line, = ax1.plot(datax, datay[x - 1])
        line2, = ax1.plot(datax, np.ones_like(datax))
        ax1.set_xlabel(xlab)
        ax1.set_ylabel(ylab)
        return line, line2,

    ani = animation.FuncAnimation(fig, updatefig, range(minim, len(datay)), interval=40, blit=True, repeat=True)
    writergif = animation.PillowWriter()
    ani.save(title + ".gif", writer=writergif)


def animate_two_sets(datax, datay, datax2, datay2, minim=20, xlab="dose rate", ylab="relative risk"):
    fig = plt.figure()
    ax1 = fig.add_subplot()
    ax1.plot(datax, datay[minim])
    ax1.plot(datax2, datay2[minim], 'g--')

    ax1.set_title("week: " + str(minim))
    lim = [0, max(max(p) for p in datay[minim:])*1.1]
    ax1.set_ylim(lim)
    ax1.plot(datax, np.ones_like(datax))
    ax1.set_title(minim)
    ax1.set_xlabel(xlab)
    ax1.set_ylabel(ylab)

    plt.subplots_adjust(bottom=0.25)
    axt = plt.axes([0.1, 0.07, 0.8, 0.02])
    st = Slider(axt, 't', minim, len(datay), valstep=1)

    def update2(val):
        ax1.clear()
        ax1.set_ylim(lim)
        ax1.set_title("week: " + str(st.val))
        ax1.set_xlabel(xlab)
        ax1.set_ylabel(ylab)
        ax1.plot(datax, datay[st.val - 1])
        ax1.plot(datax, np.ones_like(datax))
        ax1.plot(datax2, datay2[st.val - 1], 'g--')

    st.on_changed(update2)
    plt.show()


def zapis2(datax, datay, datax2, datay2, minim=20, title="two data sets"):

    fig = plt.figure()
    ax1 = fig.add_subplot()
    ax1.plot(datax, datay[minim])
    ax1.plot(datax2, datay2[minim], 'g--')

    ax1.set_title("week: " + str(minim))
    lim = [0, max(max(p) for p in datay[minim:])]
    ax1.set_ylim(lim)
    ax1.plot(datax, np.ones_like(datax))
    ax1.set_title(minim)
    ax1.set_xlabel("dose rate")
    ax1.set_ylabel("RR")

    def updatefig(x):
        ax1.clear()
        ax1.set_ylim(lim)
        ax1.set_title("week: " + str(x))
        ax1.set_xlabel("dose rate")
        ax1.set_ylabel("RR")
        line, = ax1.plot(datax, datay[x - 1])
        line2, = ax1.plot(datax, np.ones_like(datax))
        line3, = ax1.plot(datax2, datay2[x - 1], 'g--')
        return line, line2, line3,

    ani = animation.FuncAnimation(fig, updatefig, range(minim, len(datay)), interval=40, blit=True, repeat=True)
    writergif = animation.PillowWriter()
    ani.save(title + ".gif", writer=writergif)


x_contr = [43, 46, 50, 52, 61, 63, 64, 65, 67, 69, 70, 71, 73, 74, 75, 77, 78, 79, 82, 83, 84, 85, 89]
y_contr = [0.987, 0.974, 0.961, 0.934, 0.92, 0.907, 0.893, 0.878, 0.864, 0.85, 0.835, 0.821, 0.789, 0.757, 0.74, 0.706,
           0.689, 0.671, 0.653, 0.633, 0.614, 0.554, 0.532]

x_3 = [21, 42, 47, 53, 79, 84]
y_3 = [0.958, 0.915, 0.818, 0.77, 0.693, 0.607]

x_6 = [43, 50, 58, 72, 74, 89]
y_6 = [0.958, 0.917, 0.873, 0.818, 0.764, 0.688]

x_12 = [37, 43, 52, 53, 58, 63, 66, 74, 75, 84]
y_12 = [0.958, 0.875, 0.833, 0.789, 0.746, 0.702, 0.655, 0.605, 0.554, 0.462]

x_24 = [18, 22, 33, 36, 51, 52, 53, 58]
y_24 = [0.958, 0.917, 0.875, 0.833, 0.789, 0.743, 0.693, 0.644]

x_60 = [12, 29, 32, 35, 37, 38, 44, 45, 50, 55]
y_60 = [0.957, 0.913, 0.87, 0.783, 0.652, 0.609, 0.565, 0.522, 0.435, 0.386]  # data

XX = [x_contr, x_3, x_6, x_12, x_24, x_60]
YY = [y_contr, y_3, y_6, y_12, y_24, y_60]

dose_rates = [0, 3, 6, 12, 24, 60]

sig_fun_b = []  # b, c parameters for consecutive dose rates
sig_fun_c = []

for x in range(len(XX)):  # fitting sigmoidal function 1 / (1 + np.exp(-b * (x - c))) to the data to get continuous data
    popt1, pcov1 = curve_fit(function_sig, XX[x], YY[x], bounds=([-1, 0], [0., 150.]))
    sig_fun_b.append(popt1[0])
    sig_fun_c.append(popt1[1])

"""
nr = 55
# plotting each dataset (for given dose rate) with fitted function and one point to see how we get values for timestep
plt.figure(1)
for x in range(len(XX)):
    plt.plot(range(100), [function_sig(a, sig_fun_b[x], sig_fun_c[x]) for a in range(100)])
    plt.scatter(XX[x], YY[x], label=str(dose_rates[x]) + " mGy/h")
plt.legend()
plt.xlabel("time [weeks]")
plt.ylabel("survival [%]")
plt.plot([nr, nr], [1, 0], 'pink')
plt.scatter([nr, nr, nr, nr, nr, nr], [function_sig(nr, sig_fun_b[x], sig_fun_c[x]) for x in range(len(dose_rates))])
plt.ylim([-0.1, 1.1])
plt.show()

# survival (dose rates) for one time step shown in previous
plt.figure(2)
plt.plot(dose_rates, [function_sig(nr, sig_fun_b[x], sig_fun_c[x]) for x in range(len(dose_rates))])
plt.title("week: " + str(nr))
plt.xlabel("dose rate [mGy]")
plt.ylabel("survival [%]")
plt.ylim([-0.1, 1.1])
plt.show()
# """

survival_from_function = []  # survival = function_sig(time, b, c) - for given dose rat
cancer_risk_from_function = []  # risk = 1 - survival
for x in range(100):
    a = []
    b = []
    for y in range(len(sig_fun_b)):  # for every dose rate
        i = function_sig(x, sig_fun_b[y], sig_fun_c[y])
        a.append(1 - i)
        b.append(i)
    cancer_risk_from_function.append(a)
    survival_from_function.append(b)


# animate_one_set(dose_rates, cancer_risk_from_function)  # plots one dataset on a plot with slider
# zapis(dose_rates, survival_from_function, 50, "dose rate", "survival", "survival")
# zapis(dose_rates, cancer_risk_from_function, 50, "dose rate", "risk", "cancer risk")

"""
only_doses = [3, 6, 12, 24, 60]
do_wizki_RR = []  # cancer risk (CR) for a dose / CR for 0 Gy

for x in range(len(cancer_risk_from_function)):
    a = []
    for y in range(len(only_doses)):
        a.append(cancer_risk_from_function[x][y+1]/cancer_risk_from_function[x][0])
    do_wizki_RR.append(a)  # RR for given week for each dose rate

# animate_one_set(only_doses, do_wizki_RR, 50)
# zapis(only_doses, do_wizki_RR, 50, "dose rate", "relative risk", "relative risk")
# """

"""
nr = 90
popt1, pcov1 = curve_fit(function, only_doses, do_wizki_RR[nr], bounds=([-0, 0, 0], [2., 2., 0.5]))  # fitting funstion
# of a relative risk that takes into account adaptive response, for one time point (nr)
print(popt1)
plt.plot(range(60), [function(x, popt1[0], popt1[1], popt1[2]) for x in range(60)],'g--',  label='fit: a=%.3f, b=%.3f, c=%.3f' % tuple(popt1))
plt.plot(only_doses, do_wizki_RR[nr], label="data")
plt.legend()
plt.show()
# """

"""
abc = [[], [], []]
mi, ma = 70, 100
for nr in range(mi, ma):
    popt1, pcov1 = curve_fit(function, only_doses, do_wizki_RR[nr], bounds=([-0, 0, 0], [2., 2., 0.5]))
    abc[0].append(popt1[0])
    abc[1].append(popt1[1])
    abc[2].append(popt1[2])
    # print(nr, popt1[0], popt1[1], popt1[2])
    # plt.plot(range(60), [function(x, popt1[0], popt1[1], popt1[2]) for x in range(60)], label='fit: a=%.3f, b=%.3f, c=%.3f' % tuple(popt1))
    # plt.scatter(only_doses, do_wizki_RR[nr], label="data")
    # plt.legend()
    # plt.show()

plt.title("exp(- a * x^2 * exp(-b * x)) + c * x")
plt.scatter(range(mi, ma), abc[0], label="a")
plt.scatter(range(mi, ma), abc[1], label="b")
plt.scatter(range(mi, ma), abc[2], label="c")
plt.legend()
plt.show()

# """
"""
dat = []
for nr in range(100):
    popt1, pcov1 = curve_fit(function, only_doses, do_wizki_RR[nr], bounds=([-0, 0, 0], [2., 2., 0.5]))
    print(nr, popt1[0], popt1[1], popt1[2])
    a = [function(x, popt1[0], popt1[1], popt1[2]) for x in range(60)]
    dat.append(a)

animate_two_sets(only_doses, do_wizki_RR, range(60), dat, 70)
# zapis2(only_doses, do_wizki_RR, range(60), dat, 70, title="fits for times")
# """
