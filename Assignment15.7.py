# 7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings
#    having length greater than 5.

words = ["python", "java", "computer", "science", "AI", "coding", "program"]

long_words = list(filter(lambda x: len(x) > 5, words))

print("Strings with length > 5:", long_words)

# Output : Strings with length > 5: ['python', 'computer', 'science', 'coding', 'program']