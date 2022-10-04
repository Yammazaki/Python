# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['sdf134', 'dfs53', 'sdf11', '89']
# '3'
# res: 'sdf134', 'dfs53'
# *Что такое "in" в Python


def looking_for(my_list, num):
    for i in range(len(my_list)):
        if num in my_list[i]:
            print(my_list[i])
looking_for(['sdf134', 'dfs53', 'sdf11', '89'], '3')



#                  # ПАРАМЕТРЫ
# def looking_for(my_list: list=[], num: str='0') -> list:
#     res = []
#     for i in range(len(my_list)):
#         if num in my_list[i]:
#         res.append(my_list[i])
#         return res
# my_list = ['sdf0', '1123xc']
# print(looking_for(my_list=my_list))
