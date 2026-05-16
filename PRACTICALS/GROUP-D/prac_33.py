# b. Create a class BankAccount with the following attributes:
#  Private account_number, balance, and owner_name.
#  Provide methods to: Initialize an account with a default balance. 
#  Deposit and withdraw money (with validation for sufficient funds).
#  Display account details.



class BankAccount:
    def __init__(self, acc_no, owner, balance=0):
        self.__account_number = acc_no
        self.__owner_name = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account Number:", self.__account_number)
        print("Owner:", self.__owner_name)
        print("Balance:", self.__balance)

acc = BankAccount(101, "Om", 5000)

acc.deposit(1000)
acc.withdraw(2000)

acc.display()