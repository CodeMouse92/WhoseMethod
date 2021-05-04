from collections import defaultdict
from restaurant.mixins import ShortOrderKitchenMixin, EspressoMachineMixin


class Diner(ShortOrderKitchenMixin):

    def __init__(self, establishment):
        self.establishment = establishment
        self.ready = defaultdict(lambda: [])

    def take_order(self):
        print(f"Welcome to {self.establishment}.")
        name = input("What's your name? ")
        food = input("What would you like, honey? ")
        coffee = input("You want coffee? ")
        self.brew(coffee, name)
        self.cook(food, name)

    def deliver_orders(self):
        for name, orders in self.ready.items():
            for order in orders:
                print(f"Here's your {order.lower()}, {name}.")


#class CoffeeShop(ShortOrderKitchenMixin, EspressoMachineMixin):  # wrong way
class CoffeeShop(EspressoMachineMixin, ShortOrderKitchenMixin):

    def __init__(self, establishment):
        self.establishment = establishment
        self.ready = defaultdict(lambda: [])

    def take_order(self):
        print(f"Welcome to {self.establishment}.")
        name = input("What's your name? ")
        coffee = input("What can I get started for you? ")
        food = input("Anything to eat? ")
        self.brew(coffee, name)
        self.cook(food, name)

    def deliver_orders(self):
        for name, orders in self.ready.items():
            for order in orders:
                print(f"{order.title()} for {name}!")
