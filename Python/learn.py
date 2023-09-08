def display_menu():
    print("Welcome to the Menu")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")

while True:
    display_menu()
    
    choice = input("Enter your choice: ")

    if choice == "1":
        print("You selected Option 1")
        # Add code for Option 1 here
    elif choice == "2":
        print("You selected Option 2")
        # Add code for Option 2 here
    elif choice == "3":
        print("You selected Option 3")
        # Add code for Option 3 here
    elif choice == "4":
        print("Exiting the menu")
        break
    else:
        print("Invalid choice. Please select a valid option.")


