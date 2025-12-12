def add_items_to_cart():
    cart = {}

    while True:
        item = input("Enter the item. Type 'done' to finsh: ")
        if item.lower() == "done":
            break
        price = float(input("Enter the price: $"))
        cart[item] = price

    return cart


def calculate_total(cart):
    total = sum(cart.values())
    print("\nCart Summary:\n")

    for key, value in cart.items():
        print(f"Item: {key} Price: ${value:.2f}")
    print(f"Total: {total:.2f}")

    if total > 100:
        discount = total * 0.1
        final_amount = total - discount
        print(f"Discount Applied: ${discount:.2f}")
    else:
        final_amount = total

    print(f"Final Amount: {final_amount:.2f}")


cart = add_items_to_cart()
calculate_total(cart)
