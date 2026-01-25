# 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of
#each number.


numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Using map() with lambda to find squares
squares = list(map(lambda x: x ** 2, numbers))

# Displaying result
print("Original List:", numbers)
print("List of Squares:", squares)

