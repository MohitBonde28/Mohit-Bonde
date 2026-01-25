
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Using filter() with lambda to select even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Displaying result
print("Original List:", numbers)
print("List of Even Numbers:", even_numbers)