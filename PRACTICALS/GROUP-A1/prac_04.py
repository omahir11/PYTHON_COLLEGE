# d. If the total selling price of 10 items and the total profit
# earned on them are input through the keyboard, write a program 
# to calculate the cost price of one item.

sp = float(input("Enter total selling price of 10 items: "))
profit = float(input("Enter total profit: "))
total_cp = sp - profit
cp_one = total_cp / 10
print("Cost Price of one item =", cp_one)