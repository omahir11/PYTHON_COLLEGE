# 12 a. Use the datetime module to: Display the current date and time.
# Compute the difference between two dates. 

from datetime import datetime

# Current date and time
now = datetime.now()

print("Current Date and Time:")
print(now)

# Difference between two dates
date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 5, 1)

difference = date2 - date1

print("\nDifference Between Dates:")
print(difference.days, "days")


# b. Write a Python program to read the contents of a text file story.txt. 
# Split the contents into words and count the frequency of each word. 
# Display the words along with their frequencies in descending order of frequency.

try:
    with open("story.txt", "r") as file:
        text = file.read().lower()
        words = text.split()
        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        # Sort by frequency
        sorted_words = sorted(frequency.items(),
                              key=lambda x: x[1],
                              reverse=True)
        print("Word Frequencies:\n")
        for word, count in sorted_words:
            print(word, ":", count)
except FileNotFoundError:
    print("story.txt file not found")