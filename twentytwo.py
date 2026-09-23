# Create a lsit of dictionary where each dictionary contains a student name and marks in three subjects. calculate total percentage and results.
students = [
    {"name": "Utrkisht", "marks": [85, 90, 78]},
    {"name": "Kapil", "marks": [92, 88, 95]},
    {"name": "Ronak", "marks": [76, 84, 80]}
]
for student in students:
    total_marks = sum(student["marks"])
    percentage = (total_marks / 300) * 100  # Assuming each subject is out of 100
    result = "Pass" if percentage >= 40 else "Fail"
    
    print(f"Student: {student['name']}, Total Marks: {total_marks}, Percentage: {percentage:.2f}%, Result: {result}")
    