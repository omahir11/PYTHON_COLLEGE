# 16 a. Write a function to check whether a number is prime using function. 
def is_prime(num):

    if num <= 1:
        return False

    for i in range(2, num):

        if num % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

if is_prime(number):
    print("Prime Number")

else:
    print("Not a Prime Number")

# b. Use a lambda function to calculate the square of a number.

square = lambda x: x * x
num = int(input("Enter a number: "))
print("Square =", square(num))

# c. If the marks obtained by a student in five different subjects are input 
# through the keyboard, write a program to calculate the aggregate marks and the percentage 
# of marks obtained by the student. Assume that the maximum marks for each subject is 100
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))
aggregate = m1 + m2 + m3 + m4 + m5
percentage = aggregate / 5
print("Aggregate Marks =", aggregate)
print("Percentage =", percentage, "%")