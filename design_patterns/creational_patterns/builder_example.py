"""`Builder`_ is a creational design pattern that is used to create complex objects step by step.
Instead of creating an object with one large constructor, the builder allows adding parts of it
sequentially, providing control over the overall creation process.

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


# The builder's interface.
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


# The client's code.
if __name__ == "__main__":
    builder = BurgerBuilder()

    # Building a burger with all ingredients.
    burger = builder.add_bun().add_patty().add_cheese().add_lettuce().build()
    print(burger)  # Burger with: bun, patty, cheese, lettuce

    # Building a simple burger with bun and patty.
    simple_burger = builder.add_bun().add_patty().build()
    print(simple_burger)  # Burger with: bun, patty
