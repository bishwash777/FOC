def load_products():
    products = {}
    try:
        with open("product.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    name, brand, qty, cp, origin = parts
                    products[name.lower()] = {
                        "display_name": name,
                        "brand": brand,
                        "quantity": int(qty),
                        "cp": int(cp),
                        "origin": origin
                    }
    except FileNotFoundError:
        print("product.txt not found. Starting with an empty product list.")
    return products
