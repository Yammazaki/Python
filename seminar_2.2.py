# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#     *Пример:*
#     - Для n = 6: 4, 7, 10, 13, 16, 19

n = int(input('Введите число: '))
for i in range(1, n+1):
    print((3 * i + 1), end = ' ')

# n = int(input('Введите число: '))
# k = 1
# for i in range(n):
#     k = k + 3
#     print(k, end=' ')

