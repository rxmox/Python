# ENDG 233 F21 Demonstration of NumPy and Matplotlib modules
# Code associated with Week 9 Part 4 video


import numpy as np
import matplotlib.pyplot as plt


data_2021 = np.genfromtxt('datademo_May2021.csv', delimiter = ',', skip_header = True)
print(data_2021)

data_2020 = np.genfromtxt('datademo_May2020.csv', delimiter = ',', skip_header = True)
print(data_2020)

data_2019 = np.genfromtxt('datademo_May2019.csv', delimiter = ',', skip_header = True)
print(data_2019)

days = list(range(1,16))
print(days)


print('Highest temp in 2021 is', data_2021.max())

print('Highest temp on May 3 in 2021 is', data_2021[2][0])
print('Highest temp on May 3 in 2021 is', data_2021[2].max())

print('Highest max temp in 2021 is', data_2021[:,0].max())
print('Lowest min temp in 2021 is', data_2021[:,1].min())


plt.subplot(3,1,1)
plt.plot(days, data_2021[:,2])
plt.xlabel("Date in May")
plt.ylabel("Mean Temp in C")
plt.axis([1, 15, -5, 25])

plt.subplot(3,1,2)
plt.plot(days, data_2020[:,2])
plt.xlabel("Date in May")
plt.ylabel("Mean Temp in C")
plt.axis([1, 15, -5, 25])

plt.subplot(3,1,3)
plt.plot(days, data_2019[:,2])
plt.xlabel("Date in May")
plt.ylabel("Mean Temp in C")
plt.axis([1, 15, -5, 25])


plt.show()
