# WAP to enter 10 number and finnd their sum and average using for loop

# Initialize variables
sum_numbers = 0

# Input loop
for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))
    sum_numbers += num

# Calculate average
average = sum_numbers / 10

# Display results
print(f"Sum of the numbers: {sum_numbers}")
print(f"Average of the numbers: {average}")

