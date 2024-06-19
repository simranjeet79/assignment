# 22.Write a python program that returns the minimum and maximum values in a list of numbers.


numbers = [4, 5, 1, 3, 56]

min_value = max_value = numbers[0]

for num in numbers:
    if num < min_value:
        min_value = num
    elif num > max_value:
        max_value = num


print(f"List: {numbers}")
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
