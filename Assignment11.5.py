# Write a program which accept one number and check whether it is palindrome or not. 
# Input: 121
# Output: Palindrome
def checkPalindrome(no):
    if str(no) == str(no)[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

checkPalindrome(121)

# Output: 
# Palindrome
