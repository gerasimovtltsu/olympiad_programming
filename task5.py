# Для заданного числа N ≤ 103 вывести все его делители по одному разу
# 
# Входные данные:
# Одно число N. 1 ≤ N ≤ 103.
# 
# Выходные данные:
# В одну строку через пробел в порядке возрастания вывести все делители числа N по одному разу.
# 
# Sample Input:
# 10
# 
# Sample Output:
# 
# 1 2 5 10


def dividers(n):
    return ' '.join(str(e) for e in [x for x in range(1, n // 2 + 1) if n % x == 0] + [n])

n = int(input('Input N: '))
print(dividers(n))