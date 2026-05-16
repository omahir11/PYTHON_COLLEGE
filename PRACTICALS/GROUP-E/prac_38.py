# b. Write a Python program to read the contents of a text file story.txt.
# Split the contents into words and count the frequency of each word.
# Display the words along with their frequencies in descending order of frequency.


file = open("story.txt", "r")

text = file.read().lower()
file.close()

words = text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

# Sort by frequency
sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words:
    print(word, ":", count)