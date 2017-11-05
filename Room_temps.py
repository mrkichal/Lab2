import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
from statistics import mean

data = np.fromfile('roomtempbn100Mf1000.dat', dtype='int16') - 2 ** 11
data = data - np.mean(data)

data_fft = np.fft.fft(data[0:2**19].reshape(-1,1024),axis=1)
s_data_fft = (data_fft .real**2+data_fft.imag**2).sum(axis=0)
plt.plot(10*np.log10(s_data_fft[0:512]),'.',label = '1000')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.title('Freq vs Spectral Power')
plt.ylim(70,140)
plt.legend()
plt.show()