#Write a program which accepts one number and prints sum of digits.
# Input: 123 
# Output: 6
def sumOfDigits(no):
    total = 0
    while no > 0:
        total = total + (no % 10)
        no = no // 10
    print(total)

sumOfDigits(123)

# Output:
#  6
