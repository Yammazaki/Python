# Пример с использованием lambda и map

my_list = [1, 2, 3, 4, 5, 6]
new_list = list(map(lambda x: x*2, my_list))
print(new_list) 

# а теперь lambda и filter

my_list = [18, -3, 5, 0, -1, 12]
new_list = list(filter(lambda x: x > 0, my_list))
print(new_list) 

# Да, знаю, что сдаю фигню, увлеклись телефонным справочником :D тут подумали
# и решили попробвать сделать через справочники