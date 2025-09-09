'''2. Restaurant Menu Management

Scenario:

You are managing a restaurant's menu. Write a program to update the menu by adding or removing items and allow users to check if a particular item is available.

Requirements:

- Use functions for adding, removing, and checking menu items.

- Handle cases where the item to be removed does not exist.

Input Example:

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]

add_item = "Tacos"

remove_item = "Salad"

check_item = "Pizza"

Expected Output:

Updated menu: ["Pizza", "Burger", "Pasta", "Tacos"]

Availability: "Pizza is available" '''

class MenuManager:
    def __init__(self, menu):
        self.menu = menu

    def add_item(self, item):
        if item not in self.menu:
            self.menu.append(item)

    def remove_item(self, item):
        try:
            self.menu.remove(item)
        except ValueError:
            print('Item not Found')

    def check_item(self, item):
        if item in self.menu:
            return f"Availability: '{item} is available'"
        else:
            return f"Availability: '{item} is not available'"


initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"

menu_manager = MenuManager(initial_menu)
menu_manager.add_item(add_item)
menu_manager.remove_item(remove_item)

print(f"Updated menu: {menu_manager.menu}")
print(menu_manager.check_item(check_item))
