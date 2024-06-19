# 3.Write a python program that calculates the factorial of a given number.
num =int(input("enter a number:"))
if(num<0):
    print("Factorial is not defined for negative numbers")
elif(num==0):
    print("Factorial of 0 is 1")
else:
    factorial=1
    for i in range(1,num+1):
        factorial =factorial* i
print("Factorial:",factorial)
