# Write a Python program to store student records containing roll number, name, and marks, and search for a student using their roll number.

# Store student records in a file
with open("records.txt", "w") as f:
    f.write("101,Utkrisht Patel,92\n")
    f.write("102,Rahul Sharma,85\n")
    f.write("103,Ananya Singh,90\n")

# Search using roll number
search_roll = input("Enter roll number to search: ")

found = False

with open("records.txt", "r") as f:
    for line in f:
        roll, name, marks = line.strip().split(",")

        if roll == search_roll:
            print("Student Found!")
            print("Roll Number:", roll)
            print("Name:", name)
            print("Marks:", marks)
            found = True
            break

if not found:
    print("Student record not found.")
