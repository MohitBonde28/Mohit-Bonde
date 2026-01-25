# 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all
#    elements.

from functools import reduce

numbers = [2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)

print("Product of all elements:", product)

# output : Product of all elements: 120