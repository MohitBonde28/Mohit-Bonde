#Write a program which accepts marks and displays grade. 
# Condition: 
# Example: >= 75 -> Distinction
# >= 64 -> First Class
# >= 50 -> Second Class
# < 50 -> Fail.

marks = float(input("Enter your marks: "))

# Check grade
if marks >= 75:
    grade = "Distinction"
elif marks >= 64:
    grade = "First Class"
elif marks >= 50:
    grade = "Second Class"
else:
    grade = "Fail"

# Print grade
print("Your grade is:", grade)

#Output:
# Input: 80
# Output: Your grade is: Distinction

# Input: 70
# Output: Your grade is: First Class

# Input: 55
# Output: Your grade is: Second Class

# Input: 40
# Output: Your grade is: Fail
