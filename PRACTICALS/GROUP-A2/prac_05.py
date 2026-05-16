# a. Write a program to print the first n Fibonacci numbers.


n = int(input("Enter n: "))
a=0
b=1
for i in range(n):
    print(a, end=" ")
    a=b
    b=a+b
    