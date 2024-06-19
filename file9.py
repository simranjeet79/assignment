#9.Write a python program that checks if a substring is present in a given string

str = input("Enter the string:")

words_list =str.split()
print(words_list)

sub_str =input("Enter the substring:")

for i in words_list:
    if i==sub_str:
        print(f"The substring {sub_str} is present in {str}")
    else:
        print("substring is not present")
