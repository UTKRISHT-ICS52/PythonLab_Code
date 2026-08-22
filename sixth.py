# Program No. 6
# Aim: Write a program to find the smallest and largest number between two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    largest = a
    smallest = b
else:
    largest = b
    smallest = a

print("Largest number:", largest)
print("Smallest number:", smallest)