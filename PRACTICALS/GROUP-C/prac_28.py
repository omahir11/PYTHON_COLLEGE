# k. Use the random module to generate:
# a. A random integer between two numbers.
# b. A random floating-point number. 
# c. A random element from a list.

import random

# Random integer
print(random.randint(1, 100))

# Random float
print(random.random())

# Random element from list
lst = [10, 20, 30, 40]

print(random.choice(lst))