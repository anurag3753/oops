import csv
from os import read

class Item:

    pay_rate = 0.8
    all = []
    
    def __init__(self, name : str, price : float, quantity=0):

        assert price >= 0, f"Price : {price} can not be -ve"
        assert quantity >= 0, f"Quantity : {quantity} can not be -ve"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        #self.price = self.price * Item.pay_rate    # BAD (Item.pay_rate)
        self.price = self.price * self.pay_rate     # GOOD Way

    @classmethod
    def instantiate_from_csv(cls):
        # cls reference is passed as first argument
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity= int(item.get('quantity'))
            )

    def __repr__(self):
        # Used to represent your object meant for developers
        #return f"Item('{self.name}', {self.price}, {self.quantity})"
        """
        When we do inheritance then we will come to know about the usage of below syntax.
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

class Phone(Item):
    # all = []
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        """
        Above duplication of args can be solved using the kwargs
        """
        super().__init__(name, price, quantity=quantity)

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones}"

        # Actions to execute
        """
        Parent has access to all the child, using all attributes. This way we can always compute how many 
        instances have been initiated at any point of time.
        """
        # Phone.all.append(self)



Item.instantiate_from_csv()    # cls reference is passed as first argument

phone1 = Phone("Motorola",1000,5,1)
print(phone1.calculate_total_price())