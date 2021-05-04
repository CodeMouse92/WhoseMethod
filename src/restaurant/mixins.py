class EspressoMachineMixin:
    """Provides brew() method to create fancy coffee drinks.
    Expects class to have `self.ready` attribute of type Dict[str, List[str]]
    """

    def brew(self, order, customer):
        if order.lower() == "no":
            return
        print(f"Brewing {order} for {customer}")
        self.ready[customer].append(order)  # type: ignore


class ShortOrderKitchenMixin:
    """Provides cook() method to create food.
    Also provides brew() to provide basic coffee.
    Expects class to have `self.ready` attribute of type Dict[str, List[str]]
    """

    def cook(self, order, customer):
        print(f"Cooking {order} for {customer}")
        self.ready[customer].append(order)  # type: ignore

    def brew(self, order, customer):
        print(f"Pour drip coffee for {customer}")
        self.ready[customer].append("Coffee")  # type: ignore
