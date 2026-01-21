#Write a program that accepts one number and print that many number in reverse order. 
# Input: 5 
# Output: 5 4 3 2 1
def printReverse(n):
    for i in range(n, 0, -1):
        print(i, end=" ")

printReverse(5)

# Output: 
# 5 4 3 2 1
