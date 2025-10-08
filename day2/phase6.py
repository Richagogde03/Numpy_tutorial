import numpy as np

# Reshaping and Combining Arrays
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


# Swapaxes(input_array, axis1, axis2) using 3d array
swapaxes_3d = np.arange(24).reshape(2, 3, 4)
print("before swapping axis :\n", swapaxes_3d)
print("shape before axis swap :", swapaxes_3d.shape)

# swapped_arr = np.swapaxes(swapaxes, 0, 2)
swapped_arr1 = np.swapaxes(swapaxes_3d, 0, 1)
print("After swapping using swapaxes :\n", swapped_arr1)
print("Shape of array after swapping :", swapped_arr1.shape)

# Swapaxes using 2d matrix
swapaxes_2d = np.array([[1, 2, 3],
                       [4, 5, 6]])
print("Original 2D Array before swapping :\n", swapaxes_2d)
swapped_arr2 = np.swapaxes(swapaxes_2d, 0, 1)
print("2d Array after swapping axes:\n", swapped_arr2)


# concatenate()
concate_a1 = np.array([[1, 2],
                       [3, 4]])
concate_a2 = np.array([[5, 6],
                       [7, 8]])
print("Concate vertically axis=0 :\n", np.concatenate((concate_a1, concate_a2),
                                                      axis=0))
print("Concate horizontlly :\n", np.concatenate((concate_a1, concate_a2),
                                                axis=1))

# Stack(), used to join a sequence of arrays along a new axis
# Unlike numpy.concatenate(), which joins arrays along an existing axis,
# np.stack() creates a new dimension in the resulting array.
stack1 = np.array([1, 2, 3])
stack2 = np.array([4, 5, 6])
result = np.stack((stack1, stack2))
print("Stack array by default axis=0:\n", result)
print("Stack array horizontally axis=1:\n", np.stack((stack1, stack2), axis=1))


# vstack(), vertically stack
vstack1 = np.array([[0, 1],
                    [2, 3]])
vstack2 = np.array([[4, 5],
                    [6, 7]])
print("using vstack in 2d array:\n", np.vstack((vstack1, vstack2)))


# hstack, horizontally stack


# np.split(array, indices_or_sections, axis=0), split an array into multiple
# subarrays value error if array size is not divisible by sections provided
split1 = np.array([0, 1, 2, 3, 4, 5])
print("splitting in eqaul parts :", np.split(split1, 3))
# split before 2nd and 5th indices
print("splitting at specific indices :\n", np.split(split1, [2, 5]))

split_row_2d = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])
print("Split along rows in 2d :\n", np.split(split_row_2d, 3, axis=0))
print("Split along columns in 2d :\n", np.split(split_row_2d, 3, axis=1))


# expand_dim(), used to add new dimention(or axis) to an array
# axis=0, expand at begining
# axis=1, expand at the end
expand_1d = np.array([1, 2, 3])
print("Expand 1d in 2d axis=0:\n", np.expand_dims(expand_1d, axis=0))
print("Expand 1d in 2d axis=1:\n", np.expand_dims(expand_1d, axis=1))
expand_2d = np.array([[1, 2],
                      [2, 4]])
print("Expand 2d to 3d axis=0:\n", np.expand_dims(expand_2d, axis=0))
print("Expand 2d to 3d axis=1:\n", np.expand_dims(expand_2d, axis=1))


# numpy.squeeze() is a function in the NumPy library used to remove
# single-dimensional entries (axes) from the shape of an array
sq1 = np.array([[[[5]], [[6]]]])
print("Shape before squeezing sq1:", sq1.shape)
print("After squezing sq1 :", np.squeeze(sq1))
result = np.squeeze(sq1)
print("Shape after squezing sq1:", result.shape)
