import numpy as np
# CORE ARRAY OPERATIONS AND BRoADCASTING

# Element-wise operations (+, -, *, /)
# ADDITION
add_arr1 = np.array([1, 2, 3])
add_arr2 = np.array([4, 5, 6])
print("Addition using + operator :", add_arr1 + add_arr2)
print("Addition using add() operator :", np.add(add_arr1, add_arr2))
print("scalar addition :", add_arr1 + 10)

# SUBSTRACTION
sub1 = np.array([10, 8, 15])
sub2 = np.array([4, 3, 2])
print("Sub using - operator :", sub1 - sub2)
print("Sub using subtract() :", np.subtract(sub1, sub2))

# MULTIPLICATION (element wise)
mult1 = np.array([1, 2, 3])
mult2 = np.array([2, 3, 4])
print("Multiplication using * opr :", mult1 * mult2)
print("Multiplication using multiply() :", np.multiply(mult1, mult2))

# DIVIDE
div1 = np.array([10, 6, 15])
div2 = np.array([5, 3, 2])
print("Divide using / operator :", div1/div2)
print("Divide using divide() :", np.divide(div1, div2))


# Matrix operations: np.dot(), np.matmul()
# matrix multiplication using dot() (dot product)
dot1 = np.array([[1, 2], [2, 3]])
dot2 = np.array([[4, 5], [6, 7]])
print("Dot product of 2 mat using dot() :", np.dot(dot1, dot2))
dot3 = np.array([[1, 2],
                 [2, 3],
                 [4, 5]])
dot4 = np.array([[4, 5, 1],
                 [6, 7, 2]])
print("Dot product using dot() :\n", dot1.dot(dot2))

# matrix multiplication using matmul()
mat1 = np.array([[1, 2],
                 [2, 3],
                 [4, 5]])
mat2 = np.array([[4, 5, 1],
                 [6, 7, 2]])
print("Dot product using matmul() :\n", np.matmul(mat1, mat2))

# matrix multiplication using @ operator
print("dot product using @ opr :\n", mat1 @ mat2)
