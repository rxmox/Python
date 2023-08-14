import numpy as np
import matplotlib.pyplot as plt


plt.plot(days, data_2021[:,2], 'r--')
plt.xlabel("Date in May")
plt.ylabel("Mean Temp in C")
plt.xticks(days)


# array1 = np.array([1,2,3,4,5])
# array2 = np.array([0,2,4,6,8])

# array_result = array1 - array2 -2

# print(array_result)