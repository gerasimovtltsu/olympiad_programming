# Квадратный корень
# 
# Входные данные:
# Дано натуральное число A ≤ 10^9
#
# Выходные данные:
# Выведите такое наибольшее целое число X, что X^2 ≤ A.

def square(n):
    l = 1
    r = n
    while r >= l:
        m = (r + l) // 2
        if (m ** 2 == n):
            return m
        elif m * m < n:
            l = m + 1
        else:
            r = m - 1
    return r

print(square(1))