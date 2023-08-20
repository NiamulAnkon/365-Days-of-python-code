#Product Inventory
class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def display_info(self):
    print(f"The name of the product is: {self.name} \nThe price of the product is: {self.price} \nThe quantity of the product is: {self.quantity}")


class Inventory:
  def __init__(self):
    self.inventory = Inventory
    self.product_list = []

  def add_product(self, product):
    self.product_list.append(product)

  def List_products(self):
    for product in self.product_list:
      print(f"The name of the product is: {product.name}")
      print(f"The price of the product is: {product.price}")
      print(f"The quantity of the product is: {product.quantity}")

if __name__ == "__main__":
  Inventory = Inventory()

product1 = Product("RTX 4090 Ti", 69000, 908)
product2 = Product("AMD RYZEN 9 7900x", 70000, 200)

Inventory.add_product(product1)
Inventory.add_product(product2)

print("The Product in stock is:")
Inventory.List_products()