# 12.Write a python program that calculates the sum of the digits of a given number
num =(input("Enter a number:"))
num_str = str(num)
total = 0
for char in num_str :
    total = total + int(char)
print ("Total:",total)
