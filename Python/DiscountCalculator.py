def store_item_and_price():
    items = {}

    while True:
        item = input("Enter the item. Type 'done' to finsh: ")
        if item.lower() == "done":
            break

        price = float(input("Enter the price: $"))
        items[item] = price

    return items


def calculate_total_amount(items):
    total = sum(items.values())
    return total


def calculate_discount(total):
    if (total >= 50.00) and (total <= 100.00):
        discounted_total = total - (total * 0.05)
    elif total > 100.00:
        discounted_total = total - (total * 0.1)
    else:
        discounted_total = total

    return discounted_total


def main():
    items = store_item_and_price()
    total = calculate_total_amount(items)
    discounted_total = calculate_discount(total)

    print(f"Total: ${total:.2f}")
    print(f"Discounted Total: ${discounted_total:.2f}")

main()
