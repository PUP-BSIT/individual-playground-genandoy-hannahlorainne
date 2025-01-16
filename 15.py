# Genandoy Module
import os
import time

EXIT_OPTION = 0
UNSET_OPTION = -1

class OrderSystem:  
    def __init__(self):  
        self.items = []  
        self.total = 0
        self.customer = ""

    def print_header(self, title): 
        os.system('cls')
        print(title)

    def get_customer(self):
        self.print_header("Customer Profile")
        self.customer = input('Enter your name: ')
        time.sleep(2)
        print('--Customer profile saved successfully!--')

    def add_item(self):
        self.print_header("Add Item Section")
        name = input("Item name: ")
        price = float(input(f"Enter the price of {name}: ₱"))
        qty = int(input(f"Enter the quantity of {name}: "))

        for item in self.items:
            if item['name'] == name:
                item['qty'] += qty
                self.total += price * qty
                time.sleep(2)
                print(f"--Updated {name} with {qty} more units--")
                return

        self.items.append({'name': name, 'price': price, 'qty': qty})
        self.total += price * qty
        time.sleep(2)
        print(f"--{name} added successfully with {qty} units--")

    def remove_item(self):
        self.print_header("Remove Item Section")
        self.display_order()

        if not self.items:
            return

        try:
            choice = int(input('Enter the number of the item to remove: '))
            if 1 <= choice <= len(self.items):
                removed = self.items.pop(choice - 1)
                self.total -= removed['price'] * removed['qty']
                time.sleep(2)
                print(f"--{removed['name']} removed!--")
            else:
                print("--Invalid item number--")
        except ValueError:
            print("--Invalid input. Please enter a valid number--")

    def display_order(self):
        self.print_header("Current Order")
        if not self.items:
            print('--Your order is empty--')
            return

        print(f"{'Item':<20}{'Qty':<10}{'Price':<10}{'Total':<10}")
        print("-" * 50)

        for idx, item in enumerate(self.items, start=1):
            total_price = item['price'] * item['qty']
            print(f"{idx}. {item['name']:<15} {item['qty']:<10} "
                  f"₱{item['price']:<10.2f} ₱{total_price:.2f}")

        print("-" * 50)
        print(f"Total Order Value: ₱{self.total:.2f}")

    def update_item(self):
        self.print_header("Update Item Section")
        self.display_order()

        if not self.items:
            return

        try:
            choice = int(input('Enter the number of the item to update: '))
            if 1 <= choice <= len(self.items):
                item = self.items[choice - 1]
                new_qty = int(input(f"Enter new quantity for {item['name']}: "))
                self.total -= item['price'] * item['qty']
                item['qty'] = new_qty
                self.total += item['price'] * new_qty
                time.sleep(2)
                print(f"--{item['name']} set to {new_qty} qty--")
            else:
                print("--Invalid item number--")
        except ValueError:
            print("--Invalid input. Please enter a valid number--")

    def clear_order(self):
        self.print_header("Clear All Items")
        self.items.clear()
        self.total = 0
        time.sleep(2)
        print('--Your order has been cleared!--')

    def genandoy_menu(self):
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            self.print_header("Order System Menu")
            print(f"Customer: {self.customer or ' '}\n")
            print("1. Customer Profile")
            print("2. Add Item")
            print("3. Remove Item")
            print("4. View Order")
            print("5. Update Item")
            print("6. Clear Order")
            print(f"{EXIT_OPTION}. Exit")

            try:
                choice = int(input("\nEnter your choice: "))
            except ValueError:
                print("--Invalid input. Please enter a number--")
                input("\nPress enter to continue.")
                continue

            if choice == 1:
                self.get_customer()
            elif choice == 2:
                self.add_item()
            elif choice == 3:
                self.remove_item()
            elif choice == 4:
                self.display_order()
            elif choice == 5:
                self.update_item()
            elif choice == 6:
                self.clear_order()
            elif choice == EXIT_OPTION:
                print("Thank you for using my Order System!")
                time.sleep(2)
            else:
                print("-- Invalid input, try again --")

            if choice != EXIT_OPTION:
                input("\nPress Enter to continue.")

if __name__ == "__main__":
    os.system("cls")
    order_system = OrderSystem()
    order_system.genandoy_menu()
