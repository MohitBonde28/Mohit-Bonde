#Program which accepts one number and prints reverse of that number. 
# Input: 123
# Output: 321
def reverseNumber(no):
    rev = 0
    while no > 0:
        rev = rev * 10 + (no % 10)  
        no = no // 10                
    print(rev)

reverseNumber(123)

# Output: 
# 321
