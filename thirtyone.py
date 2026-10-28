# Write a Python program to check whether a file exists, read its contents if available, and handle a missing-file error.

import os

filename = input("Enter file name: ")

if os.path.exists(filename):
    try:
        with open(filename, "r") as f:
            print("File Contents:")
            print(f.read())
    except OSError as e:
        print("Error reading file:", e)
else:
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: File does not exist.")
