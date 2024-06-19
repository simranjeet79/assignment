# 16.Write a program in python that counts the frequency of each character in a string.

str =input("Enter the string:")
input_char =input("Enter the character:")


frequency =0
for  char in str:
    if char == input_char:
        frequency =frequency +1

print("Frequency:",frequency)


