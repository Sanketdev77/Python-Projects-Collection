from invoice import display_invoice

def checkout(cart):
    if not cart:
        print("Your cart is empty. Cannot proceed to billing.")
        return
 #Nested functions
  #Function to calculate total sum of prices of all the items
    def calculate_subtotal(*items):
        get_price = lambda item: item['price']
        subtotal = sum(map(get_price, items))
        return subtotal

 #Function calculate the total discount
    def calculate_discount(subtotal):
        total_discount = 0
        if 0< subtotal  <= 300:
            total_discount = subtotal * 0.02
        elif 300< subtotal <= 500:
            total_discount = subtotal * 0.05
        elif 500< subtotal <=2000:
            total_discount = subtotal * 0.08
        else:
            total_discount = subtotal * 0.12
        return total_discount
 #Function to calculate total final bill amount
    def calculate_finalbill(subtotal,total_discount) :
         final_amount = subtotal - total_discount
         return final_amount
#Function for payment processing
    def make_payment(amount):
        print(f"\nAmount to be paid: ₹{amount}")

        payment_method = input(
            "Choose payment method (UPI/Card/Cash): "
        ).strip().lower()

        if payment_method == "upi":
            upi_id = input("Enter UPI ID: ").strip()

            if upi_id:
                print("Processing UPI payment...")
                return True

        elif payment_method == "card":
            card_number = input("Enter card number: ").strip()

            if len(card_number) >= 4:
                print("Processing card payment...")
                return True

        elif payment_method == "cash":
            print("Cash payment selected.")
            return True

        else:
            print("Invalid payment method.")

        return False

  #Billing
    subtotal = calculate_subtotal(*cart)
    total_discount = round(calculate_discount(subtotal),2)
    final_bill = calculate_finalbill(subtotal,total_discount)
    print(f"Total Amount - ₹{subtotal}")
    print(f"Discount Applied - ₹{total_discount}")
    print(f"Final Amount to be paid - ₹{final_bill}")

 #Payment Processing status
    payment_status = make_payment(final_bill)
    if payment_status:
        print("\nPayment successful!")
        print("Order placed successfully.")
        display_invoice(cart, subtotal, total_discount, final_bill)
        cart.clear()
    else:
        print("\nPayment failed.")
        print("Order could not be placed.")