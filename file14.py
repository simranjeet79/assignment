# 14.Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

print("Enter the text lines and for the function to end,left it empty and press enter:")

lines=[]
while True:
    line =input()
    if line == "" :
        break
    lines.append(line)
print("\nYour entered text lines are:")
for line in lines:
    print(line)


