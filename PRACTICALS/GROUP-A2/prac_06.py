# b. Write a program to display all prime numbers within a given range.
# Modify the program to count the number of prime numbers in the range.


start = int(input("Enter start: "))
end = int(input("Enter end: "))

count = 0

for num in range(start, end + 1):
    if num > 1:
        prime = True

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
                break

        if prime:
            print(num, end=" ")
            count += 1

print("\nTotal Prime Numbers =", count)