"""Decorator

The `Decorator`_ pattern is a structural design pattern that allows dynamically adding new behaviors
to objects by wrapping them in wrapper classes. Instead of modifying the original object’s code,
decorators encapsulate additional functionality, providing a flexible alternative to inheritance
for extending object capabilities.

Why use it?
* Flexibility (dynamically modify object behavior without altering its code).
* Composition over inheritance (combine multiple behaviors without creating numerous subclasses).
* Open/Closed Principle (OCP) (extend functionality without modifying existing code).
* Cleaner code (encapsulates additional behaviors, reducing the complexity of class hierarchies).

.. _Decorator:
    https://refactoring.guru/design-patterns/decorator

"""


# Base component (beverage interface)
class Beverage:
    def cost(self):
        pass


# Concrete component (plain coffee)
class Coffee(Beverage):
    def cost(self):
        return 5  # Base price of coffee


# Base decorator
class BeverageDecorator(Beverage):
    def __init__(self, beverage):
        self._beverage = beverage

    def cost(self):
        return self._beverage.cost()


# Concrete decorators
class MilkDecorator(BeverageDecorator):
    def cost(self):
        return self._beverage.cost() + 1  # Adds the cost of milk


class SugarDecorator(BeverageDecorator):
    def cost(self):
        return self._beverage.cost() + 0.5  # Adds the cost of sugar


if __name__ == "__main__":
    # Plain coffee
    my_coffee = Coffee()
    print("Plain coffee: ", my_coffee.cost())

    # Coffee with milk
    my_coffee_with_milk = MilkDecorator(my_coffee)
    print("Coffee with milk: ", my_coffee_with_milk.cost())

    # Coffee with milk and sugar
    my_coffee_with_milk_and_sugar = SugarDecorator(my_coffee_with_milk)
    print("Coffee with milk and sugar: ", my_coffee_with_milk_and_sugar.cost())
