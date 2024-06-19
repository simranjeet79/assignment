# 19.Write a python program that removes all punctuation from a given string.

string =input("Enter the string")
"""
import string

punctuations = string.punctuation

no_punctuation_string = ""


for char in string:

    if char not in punctuations:
        no_punctuation_string += char
print("Updated string:",no_punctuation_string)
"""

print(string.punctuation)
