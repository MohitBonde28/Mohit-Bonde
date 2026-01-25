# 3. Write a lambda function which accepts two numbers and returns maximum number.

maximum = lambda a, b: a if a > b else b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Maximum number is:", maximum(num1, num2))

# input : Enter first number: 21 
#         Enter second number: 23
# Output : Maximum number is: 23