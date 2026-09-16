# Write a program to check whether a sring is palindrome or not
test_string = "Python"
cleaned_string = test_string.replace(" ", "").lower()
reversed_string = cleaned_string[::-1]
if cleaned_string == reversed_string:
    print(f'"{test_string}" is a palindrome.')
else:
    print(f'"{test_string}" is not a palindrome.') 