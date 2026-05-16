# a. If the basic salary of an employee is input through the keyboard,
# and the dearness allowance is 50% of the basic salary while the house 
# rent allowance is 20% of the basic salary, write a program to calculate 
# the employee's gross salary.


basic = float(input("Enter basic salary: "))
da = 0.5 * basic
hra = 0.2 * basic
gross = basic + da + hra
print("Gross Salary =", gross)