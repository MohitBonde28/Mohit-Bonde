#Write a program which accept one number and check whether it is perfect number or not. 
# Input: 6 
# Output: Perfect number

def perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        print("Perfect number")
    else:
        print("Not a perfect number")
perfect(6)

#Output:
#Perfect number
