#Write a program which accept one number and print all odd number till that number.
def printOdd(no):
    for i in range(1, no + 1):
        if i % 2 != 0:
            print(i, end=" ")

printOdd(10)

#Output:
# 1 3 5 7 9
