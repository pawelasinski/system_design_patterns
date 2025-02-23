"""Builder

`Builder`_  is a creational design pattern that simplifies the construction of complex objects
by assembling them step by step. Instead of using a single, cumbersome constructor,
it allows a more controlled and incremental way to create objects.

Why use it?
* Step-by-step construction (adds flexibility by creating objects progressively).
* Improved readability (avoids complex, overloaded constructors).
* Encapsulation (hides the details of object creation, ensuring a clean interface).
* Consistency (ensures a uniform process for assembling different object variations).

.. _Builder:
    https://refactoring.guru/design-patterns/builder

"""


# The product that we want to build step by step.
class Burger:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def __str__(self):
        return f"Burger with: {', '.join(self.ingredients)}"


# Builder's interface
class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_bun(self):
        self.burger.add_ingredient("bun")
        return self

    def add_patty(self):
        self.burger.add_ingredient("patty")
        return self

    def add_lettuce(self):
        self.burger.add_ingredient("lettuce")
        return self

    def add_cheese(self):
        self.burger.add_ingredient("cheese")
        return self

    def build(self):
        return self.burger


if __name__ == "__main__":
    builder = BurgerBuilder()

    # Building a burger with all ingredients.
    burger = builder.add_bun().add_patty().add_cheese().add_lettuce().build()
    print(burger)  # Burger with: bun, patty, cheese, lettuce

    # Building a simple burger with bun and patty.
    simple_burger = builder.add_bun().add_patty().build()
    print(simple_burger)  # Burger with: bun, patty
