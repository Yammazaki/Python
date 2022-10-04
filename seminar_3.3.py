# 3. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# - мат. преобразования
# - библиотека time


import time
def randomaizer(repeat: int=0) -> float:
    count = 0
    num = 0.0
    for i in range(repeat):
        num = time.time() / 1000000
        print('{0:.15}'.format(num))
        count += 1
    return num
print(randomaizer())