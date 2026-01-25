# 8. Write a lambda function which accepts two numbers and returns addition.

add = lambda a, b: a + b

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Displaying result
result = add(num1, num2)

print("Addition of two numbers is:", result)

# input : Enter first number: 23
#         Enter second number: 33
# output: Addition of two numbers is: 56