# Write a program to reverse a String without using split method 
test_string = "Python"
reversed_string = ""
for char in test_string:
    reversed_string = char + reversed_string
print("Original string:", test_string)
print("Reversed string:", reversed_string)
