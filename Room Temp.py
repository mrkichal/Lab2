# import numpy as np
# myarray = np.fromfile('roomtempn100Mf609.dat',dtype=float)
#
# print(myarray[0:2])

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

data = np.fromfile('roomtempn100Mf609.dat', dtype='int16') - 2 ** 11


# -3.08037959
# -3.0
# 30.526131936
# 931.844730972

def mmsv():
    print(np.mean(data))
    print(np.median(data))
    print(np.std(data))
    print(np.var(data))


mean = -3.08037959
room_temp_mean_adjusted = data - mean


def sp():  # Plotting the scatter plot
    x_axis = np.arange(0.0, .000001, 0.000000001)
    y = room_temp_mean_adjusted[0:1000]
    plt.xlim(0, .000001)
    plt.ylim(-200, 200)
    plt.xlabel('Time 1ns samples')
    plt.ylabel('ADC Value [bits]')
    plt.title('Room Temperature Run')
    plt.scatter(x_axis, y)
    plt.show()


def his():  # plotting the histogram
    image_his_x = [-200, -190, -180, -170, -160, -150, -140, -130, -120, -110, -100, -90, -80, -70, -60, -50, -40, -30,
                   -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190,
                   200]
    plt.hist(room_temp_mean_adjusted, image_his_x, histtype='step', label='Data')
    plt.xlabel('ADC Value [bits]')
    plt.ylabel('Count')
    plt.title('Histogram of room temperature run')
    plt.show()


def sq_hist():
    room_temp_mean_adjusted_sq = room_temp_mean_adjusted ** 2
    x = (list(range(0, 300, 50)))
    plt.hist(room_temp_mean_adjusted, x, histtype='step', label='Data')
    plt.gca().set_yscale("log")
    plt.xlabel('Power')
    plt.ylabel('Log of count')
    plt.title('Log histogram of power')
    plt.show()


def con_add():
    adj_2 = []
    # for _ in range(2,100000000-2,2):
    #     adj_2.append([_] + room_temp_mean_adjusted[_+1])
    adj_2 = np.add.reduceat(room_temp_mean_adjusted, np.arange(0, len(room_temp_mean_adjusted), 100))
    image_his_x = list(range(0, 200, 20))
    adj_2 = adj_2 ** 2
    plt.hist(adj_2, image_his_x, histtype='step', label='Data')
    plt.xlabel('ADC Value [bits]')
    plt.ylabel('Count')
    plt.xlim(0, 200)
    # plt.ylim(30000, 4000000)
    plt.gca().set_yscale("log")
    plt.title('Histogram of room temperature run, n = 10')
    plt.show()


def thousand_sample_avg():
    data = np.add.reduceat(room_temp_mean_adjusted, np.arange(0, len(room_temp_mean_adjusted), 1000))
    data = data / 1000
    print(len(data))
    x_axis = np.arange(0.0, .0001, 0.000000001)
    print(len(x_axis))
    plt.xlim(0, .0001)
    plt.ylim(-5, 5)
    plt.xlabel('Time 1ns samples')
    plt.ylabel('ADC Value [bits]')
    plt.title('Room Temperature Run, sample of 1000 bits')
    plt.scatter(x_axis, data)
    plt.show()


def fft():
    data = np.fft.fft(room_temp_mean_adjusted)
    real = np.square(np.real(data))
    imag = np.square(np.imag(data))
    data = real + imag

fft()
