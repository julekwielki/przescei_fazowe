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


def wizka1(danex, daney, title="", minim=20):

    fig = plt.figure(1)
    ax1 = fig.add_subplot()
    ax1.plot(danex, daney[20])

    plt.subplots_adjust(bottom=0.25)  # przesuwam żeby mi się zmieściły slidery i przyciski
    ax1.set_title("tydzien nr: " + str(minim))
    lim = [0, max(max(p) for p in daney[minim:])]
    ax1.set_ylim(lim)
    ax1.set_xlabel("dose rate")
    ax1.set_ylabel("survival")

    axt = plt.axes([0.1, 0.07, 0.8, 0.02])  # współrzędne slidera
    st = Slider(axt, 't', minim, len(daney), valstep=1)

    def update2(val):  #
        ax1.clear()
        ax1.plot(danex, daney[st.val - 1])
        ax1.set_ylim(lim)
        ax1.set_title("tydzien nr: " + str(st.val))
        ax1.set_xlabel("dose rate")
        ax1.set_ylabel("survival")

    st.on_changed(update2)
    plt.show()


def wizka2(danex, daney, title="", minim=20):

    fig = plt.figure()
    ax1 = fig.add_subplot()
    ax1.plot(danex, daney[minim])

    plt.subplots_adjust(bottom=0.25)  # przesuwam żeby mi się zmieściły slidery i przyciski
    ax1.set_title(title)
    lim = [0, max(max(p) for p in daney[minim:])]
    ax1.set_ylim(lim)
    ax1.plot(danex, np.ones_like(danex))
    ax1.set_title("tydzien nr: " + str(minim))
    ax1.set_xlabel("dose rate")
    ax1.set_ylabel("risk")

    axt = plt.axes([0.1, 0.07, 0.8, 0.02])  # współrzędne slidera
    st = Slider(axt, 't', minim, len(daney), valstep=1)

    def update2(val):  #
        ax1.clear()
        ax1.plot(danex, daney[st.val - 1])
        ax1.plot(danex, np.ones_like(danex))
        ax1.set_title("tydzien nr: " + str(st.val))
        ax1.set_xlabel("dose rate")
        ax1.set_ylabel("risk")
        ax1.set_ylim(lim)

    st.on_changed(update2)
    plt.show()


def wizka3(danex, daney, daney2, title="", minim=20):
    fig = plt.figure()
    ax1 = fig.add_subplot()
    ax1.plot(danex, daney[minim])
    ax1.plot(range(60), daney2[minim])

    plt.subplots_adjust(bottom=0.25)

    ax1.set_title("week: " + str(minim))
    lim = [0, 4]  # max(max(p) for p in daney[minim:])]
    ax1.set_ylim(lim)
    ax1.plot(danex, np.ones_like(danex))
    ax1.set_title(minim)
    ax1.set_xlabel("dose rate")
    ax1.set_ylabel("Risk")

    axt = plt.axes([0.1, 0.07, 0.8, 0.02])  # współrzędne slidera
    st = Slider(axt, 't', minim, len(daney), valstep=1)

    def update2(val):  #
        ax1.clear()
        ax1.set_ylim(lim)
        ax1.set_title("week: " + str(st.val))
        ax1.set_xlabel("dose rate")
        ax1.set_ylabel("RR")
        ax1.plot(danex, daney[st.val - 1])
        ax1.plot(danex, np.ones_like(danex))
        ax1.plot(range(60), daney2[st.val - 1], 'g--')

    st.on_changed(update2)
    plt.show()

def zapis(danex, daney, title="", minim=20):

    fig = plt.figure()
    ax1 = fig.add_subplot()
    ax1.plot(danex, daney[minim])

    ax1.set_title(title)
    lim = [0, max(max(p) for p in daney[minim:])]
    ax1.set_ylim(lim)
    ax1.plot(danex, np.ones_like(danex))
    ax1.set_title(minim)

    def updatefig(x):
        ax1.clear()
        ax1.set_ylim(lim)
        ax1.set_title(x)
        line, = ax1.plot(danex, daney[x - 1])
        line2, = ax1.plot(danex, np.ones_like(danex))
        return line, line2,

    ani = animation.FuncAnimation(fig, updatefig, range(minim, len(daney)), interval=40, blit=True, repeat=True)
    writergif = animation.PillowWriter()
    ani.save(title + ".gif", writer=writergif)


def zapis2(danex, daney, daney2, title="", minim=20):

    fig = plt.figure()
    ax1 = fig.add_subplot()
    ax1.plot(danex, daney[minim])
    ax1.plot(range(60), daney2[minim])

    ax1.set_title("week: " + str(minim))
    lim = [0, max(max(p) for p in daney[minim:])]
    ax1.set_ylim(lim)
    ax1.plot(danex, np.ones_like(danex))
    ax1.set_title(minim)
    ax1.set_xlabel("dose rate")
    ax1.set_ylabel("RR")

    def updatefig(x):
        ax1.clear()
        ax1.set_ylim(lim)
        ax1.set_title("week: " + str(x))
        ax1.set_xlabel("dose rate")
        ax1.set_ylabel("RR")
        line, = ax1.plot(danex, daney[x - 1])
        line2, = ax1.plot(danex, np.ones_like(danex))
        line3, = ax1.plot(range(60), daney2[x - 1], 'g--')
        return line, line2, line3,

    ani = animation.FuncAnimation(fig, updatefig, range(minim, len(daney)), interval=40, blit=True, repeat=True)
    writergif = animation.PillowWriter()
    ani.save(title + ".gif", writer=writergif)

