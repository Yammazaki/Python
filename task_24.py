# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

code = input('Введите символы: ')
result = str()

i = 0
while i < len(code):
    count = 1
    while i + 1 < len(code) and code[i] == code[i + 1]:
        count = count + 1
        i += 1
    result += str(count) + code[i]
    i += 1

with open("input.txt", "w") as input:
    print(f'input data: {code}', file=input)

with open("output.txt", "w") as output:
    print(f'output data: {result}', file=output)