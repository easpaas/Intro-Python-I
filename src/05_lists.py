# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
print(x.append(4))

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print(x+y)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
y.pop(0) # removes 
print(x+y)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
y.insert(1,99) # insert() index# followed by value
print(x+y)

# Print the length of list x
# YOUR CODE HERE
print(len(x))
# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for i, nums in enumerate(x):
  print(f'index: {i}, nums: {nums*1000}')