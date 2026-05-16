# e. Write a program to filter even numbers from a list using filter and a lambda function.

nums = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, nums))

print(even)






# nums=[1,2,4,5,6,6,7,5,4,3,2,2,4,45]
# even=list(filter(lambda x:x%2==0,nums))
# print(even)