from read import load_products
from write import save_products
from operation import display_products, sell_product, restock_product

def main():
    products = load_products()
    while True:
        print("\n-- We Care Skin Care System --")
        print("1. Display Products")
        print("2. Sell Product")
        print("3. Restock Product")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            display_products(products)
        elif choice == "2":
            sell_product(products)
        elif choice == "3":
            restock_product(products)
        elif choice == "4":
            save_products(products)
            print("Data saved. Exiting.")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
