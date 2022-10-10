# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input('Введите число: '))
result = []

while num >= 0:
    if num % 2 == 0:
        result += [2]
        num //= 2
    elif num % 3 == 0:
        result += [3]
        num //= 3 
    elif num % 5 == 0:
        result += [5]
        num //= 5 
    elif num % 7 == 0:
        result += [7]
        num //= 7
    else:
        print(result)
        break