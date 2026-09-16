#  Check the Anagram of two Strings 
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)

# Test the function
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "bello"))    # Output: False

