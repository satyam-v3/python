# WAP to check the given no is a palindrome or not using while loop

# Input number from the user
num = int(input("Enter a number: "))

# Store the original number for comparison later
original_num = num

# Initialize variables for reversing the number
reversed_num = 0

# Reverse the number using a while loop
while num > 0:
    remainder = num % 10
    reversed_num = reversed_num * 10 + remainder
    num = num // 10

# Check if the original number is equal to its reversed version
if original_num == reversed_num:
    print(f"{original_num} is a palindrome number.")
else:
    print(f"{original_num} is not a palindrome number.")

