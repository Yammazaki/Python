# В файле находится N натуральных чисел, записанных через пробел.
# # Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

import os

road = r'sem5.txt'
my_list = [1, 2, 3, 4, 6, 7, 8, 9]
with open(road, 'w') as file:
    file.write(str(my_list))
for i in range(1, len(my_list)):
    if my_list[i] - 1 != my_list[i-1]:
        print(my_list[i]-1)

