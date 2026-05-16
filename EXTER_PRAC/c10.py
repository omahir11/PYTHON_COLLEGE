# 10 a. Explore and use Python's built-in math module to perform the following: 
# Calculate the square root of a number. Compute the value of sine, cosine, and tangent for a given angle.

import math
number = 25
# Square root
print("Square Root =", math.sqrt(number))
angle = math.radians(45)
# Trigonometric functions
print("Sine =", math.sin(angle))
print("Cosine =", math.cos(angle))
print("Tangent =", math.tan(angle))



# b. Create a class BankAccount with the following attributes: 
# Private account_number, balance, and owner_name. Provide methods to: 
# Initialize an account with a default balance. Deposit and withdraw money
#  (with validation for sufficient funds). Display account details.

class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.__account_number = account_number
        self.__owner_name = owner_name
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount Deposited Successfully")
        else:
            print("Invalid Deposit Amount")
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")
    def display(self):
        print("\nAccount Details")
        print("Account Number:", self.__account_number)
        print("Owner Name:", self.__owner_name)
        print("Balance:", self.__balance)

account = BankAccount(1001, "Om", 5000)
account.display()
account.deposit(2000)
account.withdraw(3000)
account.display()