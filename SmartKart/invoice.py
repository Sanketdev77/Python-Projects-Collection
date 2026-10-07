
# -----------------------------
# PRINT INVOICE
# -----------------------------
def display_invoice(cart, subtotal, discount, final_bill):
 print("\n" + "-" * 65)
 print(" " * 25 + "WELCOME TO SMART-KART")
 print("-" * 65)

 print(" " * 25 + "SMART-Kart Store")
 print(" " * 25 + "S-Court Building, RK Street, Lane no.01")
 print(" " * 25 + "Kalyani Nagar, Pune, Maharashtra, 411502")

 print()




 print("\n" + " " * 30 + "INVOICE")

 print("-" * 65)

 print(
    f"{'Sr no':<8}"
    f"{'Item':<20}"
    f"{'Stock':<12}"
    f"{'Price':<12}"
 )

 print("-" * 65)

# Print cart items
 for index, item in enumerate(cart, start=1):
    print(
        f"{index:<8}"
        f"{item['name']:<20}"
        f"{item['stock']:<12}"
        f"₹{item['price']:<11.2f}"
    )

 print("-" * 65)

 print(f"{'Subtotal':<45} ₹{subtotal:.2f}")
 print(f"{'Discount':<45} ₹{discount:.2f}")

 print("-" * 65)

 print(f"{'FINAL BILL AMOUNT':<45} ₹{final_bill:.2f}")

 print("-" * 65)

 print("\nThank you for shopping with SMART-Kart!")
 print("Visit Again!")

 print("-" * 65)