# Function to get customer details
def get_customer_details():
    name = input("PLEASE ENTER THE NAME           ==> ")
    phone = input("Please enter your phone number  ==> ")
    return name, phone

# Function to get the order details
def get_order(FIRST_ORDER):
    print(f"\nENTER THE {FIRST_ORDER} DETAILS ==> ")
    order = []
    item = input("Enter item name (or type 'done' to finish): ")
        
    quantity = int(input(f"Enter quantity for {item}: "))
    price_per_item = float(input(f"Enter price for {item}: "))
    order.append((item, quantity, price_per_item))
    return order

    # Function to ask for second items
def ask_for_second_items():
    second_items = []
    item = input("Enter second item name: ")
    quantity = int(input(f"Enter quantity for {item}: "))
    price_per_item = float(input(f"Enter price for {item}: "))
    second_items.append((item, quantity, price_per_item))
    
    return second_items

# Function to ask for additional items
def ask_for_additional_items():
    additional_items = []
    while True:
        item = input("\nEnter additional item name : ")
        quantity = int(input(f"Enter quantity for {item}: "))
        price_per_item = float(input(f"Enter price for {item}: "))
        additional_items.append((item, quantity, price_per_item))
        return additional_items

# Function to display the order details
def display_order(name, phone, first_order, second_order, additional_items):
    print("\nCUSTOMER'S DETAIL")
    print(f"==> NAME: {name}")
    print(f"==> PHONE: {phone}")

    total_amount = 0

    def print_order(order):
        nonlocal total_amount
        for item, quantity, price_per_item in order:
            amount = quantity * price_per_item
            total_amount += amount
            print(f"FIRST ITEM NAME : {item}")
            print(f"QUANTITY : {quantity}")
            print(f"PRICE PER ITEM : {price_per_item}")
            print(f"Amount: {amount}")
    def print_second(second_item):
        nonlocal total_amount
        for item, quantity, price_per_item in second_item:
            amount = quantity * price_per_item
            total_amount += amount
            print(f"SECOND ITEM NAME : {item}")
            print(f"QUANTITY : {quantity}")
            print(f"PRICE PER ITEM : {price_per_item}")
            print(f"Amount: {amount}")
    print("\n**FIRST ORDER DETAILS**")
    print_order(first_order)

    print("\n**SECOND ORDER DETAILS**")
    print_order(second_order)

    if additional_items:
        print("\n**ADDITIONAL ITEMS DETAILS**")
        print_order(additional_items)

    print(f"\nTotal Amount: {total_amount}")

 #Main function
def main():
    name, phone = get_customer_details()

    print("\n**FIRST ORDER**")
    first_order = get_order("FIRST ORDER")

    print("\n**SECOND ORDER**")
    second_order = get_order("SECOND ORDER")

    additional_items = []
    while True:
        more_items = input("\nWOULD YOU LIKE TO ADD SOMETHING ELSE? (yes/no): ").lower()
        if more_items == 'no':
            break
        print("\n**ADDITIONAL ORDER**")
        additional_items += ask_for_additional_items()

    display_order(name, phone, first_order, second_order, additional_items)

if __name__ == "__main__":
    main()