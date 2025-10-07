import numpy as np
import random 


# Array properties
# arr1 = np.array([[1, 2, 3],
#                  [4, 5, 6]])
# print("Shape ", arr1.shape)
# print("Dimension ", arr1.ndim)
# print("Size ", arr1.size)
# print("DType ", arr1.dtype)
# # itemsize specify the number of bytes in memory
# # required to store a single element of array
# print("Itemsize ", arr1.itemsize)


# Array reshaping
arr2 = np.arange(12)
print("Original array :", arr2)
reshaped = arr2.reshape((3, 4))
print("Reshaped array :", reshaped)

# Array flatenning, it always returns copy
flattened = reshaped.flatten()
print("Flattened Array :", flattened)

# Array raveling, it always make changes in original array
ravelled = reshaped.ravel()
print("Raveled Array :", ravelled)

# Transpose
transpose = reshaped.T
print("Transposed Array :\n", transpose)


# TYPE CONVERSION
# astype(), use to explicitly cast or convert the data of an array
# to specified types and give a new array always
arr_int = np.array([1, 2, 3, 4, 5])
print("Original array (int) :", arr_int)
arr_float = arr_int.astype(float)
print("New array (float) :", arr_float)
arr_str = arr_int.astype(str)
print("New array (string) :", arr_str)



# view(), a "view" of an array is a new array object that refers to the
# same data as the original array. This means that changes made to the
# view will also be reflected in the original array, and vice-versa. Views are
# created to avoid unnecessary memory copying, which can be beneficial for
# large arrays and performance.
original_array = np.array([1, 2, 3, 4, 5])
print("Original array :", original_array)

view_array = original_array.view()
print("View array :", view_array)

view_array[0] = 100
print("View array after modification :", view_array)
print("Original array after modification :", original_array)



# random library use
# single float number
single_float = np.random.rand()
print("Single float ", single_float)

float_array_1d = np.random.rand(5)
print("1D array :", float_array_1d)

float_array_2d = np.random.rand(3, 4)
print("2D float array :\n", float_array_2d)

# random integers
random_int = np.random.randint(10)
print("Single random integers :", random_int)

int_1d = np.random.randint(50, size=6)
print("1D int array :", int_1d)

int_2d = np.random.randint(1, 10, size=(2, 3))
print("2D int array :\n", int_2d)



# generating random number from an array
list1 = [1, 2, 7, 8, 10, 16, 5]
x1 = np.random.choice(list1)
print(x1)
x2 = np.random.choice(list1, size=(2, 3))
print(x2)


# HW
numbers = np.random.randint(10, 50, size=(2, 9, 2))
print(numbers)
even_num = numbers[numbers % 2 == 0]
print(even_num)
