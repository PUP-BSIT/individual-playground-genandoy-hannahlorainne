def display_menu():
    print("\nHELLO! My name is Hannah Lorainne Genandoy.\n")

def menu_options():
    print("--- Menu ---")
    print("1. Basic Info")
    print("2. Goals")
    print("3. Comment/Change from Teammate ?")
    print("4. Exit")

display_menu()

while True:
    menu_options()
    choice = input("Enter you're choice: ")
    
    if choice == '1':
        print("\nBasic Info:")
        print(f" - Name: Hannah Lorainne Genandoy")
        print(f" - Age: 19")
        print(f" - Birthday: April 3, 2005")
        print(f" - Program: DIT")
        print(f" - Year Level: Sophomore")
    elif choice == '2':
        print("\nGoals:")
        print(" - Graduate with a degree in Information Technology.")
        print(" - Continue learning and enhancing my technical skills.")
        print(" - Be successful, not only in my career but also in maintaining a fulfilling personal life.")
    elif choice == '3':
        print("\nComment/Change from Teammate 1:")
        print(" - Indicate your changes in this Module")
    elif choice == '4':
        print("\nThank you!")
        break
    else:
        print("\nInvalid choice. Try again.")
