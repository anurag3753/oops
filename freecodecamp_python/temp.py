class Item:

    pay_rate = 0.8
    all = []
    
    def __init__(self, name : str, price : float, quantity=0):

        assert price >= 0, f"Price : {price} can not be -ve"
        assert quantity >= 0, f"Quantity : {quantity} can not be -ve"

        self.name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    @property                # It will make price attribute as read-only
    def price(self):
        return self.__price

    def increment_price(self, new_val):    # This way we are only restricting price to be updated using increment_price func
        self.__price = new_val

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        #self.price = self.price * Item.pay_rate    # BAD (Item.pay_rate)
        self.price = self.price * self.pay_rate     # GOOD Way

obj = Item("Phone",100,1)
obj.price = 120
print(obj.price)