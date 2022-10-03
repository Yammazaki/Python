# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся через пробел в одной строкой.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# '0 2 4'
# res -> 3


num = int(input('Введите число: '))
position_one = int(input('Введите первый элемент для умножения: '))
position_two = int(input('Введите второй элемент для умножения: '))
result_one = 0
result_two = 0
result = 0

for i in range(-num, num + 1):
    if i == position_one:
        result_one = i
    if i == position_two:
        result_two = i
    result = result_one * result_two
print(result)