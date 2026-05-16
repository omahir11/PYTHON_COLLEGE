# d. Create a program to find the sum of all even numbers between 1 and 100


total = 0

for i in range(2, 101, 2):
    total += i

print("Sum =", total)