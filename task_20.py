# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random

A = random.randint(1, 10)
B = random.randint(1, 10)
C = random.randint(1, 10)

A1 = random.randint(1, 10)
B2 = random.randint(1, 10)
C3 = random.randint(1, 10)

k = 2

with open("mean1_Task_20.txt", "w") as mean1_Task_20:
    print(f'{A}*x^{k} + {B}*x + {C} = 0', file=mean1_Task_20)

with open("mean2_Task_20.txt", "w") as mean2_Task_20:
    print(f'{A1}*x^{k} + {B2}*x + {C3} = 0', file=mean2_Task_20)

with open("Task_20.txt", "w") as Task_20:
    print(f'{A + A1}*x^{k} + {B + B2}*x + {C + C3} = 0', file=Task_20)