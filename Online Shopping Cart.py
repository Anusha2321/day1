class ShoppingCart:
    def __init__(self):
        """
        Initialize the shopping cart with an empty items dictionary.
        """
        self.items = {}

    def add_item(self, item, quantity):
        """
        Add a specified quantity of an item to the cart.
        """
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        print(f"Added {quantity} of {item} to the cart.")

    def remove_item(self, item, quantity):
        """
        Remove a specified quantity of an item from the cart.
        """
        if item in self.items:
            if self.items[item] > quantity:
                self.items[item] -= quantity
                print(f"Removed {quantity} of {item} from the cart.")
            elif self.items[item] == quantity:
                del self.items[item]
                print(f"Removed all of {item} from the cart.")
            else:
                print(f"Cannot remove {quantity} of {item}. Only {self.items[item]} in the cart.")
        else:
            print(f"{item} is not in the cart.")

    def view_cart(self):
        """
        Display all items in the cart along with their quantities.
        """
        if self.items:
            print("\nItems in your cart:")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")
        else:
            print("\nYour cart is empty.")

    def clear_cart(self):
        """
        Clear all items from the cart.
        """
        self.items.clear()
        print("Your cart has been cleared.")

# Example Usage
cart = ShoppingCart()

# Adding items to the cart
cart.add_item("Apples", 5)
cart.add_item("Bananas", 3)
cart.add_item("Apples", 2)

# Viewing cart
cart.view_cart()

# Removing items
cart.remove_item("Bananas", 2)
cart.remove_item("Apples", 7)

# Viewing cart after removal
cart.view_cart()

# Clearing the cart
cart.clear_cart()

# Viewing the cart after clearing
cart.view_cart()
