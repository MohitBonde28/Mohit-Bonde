# 6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum
#    element.

from functools import reduce

# Sample list of numbers
numbers = [12, 45, 7, 89, 23, 56]

# Lambda function with reduce() to find minimum
minimum = reduce(lambda x, y: x if x < y else y, numbers)

# Display result
print("Minimum element:", minimum)

# Output : minimum element : 7