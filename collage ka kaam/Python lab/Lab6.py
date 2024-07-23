# Write a python program to select the odd items from a list

# Creating a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Selecting odd items from the list
odd_numbers = [num for num in numbers if num % 2 != 0]

# Displaying the result
print(f"The odd numbers in the list are: {odd_numbers}")
