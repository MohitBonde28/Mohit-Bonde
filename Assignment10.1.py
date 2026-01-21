#Write a program which accepts one number and print multiplication table of that number. 
# Input: 4 
# Output: 4, 8, 12, 16, 20, 24, 28, 32, 36, 40.
def printTable(no):
    for i in range(1, 11):
        print(no * i, end=", ")

printTable(4)
