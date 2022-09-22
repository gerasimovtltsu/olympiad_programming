'''
Требуется написать программу, определяющую наименьшее общее кратное (НОК) чисел a и b.

Входные данные
В единственной строке входного файла INPUT.TXT записаны два натуральных числа А и В через пробел, не превышающих 46340.

Выходные данные
В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — НОК чисел А и В.
'''

f1 = open("INPUT.txt", "r")
content = f1.read()

numbers = [int(s) for s in content.split() if s.isdigit()]

f1.close()

i = min(numbers[0], numbers[1])

while True:
    if i % numbers[0] == 0 and i % numbers[1] == 0:
        break
    i += 1

f2 = open("OUTPUT.txt", "w")
f2.write(str(i))
f2.close()

print(i)