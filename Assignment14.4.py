# 4. Write a lambda function which accepts two numbers and returns minimum number.

minimum = lambda a, b: a if a < b else b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Minimum number is:", minimum(num1, num2))

# input : Enter first number: 45
#         Enter second number: 56

# Output : Minimum number is: 45