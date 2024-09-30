class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Kart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"{product.name} added to the cart.")

    def remove_products(self, product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f"Product '{item.name}' removed successfully.")
                return  # Exit once the product is found and removed
        print("Product not found in the cart.")  # Only print this if the loop finishes without finding the product

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Cart items:")
            for item in self.items:
                print(item)

    def checkout(self):
        total_price = sum([item.price for item in self.items])
        print(f"Total Price: ${total_price}")
        self.items.clear()

class Store:
    def __init__(self):
        self.products = []

    def add_product_to_store(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added to the store.")

    def show_products(self):
        print("\nAvailable Products:")
        if not self.products:
            print("No products in the store.")
        else:
            for product in self.products:
                print(product)

# Create a store and some products
store1 = Store()
store1.add_product_to_store(Product("Laptop", 1000))
store1.add_product_to_store(Product("Phone", 500))
store1.add_product_to_store(Product("Headphones", 200))

# Create a cart
cart = Kart()

# Display available products in the store
store1.show_products()

# Add products to the cart
cart.add_product(Product("Laptop", 1000))
cart.add_product(Product("Phone", 500))

# View items in the cart
cart.view_cart()

# Checkout
cart.checkout()
