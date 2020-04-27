# Exercise 6.1 Menu

The gourmet restaurant 'Seasons' on the Cowbridge Road campus of Bridgend College needs a new menu. The chef knows about programming and wants a computer system to manage the menu. In this assignment, we'll implement the heart of the system, the Menu class.

The exercise template comes with a `exercise.py` filess that you can use to test the menu. For the implementation of the menu, you'll have the following boilerplate code:

```python
class Menu:
    def __init__(self):
        self.meals = []

    # implement the required methods here
```

The menu object has a list as an instance variable to store the names of the dishes on the menu. The menu should provide the following methods:

- `def add_meal(self, meal)` adds a meal to the menu. If the meal is already on the list, it should not be added again.

- `def print_meals()` prints the meals.

- `def clear_menu()` clears the menu.

Once the menu is done, you can use it as follows.

```python
menu = Menu()
menu.add_meal("Tofu ratatouille")
menu.add_meal("Chilli coconut chicken")
menu.add_meal("Chilli coconut chicken")
menu.add_meal("Meatballs with mustard sauce")

menu.print_meals()
menu.clear_menu()

print()
menu.add_meal("Tomato and mozzarella salad")
menu.print_meals()
```

```plaintext
Tofu ratatouille
Chilli coconut chicken
Meatballs with mustard sauce

Tomato and mozzarella salad
```

## Adding a Meal

Implement the `def add_meal(String meal)` method, which adds a new meal to the `meals` list. If the meal you want to add is already on the list, you shouldn't add it again. The list method `contains` is handy for checking an items existence on it.

## Printing the Meals

Implement the `def print_meals()` method, which prints the meals. You can test out the program using the following example code.

```python
menu = Menu()
menu.add_meal("Tofu ratatouille")
menu.add_meal("Chilli Coconut Chicken")
menu.add_meal("Chilli Coconut Chicken")
menu.add_meal("Meatballs with mustard sauce")

menu.print_meals()
```

```plaintext
Tofu ratatouille
Chilli Coconut Chicken
Meatballs with mustard sauce
```

## Clearing the Food List

Implement the `def clear_menu()` method, which clears the menu.

Once the menu is ready, try it with the following example code.

```python
menu = Menu()
menu.add_meal("Tofu ratatouille")
menu.add_meal("Chilli Coconut Chicken")
menu.add_meal("Chilli Coconut Chicken")
menu.add_meal("Meatballs with mustard sauce")

menu.print_meals()
menu.clear_menu()

print()
menu.add_meal("Tomato and mozzarella salad")
menu.print_meals()
```

```plaintext
Tofu ratatouille
Chilli Coconut Chicken
Meatballs with mustard sauce

Tomato and mozzarella salad
```
