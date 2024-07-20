# WAP to find the greatest of any two number

# Taking input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Finding the greatest number
if number1 > number2:
    greatest = number1
else:
    greatest = number2

# Displaying the result
print(f"The greatest number between {number1} and {number2} is {greatest}.")
