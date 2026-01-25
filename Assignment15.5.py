# 5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce

# Sample list of numbers
numbers = [12, 45, 7, 89, 23, 56]

# Lambda function with reduce() to find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)

# Display result
print("Maximum element:", maximum)

# output : Maximum element: 89