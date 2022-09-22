# Дана последовательность состоящая из N ( от А до N) натуральных чисел. Вывести на экран все простые числа из этой последовательности

def is_prime(A, N):
    prime_nums = []
    for x in range(A, N):
        primed = True
        for i in range(2, x):
            if x % i == 0:
                primed = False
                break
            
        if primed is True:
            prime_nums.append(x)
            
    return prime_nums

A = int(input('Введите начальный интервал: '))
N = int(input('Введите конечный интервал: '))

print(is_prime(A, N))