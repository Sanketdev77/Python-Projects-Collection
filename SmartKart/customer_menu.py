from os import name
from checkout import checkout
from products import products
def customer_menu():
    while True:
     print("\n----CUSTOMER MENU----")
     print("1. View Products")
     print("2. Search Products")
     print("3. Add Product to the cart")
     print("4. View Cart")
     print("5. Remove Product from the Cart")
     print("6. Billing / Checkout")
     print("7. Exit")

     cust_choice = int(input("\nEnter your choice: ").strip())

     if cust_choice == 1:
         print("\nHere is the list of all your products")
         for i in products:
             print(
                 f"Id: {i['id']}"
                 f"\nName:{i['name']}"
                 f"\nCategory:{i['category']}"
                 f"\nPrice:{i['price']}"
                 f"\nStock:{i['stock']}"
                 "\n" + "-" * 30
             )

     elif cust_choice == 2:
          search_text = input("\nEnter the Product you wanted to search: ").strip()
          search_product(search_text)
     elif cust_choice == 3:
         product_name = input("\nEnter the product you want to add to the cart: ").strip().lower()
         add_product(product_name)
     elif cust_choice == 4:
         view_cart()
     elif cust_choice == 5:
         product_name = input("\nEnter the product you want to remove from the cart: ").strip().lower()
         remove_product(product_name)
     elif cust_choice == 6:
      checkout(cart)
     elif cust_choice == 7:
          print("\nExiting the Customer Menu")
          break
     else:
         print("\nInvalid choice. Please try again.")


#Function to search for a particular product from the list
def search_product(search_text):
    found = False
    for product in products:
      if search_text.lower() in product['name'].lower():
        found = True
        print(
                f"Id: {product['id']}"
                f"\nName:{product['name']}"
                f"\nCategory:{product['category']}"
                f"\nPrice:{product['price']}"
                f"\nStock:{product['stock']}"
                    )
    if not found:
       print("\nNo product found.")

#Cart to store the products selected by the customer (empty list)
cart=[] #product will be appended here in the list

def add_product(product_name):

        #To find the product by name
        find_product = lambda product : product['name'].lower() == product_name.lower()

        selected_product = next((product for product in products if find_product(product)),None)

        if selected_product is None:
            print("\nProduct not found.")
        # elif selected_product['stock']<=0:
        #  print("\nProduct not found.")
        else:
           # Reduce stock by 1
          # selected_product['stock'] -= 1
           # Add Product to the cart
           cart.append(selected_product)
           print(f"\n{selected_product['name']} added to your cart.")
#function to view cart items
def view_cart():
    if not cart:
        print("\nYour cart is empty.")
    else:
     print('\nYour cart contains these products:')
     for item in cart:
         print(f"Id: {item['id']}" f"\nName: {item['name']}" f"\nPrice: {item['price']}" "\n" + "-" * 30)

#Function to remove cart items
def remove_product(product_name):
    for item in cart:
      if product_name == item['name'].lower():
          cart.remove(item)
          print(f"\n{item['name']} removed from your cart.")
          return

    print('Your cart does not contain this product')




