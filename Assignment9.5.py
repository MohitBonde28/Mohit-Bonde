#Write a program which accepts one number and check whether it is divisible by 3 and 5.
# Input: 15 
# Output: Divisible by 3 and 15.

def checkDivisibility(no):
    if no % 3 == 0 and no % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")

checkDivisibility(15)

#Output:
#Divisible by 3 and 15.