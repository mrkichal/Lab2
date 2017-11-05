import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
from statistics import mean

room_609 = np.fromfile('roomtempn100Mf609.dat', dtype='int16') - 2 ** 11
room_609 = room_609 - np.mean(room_609)
boil = np.fromfile('boilingn100Mf609.dat', dtype='int16') - 2 ** 11
boil = boil - np.mean(boil)
dry_ice = np.fromfile('dryicen100Mf609.dat', dtype='int16') - 2 ** 11
dry_ice = dry_ice - np.mean(dry_ice)
ice_water = np.fromfile('iceicebabyn100Mf609.dat', dtype='int16') - 2 ** 11
ice_water = ice_water - np.mean(ice_water)
nitrogen = np.fromfile('nitrogenn100Mf609.dat', dtype='int16') - 2 ** 11
nitrogen = nitrogen - np.mean(nitrogen)


def mean_variance():
    mean_room_609 = np.mean(room_609)
    mean_boil = np.mean(boil)
    mean_dry_ice = np.mean(dry_ice)
    mean_ice_water = np.mean(ice_water)
    mean_nitrogen = np.mean(nitrogen)
    var_room_609 = np.var(room_609)
    var_boil = np.var(boil)
    var_dry_ice = np.var(dry_ice)
    var_ice_water = np.var(ice_water)
    var_nitrogen = np.var(nitrogen)
    # -3.08037959 - 3.06331513 - 3.06687235 - 3.07039269 - 3.05681245
    # 931.844730972 955.273582404 851.667162399  915.937953979 775.760108436
    print(mean_room_609, mean_boil, mean_dry_ice, mean_ice_water, mean_nitrogen)
    print(var_room_609, var_boil, var_dry_ice, var_ice_water, var_nitrogen)

    x_axis = np.arange(-150, 150, 1)
    plt.hist(room_609, x_axis, histtype='step', label='Room')
    plt.hist(boil, x_axis, histtype='step', label='Boil')
    plt.hist(dry_ice, x_axis, histtype='step', label='Dry Ice')
    plt.hist(ice_water, x_axis, histtype='step', label='Ice Water')
    plt.hist(nitrogen, x_axis, histtype='step', label='Nitrogen')
    plt.xlabel('ADC Value [bits]')
    plt.ylabel('Count')
    plt.title('Histogram of various (Overlap)')
    plt.legend()
    plt.ylim(1, 1600000)
    plt.show()


def lin_graph():
    var_room_609 = 931.844730972
    var_boil = 955.273582404
    var_dry_ice = 851.667162399
    var_ice_water = 915.937953979
    var_nitrogen = 775.760108436
    y = np.array([931.844730972, 955.273582404, 851.667162399, 915.937953979, 775.760108436])
    x = np.array([303.5, 365.1, 194.8, 273.4, 77.3])
    bf_y = [728.08, 988.38]
    bf_x = [0, 400]
    plt.plot(bf_x, bf_y)
    plt.scatter(x, y)
    plt.ylim(0, 1400)
    plt.xlim(0, 400)
    m = (((mean(x) * mean(y)) - mean(x * y)) / ((mean(x) * mean(x)) - mean(x * x)))
    b = mean(y) - m * mean(x)
    print(m, b) # m = 0.650743866477 b = 728.08308198
    plt.xlabel('Load Temp in K')
    plt.ylabel('Power in bits^2')
    plt.title('Power vs Load Temp')
    plt.show()


def fft():
    room_609_fft = np.fft.fft(room_609[0:2**19].reshape(-1,1024),axis=1)
    s_room_609_fft = (room_609_fft .real**2+room_609_fft .imag**2).sum(axis=0)
    plt.plot(10*np.log10(s_room_609_fft[0:512]),'.',label = '303.5 K')

    boil_fft = np.fft.fft(boil[0:2 ** 19].reshape(-1, 1024), axis=1)
    s_boil_fft = (boil_fft.real ** 2 + boil_fft.imag ** 2).sum(axis=0)
    plt.plot(10 * np.log10(s_boil_fft[0:512]), '.',label = '365.1 K')

    dry_ice_fft = np.fft.fft(dry_ice[0:2 ** 19].reshape(-1, 1024), axis=1)
    s_dry_ice_fft = (dry_ice_fft.real ** 2 + dry_ice_fft.imag ** 2).sum(axis=0)
    plt.plot(10 * np.log10(s_dry_ice_fft[0:512]), '.', label = '194.9 K')

    ice_water_fft = np.fft.fft(ice_water[0:2 ** 19].reshape(-1, 1024), axis=1)
    s_ice_water_fft = (ice_water_fft.real ** 2 + ice_water_fft.imag ** 2).sum(axis=0)
    plt.plot(10 * np.log10(s_ice_water_fft[0:512]), '.', label = '273.4 K')

    nitrogen_fft = np.fft.fft(nitrogen[0:2 ** 19].reshape(-1, 1024), axis=1)
    s_nitrogen_fft = (nitrogen_fft.real ** 2 + nitrogen_fft.imag ** 2).sum(axis=0)
    plt.plot(10 * np.log10(s_nitrogen_fft[0:512]), '.', label = '77.3 K')


    plt.xlabel('Frequency in MHz')
    plt.ylabel('Power')
    plt.title('Load Temp vs Spectral Power')
    plt.legend()
    # plt.xlim(609.0, 610)
    plt.show()

fft()