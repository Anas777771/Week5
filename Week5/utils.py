def calculate_total(coffee_qty, tea_qty, sandwich_qty):

    coffee_price = 8.50
    tea_price = 6.00
    sandwich_price = 12.00

    total = (
        coffee_qty * coffee_price +
        tea_qty * tea_price +
        sandwich_qty * sandwich_price
    )

    return total


def print_receipt(name, coffee_qty, tea_qty, sandwich_qty, total):

    print("\n===== RECEIPT =====")

    print("Customer :", name)
    print("Coffee   :", coffee_qty)
    print("Tea      :", tea_qty)
    print("Sandwich :", sandwich_qty)

    print("---------------------")
    print(f"Total : RM {total:.2f}")