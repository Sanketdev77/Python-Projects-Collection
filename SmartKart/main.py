from customer_menu import customer_menu

print("-" *45)
print("    WELCOME TO SMARTKART")
print("-" *45)

while True:
    print("\nPlease select an option:")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

     #Type casting as the input is integer
    choice=int(input("\nPlease enter your choice -"))
    if choice == 1:
        print("\nWelcome to the Customer Portal.")
        cust_name = input("\nPlease enter your name: ")
        customer_menu()
    elif choice == 2:
        print("\nWelcome to the administrator portal.")
    elif choice == 3:
        print("\nThank you for using SmartKart.")
        #Using break to terminate the loop
        break
    else:
        print("\nInvalid option selected pls try again.")


