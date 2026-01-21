#Program which accept one number and checks whether it is prime or not. 
# Input: 11
# Output: Prime Number

def isPrime(no):
    for i in range(2, no):
        if no % i == 0:
            print("Not Prime")
            return
    print("Prime number")

isPrime(11)

# Output:
# Prime Number. 
