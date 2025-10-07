# Numpy array and basics
import numpy as np

# creating array from list using array() function
# arr_1d = np.array([1, 2, 3, 4, 5])
# print("Array 1D:", arr_1d)

# arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
# print("Array 2D:", arr_2d)

# arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print("Array 3D:", arr_3d)


# Check Number of Dimentions
# a = np.array(42)
# b = np.array((1, 2, 3,))
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[2, 4, 6], [8, 10, 12]], [[14, 16, 18], [20, 22, 24]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)


# Higher Dimensional Arrays
# array = np.array([1, 2, 3, 4], ndmin=5)
# print("Higher dimentional arrays:", array)
# print("number of dimentions in arr1:", array.ndim)


# Accessing array elements
# arr1d = np.array([1, 2, 3, 4])
# print(arr1d[3])

# arr2d = np.array([[1, 2, 3], [4, 5, 6]])
# # 2nd element on 1st row
# print(arr2d[1, 2])

# arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# # first num = 1d, 2nd num = 2d, 3rd num=3d
# print(arr3d[0, 1, 2])

neg_arr = np.array([[2, 3, 4, 5], [6, 7, 8, 9]])
# print("Last element from 2nd dim :", neg_arr[1, -1])


# Creating array from scratch
# zeros array
zeros = np.zeros((3, 4))
print("zeros array :\n", zeros)

# ones array
ones = np.ones((2, 3))
print("Ones array :\n", ones)

# for special constant in an array
full = np.full((2, 2), 7)
print("full array :\n", full)

sequence = np.arange(0, 10, 2)
print("Sequence :\n", sequence)

# linspace(), generates an array of evenly spaced
# numbers over a specified interval
even_space = np.linspace(0, 10, 5)
print("Even spacing of 5 numbers between 0 to 10 ", even_space)

# np.eye(), returns a 2D array with ones on the diagonal and zero elsewhere
eye_2d = np.eye(3)
print("Identity Matrix \n", eye_2d)

# VECTOR, MATRIX and TENSOR
vector = np.array([1, 2, 3])
print("Vector :", vector)

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print("Matrix :", matrix)

tensor = np.array([[[2, 4], [1, 3]],
                   [[6, 8], [5, 7]]])
print("Tensor :", tensor)
