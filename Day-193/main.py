class Product:
    def __init__(self, name, category, price, quantity, expiration_date):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.expiration_date = expiration_date

class GroceryStore:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def display_inventory(self):
        print("Inventory:")
        for product in self.inventory:
            print(f"{product.name} - Category: {product.category}, Price: ${product.price}, Quantity: {product.quantity}, Exp. Date: {product.expiration_date}")

def main():
    store = GroceryStore()

    # Adding sample products
    apple = Product("Apple", "Fruit", 1.99, 50, "2023-12-31")
    bread = Product("Bread", "Bakery", 2.49, 20, "2023-12-30")
    milk = Product("Milk", "Dairy", 1.99, 30, "2023-12-25")

    store.add_product(apple)
    store.add_product(bread)
    store.add_product(milk)

    while True:
        print("\nOptions:")
        print("1. Display Inventory")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            store.display_inventory()
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
