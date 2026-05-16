# c. Write a Python program to copy the contents of source.txt into destination.txt. 
# Ensure the program handles the case where source.txt does not exist,
# displaying an appropriate error message using exception handling.


try:
    source = open("source.txt", "r")

    data = source.read()

    destination = open("destination.txt", "w")
    destination.write(data)

    source.close()
    destination.close()

    print("File copied successfully")

except FileNotFoundError:
    print("source.txt does not exist")