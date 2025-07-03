#encapsulation
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_summary(self):
        return f"{self.title} by {self.author}, {self.pages} pages long"
    
    def is_long(self):
        if self.pages > 300:
            return True
        else:
            return False

#state and behavior
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")
        return f"Deposited {amount}. New balance is {self.balance}"
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Your balance is insufficient to complete this transaction")
        return f"Withdrew {amount}. New balance is {self.balance}"
    

#inheritance
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    pass
class Bike(Vehicle):
    

    def start(self):
        return f"{self.year} {self.make} {self.model} is starting."