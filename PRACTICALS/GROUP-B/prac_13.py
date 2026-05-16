# b. Given a list of temperatures in Celsius, 
# use list comprehension to convert them to Fahrenheit.


celsius = [0, 20, 30, 40, 100]

fahrenheit = [(t * 9/5) + 32 for t in celsius]

print("Fahrenheit:", fahrenheit)
