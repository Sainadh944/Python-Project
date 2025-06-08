# Hotel menu with items and prices
menu = {
    1: {"item": "Idli", "price": 30},
    2: {"item": "Dosa", "price": 50},
    3: {"item": "Poori", "price": 45},
    4: {"item": "Upma", "price": 35},
    5: {"item": "Tea", "price": 15},
    6: {"item": "Coffee", "price": 20}
}

order = []

def display_menu():
    print("\n------ HOTEL MENU ------")
    for key in menu:
        print(f"{key}. {menu[key]['item']} - ₹{menu[key]['price']}")
    print("0. Finish Order")

def take_order():
    while True:
        try:
            choice = int(input("\nEnter item number to order (0 to finish): "))
            if choice == 0:
                break
            elif choice in menu:
                qty = int(input(f"Enter quantity for {menu[choice]['item']}: "))
                order.append((menu[choice]['item'], qty, menu[choice]['price'] * qty))
                print(f"{menu[choice]['item']} x {qty} added to your order.")
            else:
                print("Invalid item number. Try again.")
        except ValueError:
            print("Please enter valid numbers.")

def show_bill():
    print("\n-------- BILL --------")
    total = 0
    for item, qty, price in order:
        print(f"{item} x {qty} = ₹{price}")
        total += price
    print("-----------------------")
    print(f"Total Amount: ₹{total}")
    print("Thank you for your order!\n")

# Main program
display_menu()
take_order()
show_bill()
