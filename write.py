def save_products(products):
    with open("product.txt", "w") as f:
        for key, product in products.items():
            name = product.get("display_name", key)
            brand = product["brand"]
            quantity = product["quantity"]
            cp = product["cp"]
            origin = product["origin"]
            f.write(f"{name},{brand},{quantity},{cp},{origin}\n")
