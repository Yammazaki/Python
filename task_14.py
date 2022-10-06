# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите десятичное число: '))
result = str()

while num > 0:
    result = str(num % 2) + result
    num = num // 2
print(result)