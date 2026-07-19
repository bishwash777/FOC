from datetime import datetime
from write import save_products

def display_products(products):
    print("{:<25} {:<15} {:<10} {:<10} {:<15}".format("Product", "Brand", "Qty", "Price", "Origin"))
    print("-" * 80)
    for key, info in products.items():
        price = info["cp"] * 2
        display_name = info.get("display_name", key)
        print("{:<25} {:<15} {:<10} Rs{:<10} {:<15}".format(
            display_name, info["brand"], info["quantity"], price, info["origin"]
        ))

def sell_product(products):
    print("\nAvailable Products:")
    display_products(products)

    customer = input("Enter customer name: ")
    cart = []
    total = 0

    while True:
        pname_input = input("Enter product name (or 'done'): ").strip()
        if pname_input.lower() == "done":
            break

        matched_key = None
        for key, info in products.items():
            if info.get("display_name", key).lower() == pname_input.lower():
                matched_key = key
                break

        if matched_key is None:
            print("Product not found.")
            continue

        try:
            qty = int(input("Enter quantity to buy: "))
        except ValueError:
            print("Invalid quantity.")
            continue

        product = products[matched_key]
        free = qty // 3
        total_qty = qty + free
        if product["quantity"] < total_qty:
            print("Not enough stock.")
            continue

        price = product["cp"] * 2
        subtotal = price * qty
        total += subtotal
        product["quantity"] -= total_qty

        cart.append((product.get("display_name", matched_key), product["brand"], qty, free, price, subtotal))

    if total > 0:
        vat = total * 0.13
        grand_total = total + vat

        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"invoice_sale_{customer}_{timestamp}.txt"

        with open(filename, "w") as f:
            f.write("=== We Care Skin Care System ===\n")
            f.write(f"Customer: {customer}\nDate: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("Products Purchased:\n")
            for pname, brand, qty, free, price, subtotal in cart:
                f.write(f"{pname} ({brand}) - Qty: {qty} (+{free} free) @ Rs{price} = Rs{subtotal}\n")
            f.write(f"\nSubtotal: Rs{total:.2f}\nVAT (13%): Rs{vat:.2f}\nTotal Amount: Rs{grand_total:.2f}\n")

        print("\n---- We Care Skin Care System----")
        print(f"Customer: {customer}")
        print(f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        print("\nProducts Purchased:")
        for pname, brand, qty, free, price, subtotal in cart:
            print(f"{pname} ({brand}) - Qty: {qty} (+{free} free) @ Rs{price} = Rs{subtotal}")
        print(f"\nSubtotal: Rs{total:.2f}")
        print(f"VAT (13%): Rs{vat:.2f}")
        print(f"Total Amount: Rs{grand_total:.2f}")
        print(f"Invoice saved as: {filename}")

def restock_product(products):
    print("\nAvailable Products:")
    display_products(products)

    vendor = input("Enter vendor/supplier name: ")
    cart = []
    total = 0

    while True:
        pname_input = input("Enter product name to restock (or 'done'): ").strip()
        if pname_input.lower() == "done":
            break
        pname_lower = pname_input.lower()
        brand = input("Enter brand: ")
        try:
            qty = int(input("Enter quantity: "))
            cp = int(input("Enter cost price (Rs): "))
        except ValueError:
            print("Invalid input.")
            continue
        origin = input("Enter origin: ")

        matched_key = None
        for key, info in products.items():
            if info.get("display_name", key).lower() == pname_lower:
                matched_key = key
                break

        if matched_key:
            products[matched_key]["quantity"] += qty
            products[matched_key]["cp"] = cp
            products[matched_key]["brand"] = brand
            products[matched_key]["origin"] = origin
            products[matched_key]["display_name"] = pname_input
        else:
            products[pname_lower] = {
                "display_name": pname_input,
                "brand": brand,
                "quantity": qty,
                "cp": cp,
                "origin": origin
            }

        subtotal = qty * cp
        total += subtotal
        cart.append((pname_input, brand, qty, cp, subtotal))

    if total > 0:
        vat = total * 0.13
        grand_total = total + vat

        now = datetime.now()
        timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')
        filename = f"invoice_restock_{vendor}_{timestamp}.txt"

        with open(filename, "w") as f:
            f.write("---- We Care Skin Care System ----\n")
            f.write(f"Vendor: {vendor}\nDate: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("Products Restocked:\n")
            for pname, brand, qty, cp, subtotal in cart:
                f.write(f"{pname} ({brand}) - Qty: {qty} @ Rs{cp} = Rs{subtotal}\n")
            f.write(f"\nSubtotal: Rs{total:.2f}\nVAT (13%): Rs{vat:.2f}\nTotal Cost: Rs{grand_total:.2f}\n")

        print("\n--- We Care Skin Care System ----")
        print(f"Vendor: {vendor}")
        print(f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        print("\nProducts Restocked:")
        for pname, brand, qty, cp, subtotal in cart:
            print(f"{pname} ({brand}) - Qty: {qty} @ Rs{cp} = Rs{subtotal}")
        print(f"\nSubtotal: Rs{total:.2f}")
        print(f"VAT (13%): Rs{vat:.2f}")
        print(f"Total Cost: Rs{grand_total:.2f}")
        print(f"Invoice saved as: {filename}")

        #  Auto-save after restock
        save_products(products)
