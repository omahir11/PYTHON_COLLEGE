# f. Write a program to generate a multiplication table for numbers from 1 to 10.

for i in range(1, 11):
    print("\nTable of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)