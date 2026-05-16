# g. Write a function that accepts any number of arguments and returns their average.

def average(*args):
    return sum(args) / len(args)

print(average(10, 20, 30))