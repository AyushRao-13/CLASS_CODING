import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#MATH
print("Square root: ", math.sqrt(25))
print("Factorial: ", math.factorial(5))
print("Power: ", math.pow(2,3))
print("Ceiling: ", math.ceil(4.3))
print("Floor: ", math.floor(4.7))
print("Pie: ", math.pi)
print("Euler's Number: ", math.e)

#NUMPY
arr = np.array([1,2,3,4,5])

print("Array: ", arr)
print("Mean: ", np.mean(arr))
print("Sum: ", np.sum(arr))
print("Max: ", np.max(arr))

matrix = np.array([[2,4], [6,8]])
print("Matrix:\n", matrix)
print("Transpose:\n", matrix.T)

#MATPLOT LIBRARY 
x = [1,2,3,4,5]
y= [10,20,30,40,50]
plt.plot(x,y)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line Graph")
plt.show()

#SEABORN
data = [10,20,30,40,50]
sns.histplot(data)
plt.title("Seaborn Histogram")
plt.show()

#SCIPY LIBRARY
from scipy import stats
data = [10,20,30,40,50]
print("Mean: ", stats.tmean(data))
print("Median:  ", stats.scoreatpercentile(data,50))
print("Mode: ", stats.mode(data))