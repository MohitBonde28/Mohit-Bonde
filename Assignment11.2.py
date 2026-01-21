#Write a program which accept one number and print count of digit in that number. 
# Input : 7521
# Output: 4
def countDigits(no):
    count = 0
    while no > 0:
        no = no // 10
        count = count + 1
    print(count)

countDigits(7521)

# Output: 
# 4
