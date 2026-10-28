# Write a Python program to create a text file, write student details, append additional information, and display the complete contents.

# Create and write student details
f = open("student.txt", "w")
f.write("Roll Number: 101\n")
f.write("Name: Utkrisht Patel\n")
f.write("Course: Int. B.Tech CSE\n")
f.close()

# Append additional information
f = open("student.txt", "a")
f.write("University: GBU\n")
f.write("Year: Third Year\n")
f.close()

# Display complete contents
f = open("student.txt", "r")
print("Student Details:")
print(f.read())
f.close()
