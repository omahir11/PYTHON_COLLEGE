# f. Use reduce to compute the sum of elements in a list.

from functools import reduce

nums = [1, 2, 3, 4, 5]

total = reduce(lambda x, y: x + y, nums)

print(total)




# from functools import reduce
# nums=[223,3,43,2,424,2,3,23,23,2]
# total=reduce(lambda x,y:x+y,nums)
# print(total)