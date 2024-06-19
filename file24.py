# 24. Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.

num1 =float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

operator = input("enter the operator:")
#operator ='+' or '-' or '/' or '*'

if operator == '+':
    print("Sum:",num1 +num2)
elif operator =='-':
    print("Subtraction:",num1-num2)
elif operator == '/':
    print("Division:",num1/num2)
elif operator == '*':
    print("Multiplication:",num1*num2)
else:
    print("Enter the valid operator")