#Write a program which accept one number and print all even numbers till that number. 
# Input: 10 
# Output: 2 4 6 8 10
def printEven(no):
    for i in range(1, no + 1):
        if i % 2 == 0:
            print(i, end=" ")

printEven(10)

# Output:
#  2 4 6 8 10
