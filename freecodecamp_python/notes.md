# References:
[github](https://github.com/jimdevops19/PythonOOP) <br>
[youtube](https://www.youtube.com/watch?v=Ej_02ICOIgs)

# Notes:
- `self` means we pass the object to the class as the first parameter
- We can declare syntax checking for variable inside python
- Class Attributes are accessible from the instance as well
```python
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
        pass

    def __repr__(self):
        # Used to represent your object meant for developers
        return f"Item('{self.name}', {self.price}, {self.quantity})"

t1 = Item("Phone", 5, 1000)

print(Item.pay_rate)    # Access class attribute from class
print(t1.pay_rate)      # Access class attribute from instance

Item.instantiate_from_csv()    # cls reference is passed as first argument
```
- Magic method ```__dict__```    : dict() : Internally calls this only
```python
t2 = Item("Laptop", 3, 30000)
print(Item.__dict__)    # Print all attributes for class level
print(t.__dict__)       # Print all attributes for instance level
# It is mostly used in debugging for checking all the attributes belonging to some object
```
- For class attribute used inside the class methods, it is mandatory to use ```self.class_attr``` rather than ```class_name.class_attr```
    - Suppose we need to provide 30% discount on laptop, then it is not good idea to class the class attribute. In order to achieve it, we can define instance level attribute ```pay_rate``` for Laptop. So, get it reflected correctly in Laptop, we must have defined the attribute in the using ```self.pay_rate``` in ```apply_discount``` function.

- Suppose you decide to keep your data into csv file for all the items that you have. Then the issue is how will you call this method when none of the object exists for the class : `Here we need to use the class method`

- `Decorators` in python is just a quick way to change the behavior of the functions that we will write by basically calling them just before the line where we create our function 

- READ code written in main.py
- As the project grows we may need to divide our project into multiple files. So that it became easy to manage.

# Encapsulation
- We can achieve encapsulation using `property` attribute and declaring the variable using `double underscore`
```python
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

    @property                                # property decorator will make price attribute as read-only
    def price(self):
        return self.__price

    """
    If we declare below functions then, we can set it, even though it has double underscore
    """
    # @price.setter
    # def price(self, new_val):
    #     self.__price = new_val

    def increment_price(self, new_val):    # This way we are only restricting price to be updated using increment_price func
        self.__price = new_val

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        #self.price = self.price * Item.pay_rate    # BAD (Item.pay_rate)
        self.price = self.price * self.pay_rate     # GOOD Way

obj = Item("Phone",100,1)    # However we are allowed to set it during initialization time
```
# Abstraction
- Hiding unnecessary details from user
- By keeping `double underscore` we make the method hidden from client. It makes it only accessible inside class.
- Here, see `send_mail()`, it does may steps but all those are hidden from users
```python
class Sendmail:
    def __init__(self):
        pass

    def __connect(self):
        pass

    def __prepare_body(self):
        pass

    def __send(self):
        pass

    def send_mail(self):
        """
        NOTE : for this method we did not kept __
        """
        self.__connect()
        self.__prepare_body()
        self.__send()
```
# Inheritance
- allows to reuse code across our classes

# Polymorphism
- A single function does know how to handle different kinds of objects as expected
- Ex. list function `len()`
- Best implemented using the `abstract()` classes

```python
name = "anurag"
print(len(name))    # return number of characters in string

some_list = ["some", "name"]
print(len(some_list))    # returns number of items in list
```
