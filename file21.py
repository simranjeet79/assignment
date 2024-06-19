# 21. Write a python program that counts the occurrences of a specific element in a list.

list =[1,2,3,4,5,6,7,8,9,1,2,2,3,5,4,1,1,1,9,7,8]

input_element =int(input("Enter the element:"))
count=0
for i in list:
    if i ==input_element:
       count =count +1

print(f"Count of {input_element} is {count}")