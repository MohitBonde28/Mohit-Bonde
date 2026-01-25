# 4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of
#    all elements.

from functools import reduce

# Sample list of numbers
numbers = [10, 20, 30, 40, 50]

# Lambda function with reduce() to add all elements
sum_all = reduce(lambda x, y: x + y, numbers)

# Display result
print("Sum of all elements:", sum_all)