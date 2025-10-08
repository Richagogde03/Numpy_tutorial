import numpy as np
import random

# HW
# numbers = np.random.randint(0, 10, size=(2, 9, 2))
numbers = np.random.randint(0, 10, size=(4, 4))
print(numbers)
reshaped = numbers.reshape(2, 4, 2)
print(reshaped)
even_num = numbers[numbers % 2 == 0]
print(even_num)


# INDEXING, SLICING and MASKING
# Fancy indexing (using integer array)
arr = np.array([10, 20, 30, 40, 50, 60])
indices = np.array([0, 2, 5])
selected_elements = arr[indices]
print("Elements using indices :\n", selected_elements)

# fancy indexing using 2d array
matrix1 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
selected_rows = matrix1[[0, 2]]
print("Selected rows :\n", selected_rows)
specific_ele_row = matrix1[0:2, 1:2]
print("Selected elements of rows :\n", specific_ele_row)
ele_row1 = matrix1[0:3, 1:3]
print("ele row1 :", ele_row1)
ele_row2 = matrix1[:3, :3]
print("ele_row2 :", ele_row2)


# boolean Masking
arr_mask = np.array([1, 5, 2, 8, 3, 9, 4, 7])
mask1 = arr_mask > 4
print("arr using mask1 :\n", arr_mask[mask1])
mask2 = arr_mask < 7
print("arr using mask2 :\n", arr_mask[mask2])


# combining boolean masking with logical operators (fancy indexing)
logical_masking = np.array([9, 20, 13, 1, 2, 6, 8, 27, 16])
combined_mask_and = (logical_masking > 4) & (logical_masking < 7)
print(f"Combined masking and '&' : {logical_masking[combined_mask_and]}")
print(f"Combined masking and '&' : {combined_mask_and}")
combined_mask_or = (logical_masking > 4) | (logical_masking < 7)
print(f"Combined masking and '|' : {logical_masking[combined_mask_or]}")
combined_mask_neg = ~(logical_masking > 4)
print(f"Combined mask and '~' : {logical_masking[combined_mask_neg]}")


# Extracting & modifying subsets of arrays efficiently (without loops)
ext_mod = np.array([90, 45, 67, 34, 100, 35, 22, 21, 8])
subset = ext_mod[2:6]
print("subset of ext_mod :", subset)
# modification
ext_mod[2:7] = 99
print("Modification of ext_mod :", ext_mod)

# masking and modification
mask_mod = np.arange(0, 20, 2)
mask_mod[mask_mod > 10] = 100
print("Masking and modification :", mask_mod)

# logical operators and modification
lo_mod = np.linspace(0, 15, 6)
lo_mod[(lo_mod >= 5) & (lo_mod <= 12)] = 0
print("Logical operator and modification :", lo_mod)


# fancy indexing(integer array) and modification
fancy_mod = np.linspace(10, 30, 6)
print("Fancy_mod :", fancy_mod)
indeces = [0, 3, 4, 2]
fancy_mod[indeces] = [100, 300, 400, 200]
print("Fancy indexing and modification :", fancy_mod)
