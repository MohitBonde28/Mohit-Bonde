#Write a program which accept one number and print its factor. 
# Input: 12
# Output: 1 2 3 4 6 12
def printFactors(no):
    for i in range(1, no + 1):
        if no % i == 0:
            print(i, end=" ")

printFactors(12)

# Output: 
# 1 2 3 4 6 12

