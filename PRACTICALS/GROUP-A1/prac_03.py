# c. If the marks obtained by a student in five different subjects
# are input through the keyboard, write a program to calculate the
# aggregate marks and the percentage of marks obtained by the student.
# Assume that the maximum marks for each subject is 100.


total = 0
for i in range(5):
    print("Of subject number ",i+1)
    marks = float(input("Enter marks : "))
    total += marks

percentage = total / 5

print("Aggregate Marks =", total)
print("Percentage =", percentage, "%")