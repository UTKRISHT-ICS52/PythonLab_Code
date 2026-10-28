# Write a Python program to read a text file and count its total lines, words, characters, and vowels.

# Create a sample text file
with open("data.txt", "w") as f:
    f.write("Python is easy.\n")
    f.write("Python is powerful.")

# Read the file
with open("data.txt", "r") as f:
    text = f.read()

lines = text.splitlines()
words = text.split()
characters = len(text)
vowels = sum(1 for ch in text if ch.lower() in "aeiou")

print("Total Lines:", len(lines))
print("Total Words:", len(words))
print("Total Characters:", characters)
print("Total Vowels:", vowels)
