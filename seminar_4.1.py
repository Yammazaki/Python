# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.
# '4 1 7 -1 6 1 -10'
# min: -10
# max: 7


k = input("Введите список чисел: ").split()
print(k)
min_num = int(k[0])
max_num = int(k[0])
for i in range(len(k)):
    if int(k[i]) > max_num:
        max_num = int(k[i])
    if int(k[i]) < min_num:
        min_num = int(k[i])
print(min_num, max_num)
