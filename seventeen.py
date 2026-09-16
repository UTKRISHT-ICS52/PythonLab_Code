# Write a program to find the position of character 
test_string = "Python"
char_to_find = "o"
position = test_string.find(char_to_find)
if position != -1:
    print(f'The character "{char_to_find}" is found at position {position}.')
else:
    print(f'The character "{char_to_find}" is not found in the string.')
    