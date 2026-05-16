# b. If the cost price and selling price of an item are provided 
# as input, write a program to determine whether the seller has
# made a profit or suffered a loss. Additionally, calculate and
# display the amount of profit or loss.




cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))
if sp > cp:
    print("Profit =", sp - cp)
elif cp > sp:
    print("Loss =", cp - sp)
else:
    print("No Profit No Loss")