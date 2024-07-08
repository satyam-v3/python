# WAP to convert Decimal no. to Octal no. using print function

# Input: Decimal number
decimal_number = int(input("Enter a decimal number: "))

# Convert to octal
octal_number = oct(decimal_number)

# Remove the '0o' prefix that Python adds to octal numbers
octal_number = octal_number[2:]

# Print the octal number
print(f"The octal representation of {decimal_number} is {octal_number}.")
