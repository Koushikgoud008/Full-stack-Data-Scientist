''' 1. E-Commerce Cart System** 

Scenario:

You are designing the logic for an e-commerce website. Write a program to calculate the total price of items in a user's cart. If the cart contains more than 5 items, apply 10% discount.

Requirements:

- Use a function to calculate the total price.

- Handle cases where the cart is empty.

Input Example:

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}

Expected Output:

Total Price: 54000 '''

def cart_amount(myDict):
    total_amount = 0
    if len(myDict) == 0:
        raise ValueError("Cart is Empty")
    for product in myDict:
        total_amount += myDict[product]
    if len(myDict) > 5:
        total_amount = total_amount - (total_amount * 10 / 100)
    return total_amount

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}

try:
    total = cart_amount(cart_items)
    print(f"Total Price: {int(total)}")
except ValueError as e:
    print(e)
