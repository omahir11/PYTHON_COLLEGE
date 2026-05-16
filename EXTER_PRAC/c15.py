# 15 a. Create a custom module named math_utils with functions for 
#     addition, subtraction, multiplication, and division.
#     Import and use these functions in another program. 

    
import math_utils
print("Addition =", math_utils.add(10, 5))
print("Subtraction =", math_utils.subtract(10, 5))
print("Multiplication =", math_utils.multiply(10, 5))
print("Division =", math_utils.divide(10, 5))
    
    
# b. Create a function that takes a list as input and returns the largest and smallest elements.

def find_largest_smallest(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    return largest, smallest
nums = [10, 25, 5, 80, 40]
largest, smallest = find_largest_smallest(nums)
print("Largest =", largest)
print("Smallest =", smallest)