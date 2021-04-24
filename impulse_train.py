import scipy
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

fc=145.97e6

Rb=9600

Fs=16*fc
t=np.linspace(0,1,Fs/Rb)

y=np.zeros(len(t))

for i in range(len(t)):
	if i%(Rb)==0:
		y[i]=1


print(len(t))
plt.plot(t,y)
plt.show()

