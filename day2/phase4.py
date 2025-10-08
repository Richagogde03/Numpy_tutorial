import numpy as np
# BROADCASTING

# example1, Broadcasting a Scalar to a 1D Array
arr_1d = np.array([1, 2, 3])
print("adding scalar value 2 :", arr_1d + 2)

# example2, Broadcasting a 1D Array to a 2D Array
arr1_1d = np.array([2, 4, 6])
arr1_2d = np.array([[1, 3, 5],
                    [7, 9, 11]])
print("adding 1d to 2d array of expandable size :\n", arr1_1d + arr1_2d)

# example3, Using Broadcasting for Matrix Multiplication
arr2_2d = np.array([[1, 2],
                    [3, 4]])
arr2_1d = np.array([10, 20])
print("multiply 2d array by 1d array pf expandable size :\n",
      arr2_2d * arr2_1d)

# example4,
arr3_1d = np.array([1, 2, 3])
arr3_2d = np.array([[1],
                    [2],
                    [3]])
print("arr1d (1*3) shape :", arr3_1d.shape)
print("arr2d (3*1) shape :", arr3_2d.shape)
print("adding 1d (1*3) to 2d (3*1) :\n", arr3_1d + arr3_2d)
