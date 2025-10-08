import numpy as np

# AGGREGATIONS: sum, mean, std, min, max, argmin, argmax
# Axis operations (axis=0 vs axis=1)
array = np.array([1, 2, 3, 4, 5])
print("np.sum() :", np.sum(array))
print("np.mean() :", np.mean(array))
print("np.std() standard deviation :", np.std(array))
print("np.var() :", np.var(array))
print("np.min() :", np.min(array))
print("np.max() :", np.max(array))
print("np.argmin(), index of min value :", np.argmin(array))
print("np.argmax(), index of max value :", np.argmax(array))
print("np.prod() :", np.prod(array))


# Aggregation along axis in multidimentional array
# axis = none , aggregate all elements in flattened array
# axis = 0 along columns
# axis = 0 along rows
matrix = ([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
print("Total sum :", np.sum(matrix))
print("Total sum along col axis=0:", np.sum(matrix, axis=0))
print("Toal mean along row :", np.mean(matrix, axis=1))
print("max along col :", np.max(matrix, axis=0))
