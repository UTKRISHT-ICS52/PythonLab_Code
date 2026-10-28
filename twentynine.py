# Create two text files, copy the contents of the first file into another file, and merge the contents of both source files into a new file.

# Create the first source file
with open("file1.txt", "w") as f:
    f.write("This is the first file.\n")
    f.write("Python file handling.")

# Create the second source file
with open("file2.txt", "w") as f:
    f.write("This is the second file.\n")
    f.write("File operations in Python.")

# Copy file1 into copy.txt
with open("file1.txt", "r") as f:
    data = f.read()

with open("copy.txt", "w") as f:
    f.write(data)

# Merge file1 and file2 into merged.txt
with open("merged.txt", "w") as f:
    for filename in ["file1.txt", "file2.txt"]:
        with open(filename, "r") as source:
            f.write(source.read() + "\n")

# Display copied contents
print("Copied File Contents:")
with open("copy.txt", "r") as f:
    print(f.read())

# Display merged contents
print("Merged File Contents:")
with open("merged.txt", "r") as f:
    print(f.read())
