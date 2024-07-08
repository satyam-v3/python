# Write a Python program to calculate the number of days between two dates


from datetime import datetime

def days_between_dates(date1, date2):
    # Convert the date strings to datetime objects
    date1_obj = datetime.strptime(date1, "%Y-%m-%d")
    date2_obj = datetime.strptime(date2, "%Y-%m-%d")
    
    # Calculate the difference in days
    delta = abs(date2_obj - date1_obj)
    
    return delta.days

def main():
    # Input the dates from the user
    date1 = input("Enter the first date (YYYY-MM-DD): ")
    date2 = input("Enter the second date (YYYY-MM-DD): ")

    # Calculate and print the number of days between the two dates
    print("Number of days between the two dates:", days_between_dates(date1, date2))

if __name__ == "__main__":
    main()