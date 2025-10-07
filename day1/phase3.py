import numpy as np
# slicing arrays
# slicing in 1d
arr1d = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr1d[1:5])
# print(arr1d[4::2])
# print(arr1d[:4])
# print(arr1d[-3:-1])


# slicing in 2d
arr2d = np.array([[1, 2, 3, 4, 5], 
                  [6, 7, 8, 9, 10]])
print(arr2d[1, 1:4])
print(arr2d[0:2, 2]) # 2nd element from both row
print(arr2d[0:4, 4]) # 4th element from both row
print("Entire row :", arr2d[1])
print("Entir column :", arr2d[:, 1])

# SORTING
unsorted_arr = np.array([1, 6, 9, 3, 1, 2, 3, 10, 4])
sorted_arr = np.sort(unsorted_arr)
print("Sorted array :", sorted_arr)

arr_2d_unsorted = np.array([[3, 1],
                            [1, 2],
                            [2, 3]])
# top to bottom sorting, axis=0
print("Sorted 2D array by column :\n", np.sort(arr_2d_unsorted, axis=0))
# left to right sorting, axis=1
print("Sorted 2D array by row :\n", np.sort(arr_2d_unsorted, axis=1))


# FILTERING
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even_num = numbers[numbers % 2 == 0]
print("Even numbers :", even_num)

# filter with mask
# mask, it is an expression which evaluates something
mask = numbers > 5
print("Numbers greater than 5 ", numbers[mask])


# Fancy indexing (using integer arrays)
indices = [0, 2, 4]
print(numbers[indices])
