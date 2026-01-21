#Write a program which accepts one number and prints sum of first n natural number. 
# Input: 5 
# Output: 15
def sumnatural(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    print(total)

sumnatural(5)

# Output: 
# 15
