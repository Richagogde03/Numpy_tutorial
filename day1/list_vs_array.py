import numpy as np
import time

# difference between list and numpy array
list1 = [1, 2, 3]
# will double the list elements
print("Python list multiplication ", list1 * 2)

np_array = np.array([1, 2, 3])
# will double all elements of array
print("Python array multiplication", np_array * 2)


start = time.time()
py_list = [i * 2 for i in range(10000)]
print("\n List operation time:", time.time() - start)

start = time.time()
np_array = np.arange(10000) * 2
print("\n Array operation time: ", time.time() - start)
