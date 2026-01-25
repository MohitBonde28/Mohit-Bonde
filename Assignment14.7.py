# 7. Write a lambda function which accepts one number and returns True if divisible by 5.

is_divisible_by_5 = lambda x: x % 5 == 0


num = int(input("Enter a number: "))


if is_divisible_by_5(num):
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")