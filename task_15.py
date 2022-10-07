# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


n = int(input('Введите число: '))
a = 0
b = 1
result = [0]

for i in range(n):
    a, b = b, a + b
    result.append(a)
print(result)
new_result = result[:]
for i in range(1, len(result), 2):
    new_result[i] = -new_result[i]
new_result = new_result[::-1]
print(new_result + result)