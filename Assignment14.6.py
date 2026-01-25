# 6. Write a lambda function which accepts one number and returns True if number is odd
# otherwise False. 

is_odd = lambda x: x % 2 != 0

# Taking input from user
num = int(input("Enter a number: "))

# Displaying result
if is_odd(num):
    print("The number is Odd.")
else:
    print("The number is Even.")

