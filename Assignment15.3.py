# 3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd
#    numbers.

# Sample list of numbers
numbers = [10, 15, 20, 25, 30, 35, 40, 45]

# Lambda function with filter() to get odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Display result
print("Odd Numbers:", odd_numbers)

# output : Odd Numbers: [15, 25, 35, 45]