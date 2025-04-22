my_set = {1, 2, 3, 4, 5}
print(f"Original set: {my_set}") # Output Original set: {1, 2, 3, 4, 5}

my_set.clear()
print(f"Set after clear(): {my_set}") # Output Set after clear(): set()

shopping_cart = {"book", "pen", "notebook"}
print(f"Items in the shopping cart: {shopping_cart}")  # Output Items in the shopping cart: {'notebook', 'book', 'pen'}

# Process the order (imagine some code here)
print("Order processed!") # Output Order processed!

# Now, clear the cart for the next customer
shopping_cart.clear()
print(f"Shopping cart after clearing: {shopping_cart}") # Output Shopping cart after clearing: set()

