# 26.Write a program in python that checks if a string starts with a given prefix or ends with a given suffix

main_str =input("Enter the main string:")
prefix =input("Enter the prefix:")
suffix = input("Enter the suffix:")


if  main_str.startswith(prefix):
    print(f"The string starts with the prefix '{prefix}'.")
else:
    print(f"The string does not start with the prefix '{prefix}'.")

if main_str.endswith(suffix):
    print(f"The string ends with the suffix '{suffix}'.")
else:
    print(f"The string does not end with the suffix '{suffix}'.")