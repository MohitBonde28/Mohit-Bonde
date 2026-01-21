#Program which accepts one number and print that many numbers starting from one. 
# Input: 5
# Output: 1, 2, 3, 4, 5.
def printNumbers(n):
    for i in range(1, n + 1):
        print(i, end=" , ")

printNumbers(5)

# Output: 
# 1, 2, 3, 4, 5.
