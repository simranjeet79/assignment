# 11.Write a python program that generates the first n numbers in the Fibonacci sequence

n = int(input("Enter the number of Fibonacci numbers: "))

if n <= 0:
    print([])
elif n == 1:
    print([0])
elif n == 2:
    print([0, 1])
else:
    fibo_seq = [0, 1]
    for i in range(2, n):
        next_num = fibo_seq[-1] + fibo_seq[-2]
        fibo_seq.append(next_num)
    print(fibo_seq)
