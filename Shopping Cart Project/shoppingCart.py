# Product - name, price, stock
# customer - name, ID
# cart Items - product , quantity
#cart - cart Items
#Payment method - PayPal, credit card

from abc import ABC, abstractmethod
#Product Class
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} = {self.price} Taka. Stock left: {self.stock}"

#Customer Class
class Customer:
    def __init__(self, name, id):
        self.name = name
        self.ID = id

    def __str__(self):
        return f"{self.name} and ID = {self.ID}"

#CartItems Class
class CartItems:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity



#Class Cart
class Cart:
    def __init__(self, customer):
        self.customer = customer
        self.cart = []

    def add_to_cart(self, product, quantity):
        self.cart.append(CartItems(product, quantity))

    def calculate_total(self):
        total_price = 0

        for item in self.cart:
            total_price += item.get_total_price()
        return total_price

    def display_cart(self):
        print(f"Shopping cart of {self.customer}")
        for item in self.cart:
            print(f"{item.product} x {item.quantity} - {item.get_total_price()} Taka")
        print(f"Total: {self.calculate_total()} Taka")

#Abstract Payment Class
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using CreditCard")

class Paypal(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Paypal")



laptop = Product('Macbook M1 air', 79990, 4)
phone = Product('Iphone 16e', 71990, 2)
print(laptop)
print(phone)
customer1 = Customer('Jihan', 258)
print(customer1)
customer1_cart = Cart(customer1)
customer1_cart.add_to_cart(laptop, 2)
customer1_cart.add_to_cart(phone, 1)
customer1_cart.display_cart()
paymethod = CreditCard()
paymethod.pay(customer1_cart.calculate_total())