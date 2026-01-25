# 9. Write a lambda function which accepts two numbers and returns multiplication.

multiply = lambda a, b: a * b

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Displaying result
result = multiply(num1, num2)

print("Multiplication of two numbers is:", result)

# input : Enter first number: 32
#         Enter second number: 33
# Output: Multiplication of two numbers is: 1056