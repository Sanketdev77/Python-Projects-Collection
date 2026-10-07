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

    subtotal = calculate_subtotal(*cart)
    total_discount = round(calculate_discount(subtotal),2)

    print(f"Total Amount - ₹{subtotal}")
    print(f"Discount Applied - ₹{total_discount}")

    final_amount = subtotal - total_discount

    print(f"Final Amount to be paid - ₹{final_amount}")




