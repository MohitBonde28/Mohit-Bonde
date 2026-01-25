# 10.Write a lambda function using filter() which accepts a list of numbers and returns the count of even
#    numbers.

numbers = [10, 15, 20, 25, 30, 35, 40, 45]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

count_even = len(even_numbers)

print("Count of even numbers:", count_even)

# Output : Count of even numbers: 4
