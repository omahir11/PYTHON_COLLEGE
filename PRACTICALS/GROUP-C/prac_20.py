# c. Create a function that takes a list as input and returns the largest and smallest elements.

def find_values(lst):
    return max(lst), min(lst)

nums = [4, 8, 1, 9, 3]

largest, smallest = find_values(nums)

print("Largest:", largest)
print("Smallest:", smallest)