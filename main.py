# transformacja nowotworowa w funkcji liczby mutacji
# parametry za Fornalski & Dobrzyński
import math
import matplotlib.pyplot as plt
import random
import numpy as np
import time
from numpy.lib.stride_tricks import sliding_window_view


C = 1  # wartość wysycenia
kal_k = 4.4  # wyznaczony w publikacji parametr k
kal_a = 0.0087  # wyznaczony w publikacji parametr a
n = 5*3**4  # początkowy rozmiar (bok) 3^x — wielokrotność 3

kal_k = 3  # wyznaczony w publikacji parametr k
kal_a = 0.01  # wyznaczony w publikacji parametr a

kk_max = 7  # ograniczenie zakresu k = <0, kk_max>
aa_max = 0.04  # ograniczenie zakresu a = <0, aa_max>
m = 4.1  # liczba mutacji
window = 3  # rozmiar okna


# m — liczba mutacji,
# a, k — parametry
def p_m(k, a, mm=1.):  # funkcja p = 1 - exp(-a*m^k))
    return C*(1-math.exp(-a * math.pow(mm, k)))


# sprawdzenie których wartości jest więcej w ruchomym oknie, okna nie przekrywają się
# win — rozmiar okna
# arr — tablica początkowa z wartościami, które sprawdzamy w ruchomym oknie
# arr2 — tablica końcowa z uzyskanymi wartościami — trzykrotnie mniejsza
def most_pool(arr, arr2, win=3):
    v = sliding_window_view(arr, (win, win))[::win, ::win]  # stworzenie okien o boku "win"
    for xx in range(len(v[0])):  # dla każdego "okna"
        for yy in range(len(v[0])):
            val = sum(sum(v[xx][yy]))  # suma wartości w oknie
            if val > 4:
                arr2[xx][yy] = 1
    return arr2


# wizualizacja tablicy
# "a" i "k" dotyczą
def rysuj(arr, a_max=aa_max, k_max=kk_max, tick=7, title=""):
    fig = plt.figure()
    plt.imshow(arr, vmin=0, vmax=1)
    plt.xlabel("zmiana paramtru a")
    plt.ylabel("zmiana parametru k")
    # plt.xticks(ticks=np.linspace(0, n, tick), labels=np.round(np.linspace(0, a_max, tick), 3))
    # plt.yticks(ticks=np.linspace(0, n, tick), labels=np.round(np.linspace(0, k_max, tick), 1))
    plt.gca().invert_yaxis()
    plt.title(title)
    plt.colorbar()
    # nazwa = "C:/Users/Jules/Desktop/faz/" + title + ".png"
    nazwa = title + ".png"
    plt.savefig(nazwa)
    # plt.show()


# monte carlo dla całej macierzy
def MC(arr, arr2):
    length = len(arr)
    for xx in range(length):
        for yy in range(length):
            if random.random() <= arr[xx][yy]:
                arr2[xx][yy] = 1
    return arr2


def wyp_const(arr, mut=m, k=kal_k, a=kal_a):
    for xx in range(len(arr)):
        for yy in range(len(arr)):
            arr[xx][yy] = p_m(k, a, mut)  # dla stałych parametrów (tylko tyle że dużo razy)
    return arr


def wyp_dif(arr, mut=m, k_max=kk_max, a_max=aa_max):
    xx = 0  # współrzędne do wypełnienia macierzy
    for kk in np.linspace(0, k_max, n):
        yy = 0
        for aa in np.linspace(0, a_max, n):
            arr[xx][yy] = p_m(kk, aa, mut)
            yy += 1
        xx += 1
    return arr


mac = wyp_const(np.zeros((n, n), dtype=float), m, kal_k, kal_a)
# mac = wyp_dif(np.zeros((n, n), dtype=float), m, kk_max, aa_max)
rysuj(mac)


MC_mac = MC(mac, np.zeros((n, n), dtype=int))
rysuj(MC_mac)

wszystkie = [MC_mac]  # do wyświetlenia wszystkich wyników po kolei
old_array = MC_mac.copy()  # macierz większa
new_size = int(len(old_array)/window)  # bok mniejszej macierzy
new_array = np.zeros((new_size, new_size), dtype=int)  # nowa macierz o określonym boku

"""
for mmm in np.linspace(1, 4, 10):
    mac = np.zeros((n, n), dtype=float)  # macierz do symulacji
    for x in range(n):
        for y in range(n):
            mac[x][y] = p_m(kal_k, kal_a, m)  # dla stałych parametrów (tylko tyle że dużo razy)
    MC_mac = MC(mac, np.zeros((n, n), dtype=int))
    rysuj(MC_mac, title=f"{mmm:0.2f}")
# """

# """
while new_size > 3 and len(old_array) % window == 0:  # sprawdzanie, czy jest sens jeszcze zmniejszać macierz
    new_array = most_pool(old_array, new_array, window)  # nowa tablica = przetworzona stara tablica
    rysuj(new_array, title="m=" + str(m) + " k=" + str(kal_k) + " a=" + str(kal_a) + " " + str(len(wszystkie)))
    wszystkie.append(new_array)  # dodanie tablicy do wizualizacji potem
    old_array = new_array.copy()  # nowa "stara tablica"
    new_size = int(len(new_array) / window)  # nowa długość boku mniejszej tablicy
    new_array = np.zeros((new_size, new_size), dtype=int)  # nowa "nowa tablica"

# """

"""
for x in wszystkie:  # wizualizacja wszystkich kroków po kolei
    rysuj(x)
# """