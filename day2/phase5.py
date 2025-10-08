import numpy as np

# UNIVERSAL FUNCTION
# arithmetic: add, substract, multiply, divide, power,
# mod, abs, negative, floor divide
array = np.array([1, 4, 9, 16, 25])
print("Square root :", np.sqrt(array))
print("Exponentials :", np.exp(array))
print("Natural logarithms :", np.log(array))
array2 = np.array([4, 6, 7, 1, 2])
print("Addition :", np.add(array, array2))
print("sin of array :", np.sin(array))
print("Comparative greater :", np.greater(array, array2))

# mathematical: sqrt, exp, log, sin, cos, tan,
# inverse trignometric fn (np.arcsin, np.arccose, np.arctan)
# hyperbolic trignometric (np.sinh, cosh, tanh)


# Comparative: greater, greater_equal, less, less_equal
# equal, not_equal
