# 8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers
#    divisible by both 3 and 5.

numbers = [10, 15, 20, 30, 45, 50, 60, 75, 90]

divisible = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))

print("Numbers divisible by 3 and 5:", divisible)

# output : Numbers divisible by 3 and 5: [15, 30, 45, 60, 75, 90]