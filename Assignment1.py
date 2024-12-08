import numpy as np

# Array Creation
# 1. Create a 1D NumPy array with values from 0 to 9
array_1d = np.arange(10)
print("1D Array:", array_1d)

# 2. Create a 2D array with the following values: [123456789]
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:\n", array_2d)

# 3. Create a 3D array of shape (3, 3, 3) filled with random integers between 0 and 10
array_3d = np.random.randint(0, 10, size=(3, 3, 3))
print("3D Array:\n", array_3d)

# 4. Create a NumPy array of zeros with shape (4, 5) and another of ones with shape (3, 2)
zeros_array = np.zeros((4, 5))
ones_array = np.ones((3, 2))
print("Zeros Array:\n", zeros_array)
print("Ones Array:\n", ones_array)

# Slicing and Indexing
# 1. From the 2D array, extract:
#    o The second row
second_row = array_2d[1, :]
print("Second Row:", second_row)

#    o The third column
third_column = array_2d[:, 2]
print("Third Column:", third_column)

#    o A sub-matrix containing the values 4, 5, 7, 8
sub_matrix = array_2d[1:, :2]
print("Sub-matrix:\n", sub_matrix)

# 2. From the 3D array created earlier:
#    o Extract the first 2D "slice" (along the first axis)
first_slice = array_3d[0, :, :]
print("First 2D Slice:\n", first_slice)

#    o Extract a sub-array containing the first two rows and first two columns of the second 2D slice
sub_array = array_3d[1, :2, :2]
print("Sub-array:\n", sub_array)

# Broadcasting
# 1. Add 5 to each element of the 1D array
broadcast_addition = array_1d + 5
print("1D Array + 5:", broadcast_addition)

# 2. Multiply the 2D array by a scalar value (e.g., 2)
scaled_array = array_2d * 2
print("2D Array * 2:\n", scaled_array)

# 3. Create two arrays and add them using broadcasting
array_2d_shape = np.random.randint(1, 10, size=(3, 4))
array_1d_shape = np.random.randint(1, 10, size=(4,))
broadcast_sum = array_2d_shape + array_1d_shape
print("Broadcast Sum:\n", broadcast_sum)

# Manipulating 3D Arrays
# 1. Create a 3D array of shape (4, 4, 4) filled with random floating-point numbers between 0 and 1
array_3d_floats = np.random.random((4, 4, 4))
print("3D Array with Random Floats:\n", array_3d_floats)

# 2. Replace elements and perform operations
binary_array = np.where(array_3d_floats > 0.5, 1, 0)
print("Binary Array (Threshold 0.5):\n", binary_array)

sum_elements = binary_array.sum()
print("Sum of Elements:", sum_elements)

mean_last_axis = binary_array.mean(axis=2)
print("Mean Along Last Axis:\n", mean_last_axis)

# Reshaping
# 1. Create a 1D array with 12 elements and reshape it into a 2D array of shape (3, 4)
array_reshaped = np.arange(12).reshape((3, 4))
print("Reshaped Array:\n", array_reshaped)

# Advanced (Optional)
# A.
# 1. Compute element-wise operations
array_a = np.array([1, 2, 3, 4, 5])
array_b = np.array([5, 4, 3, 2, 1])

element_sum = array_a + array_b
element_diff = array_a - array_b
element_prod = array_a * array_b
element_div = array_a / array_b
print("Element-wise Sum:", element_sum)
print("Element-wise Difference:", element_diff)
print("Element-wise Product:", element_prod)
print("Element-wise Division:", element_div)

# 2. Compute the dot product of Array A and Array B
dot_product = np.dot(array_a, array_b)
print("Dot Product:", dot_product)

# 3. Find maximum, minimum, and mean values in the 2D array created earlier
max_value = array_2d.max()
min_value = array_2d.min()
mean_value = array_2d.mean()
print("Max Value:", max_value)
print("Min Value:", min_value)
print("Mean Value:", mean_value)

# B.
# 1. Create a 3D array of shape (2, 3, 4) with random integers
random_3d = np.random.randint(0, 10, size=(2, 3, 4))
print("3D Random Array:\n", random_3d)

# 2. Swap the first and second axes of the array
swapped_axes = np.transpose(random_3d, axes=(1, 0, 2))
print("Swapped Axes Array:\n", swapped_axes)

# 3. Flatten the array into a 1D array
flattened_array = random_3d.ravel()
print("Flattened Array:", flattened_array)