x_contr = [43, 46, 50, 52, 61, 63, 64, 65, 67, 69, 70, 71, 73, 74, 75, 77, 78, 79, 82, 83, 84, 85, 89]
y_contr = [0.987, 0.974, 0.961, 0.934, 0.92, 0.907, 0.893, 0.878, 0.864, 0.85, 0.835, 0.821, 0.789, 0.757, 0.74, 0.706, 0.689, 0.671, 0.653, 0.633, 0.614, 0.554, 0.532]

x_3 = [21, 42, 47, 53, 79, 84]
y_3 = [0.958, 0.915, 0.818, 0.77, 0.693, 0.607]

x_6 = [43, 50, 58, 72, 74, 89]
y_6 = [0.958, 0.917, 0.873, 0.818, 0.764, 0.688]

x_12 = [37, 43, 52, 53, 58, 63, 66, 74, 75, 84]
y_12 = [0.958, 0.875, 0.833, 0.789, 0.746, 0.702, 0.655, 0.605, 0.554, 0.462]

x_24 = [18, 22, 33, 36, 51, 52, 53, 58]
y_24 = [0.958, 0.917, 0.875, 0.833, 0.789, 0.743, 0.693, 0.644]

x_60 = [12, 29, 32, 35, 37, 38, 44, 45, 50, 55]
y_60 = [0.957, 0.913, 0.87, 0.783, 0.652, 0.609, 0.565, 0.522, 0.435, 0.386]

XX = [x_contr, x_3, x_6, x_12, x_24, x_60]
YY = [y_contr, y_3, y_6, y_12, y_24, y_60]

dose_rates = [0, 3, 6, 12, 24, 60]

BB = []
CC = []

for x in range(len(XX)):
    popt1, pcov1 = curve_fit(function_sig, XX[x], YY[x], bounds=([-1, 0], [0., 150.]))

    BB.append(popt1[0])
    CC.append(popt1[1])
    """
    plt.plot(XX[x], [function_sig(x, popt1[0], popt1[1]) for x in XX[x]],
             label='fit: a=%.3f, b=%.3f' % tuple(popt1))
    plt.scatter(XX[x], YY[x], label="data")
    plt.legend()
    plt.title("survival (time) for dose: " + str(dose_rates[x]) + " mGy/h")
    plt.show()
    # """


do_wizki_dane = []
for x in range(100):
    a = []
    for y in range(len(BB)):
        a.append(1 - function_sig(x, BB[y], CC[y]))
    do_wizki_dane.append(a)

title = "cancer risk (dose rate) - na suwaku czas"
wizka1(dose_rates, do_wizki_dane, title)

only_doses = [3, 6, 12, 24, 60]
do_wizki_RR = []
for x in range(len(do_wizki_dane)):

    a = []
    for y in range(len(only_doses)):
        a.append(do_wizki_dane[x][y+1]/do_wizki_dane[x][0])
    do_wizki_RR.append(a)

# title = "Relative Rist (dose rate) - na suwaku czas"
wizka2(only_doses, do_wizki_RR, title, 50)
# zapis(only_doses, do_wizki_RR, title, 50)

nr = 75
popt1, pcov1 = curve_fit(function, only_doses, do_wizki_RR[nr], bounds=([-0, 0, 0], [2., 2., 0.5]))
print(popt1[0], popt1[1], popt1[2])

plt.plot(range(60), [function(x, popt1[0], popt1[1], popt1[2]) for x in range(60)],'g--',  label='fit: a=%.3f, b=%.3f, c=%.3f' % tuple(popt1))
plt.scatter(only_doses, do_wizki_RR[nr], label="data")
plt.legend()

plt.show()

"""
for nr in range(70, 90):
    popt1, pcov1 = curve_fit(function, only_doses, do_wizki_RR[nr], bounds=([-0, 0, 0], [2., 2., 0.5]))

    print(nr, popt1[0], popt1[1], popt1[2])

    # plt.plot(range(60), [function(x, popt1[0], popt1[1], popt1[2]) for x in range(60)], label='fit: a=%.3f, b=%.3f, c=%.3f' % tuple(popt1))
    # plt.scatter(only_doses, do_wizki_RR[nr], label="data")
    # plt.legend()
    # plt.show()
"""

dat = []
for nr in range(100):
    popt1, pcov1 = curve_fit(function, only_doses, do_wizki_RR[nr], bounds=([-0, 0, 0], [2., 2., 0.5]))
    print(nr, popt1[0], popt1[1], popt1[2])
    a = [function(x, popt1[0], popt1[1], popt1[2]) for x in range(60)]
    dat.append(a)

wizka3(only_doses, do_wizki_RR, dat, title, 50)
zapis2(only_doses, do_wizki_RR, dat, title, 70)
