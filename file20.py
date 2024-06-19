# 20. Write a python program that takes a list of numbers and returns their sum
str = (input("Enter numbers separated by spaces: "))

# Split the input string by spaces and convert to integers
numbers = list(map(int,str.split()))

print("List of numbers:", numbers)

sum =0

for i in numbers:
    sum = sum+i

print("Sum of list is:",sum)








