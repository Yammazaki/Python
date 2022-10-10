# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

num = [1, 1, 2, 3, 4, 5, 5]
result = []

for i in num:
    count = 0
    for j in num:
        if i == j:
            count +=1
    if count == 1:
        result.append(i)
print(result)