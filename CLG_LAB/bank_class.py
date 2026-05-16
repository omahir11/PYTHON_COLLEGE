class bank:
    def __init__(self):
        self.__ac_no = 0
        self.__name = ""
        self.__bal = 0

    def inputs(self):
        self.__ac_no = int(input("Enter your Account Number: "))
        self.__name = input("Enter the name of the owner: ")

        print("Enter 1 for Deposit: ")
        print("Enter 2 for Withdrawl: ")
        print("Enter 3 to exit: ")
        op = int(input("Enter your option: "))
        if op == 1:
            self.__bal = int(input("Enter the amount to deposit: "))
        if op == 2:
            wth = int(input("Enter the amount to withdraw: "))
            if (self.__bal - wth) > 0:
                self.__bal = self.bal - wth
            else:
                print("Withdrawl amount is greater than balance")
        elif op == 3:
            print("Exiting..")

        
    def acc_details(self):
        print(f"Account Number: {self.__ac_no}")
        print(f"Name of the Owner is: {self.__name}")
        print(f"Balance: {self.__bal}")

s1 = bank()
s1.inputs()
s1.acc_details()