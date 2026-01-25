# 10. Write a lambda function which accepts three numbers and returns largest number.

largest = lambda a, b, c: a if (a > b and a > c) else (b if b > c else c)

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Displaying result
result = largest(num1, num2, num3)

print("Largest number is:", result)

# input :  Enter first number: 45
#          Enter second number: 43
#          Enter third number: 32

# Output:  Largest number is: 45