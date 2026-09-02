# write a program to input marks of students and display the grade using an if -elif -else statement
# m >90 - O grade
# m <90 & m >80 - A grade
# m <80 & m >70 - B grade
# m <70 & m >60 - C grade
marks = int(input("Enter the student's marks: "))
if marks > 90:
    print("The student has received an O grade.")
elif marks < 90 and marks > 80:
    print("The student has received an A grade.")
elif marks < 80 and marks > 70:
    print("The student has received a B grade.")
elif marks < 70 and marks > 60:
    print("The student has received a C grade.")
else:
    print("The student has not received a valid grade.")
    