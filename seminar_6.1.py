

# doc = input('Введите выражение: ')
# print(doc)
# # res = int(doc[0])
# # list_res = []
# operation_1 = {'*': lambda x, y: x * y, '/': lambda x, y: x / y}
# operation_2 = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
# while '*' or '/' in doc:
#     operation_1(doc)
# while '+' or '-' in doc:
#     operation_2(doc)

# print(doc)

# for i in range(len(doc)):
#     if doc[i] == '*':
#         res = res * int(doc[i+1])
#         list_res.append(res)
#     if doc[i] == '/':
#         res = res / int(doc[i+1])
#         list_res.append(res)
# print(list_res)
# for i in range(len(list_res)):
#     if doc[i] == '+':
#         res = res + int(doc[i+1])
#     if doc[i] == '-':
#         res = res - int(doc[i+1])
# print(res)

doc = input().split()
print(doc)
while ('*' in doc) or ('/' in doc):
    mult_ind = -1
    div_ind = -1
    if '*' in doc:
        mult_ind = doc.index('*')
    if '/' in doc:
        div_ind = doc.index('/')
        print(mult_ind, div_ind)
    if mult_ind < div_ind and (mult_ind != -1):
        doc = doc[:mult_ind - 1] + [float(doc[mult_ind - 1]) * float(doc[mult_ind + 1])] + doc[mult_ind + 2:]
    else:
        doc = doc[:div_ind - 1] + [float(doc[div_ind - 1]) / float(doc[div_ind + 1])] + doc[div_ind + 2:]

    while ('+' in doc) or ('-' in doc):
    sum_ind = -1
    dif_ind = -1
    if '+' in doc:
        sum_ind = doc.index('+')
    if '-' in doc:
        dif_ind = doc.index('-')
        print(sum_ind, dif_ind)
    if sum_ind < dif_ind and (sum_ind != -1):
        doc = doc[:sum_ind - 1] + [float(doc[sum_ind - 1]) * float(doc[sum_ind + 1])] + doc[sum_ind + 2:]
    else:
        doc = doc[:dif_ind - 1] + [float(doc[dif_ind - 1]) / float(doc[dif_ind + 1])] + doc[dif_ind + 2:]
    print(doc)


# doc = input().split()
# print(doc)
# # 2 + 3 * 2 - 1 + 4 / 2
# while ('*' in doc) or ('/' in doc):
#     mult_ind = -1
#     div_ind = -1
#     if '*' in doc:
#         mult_ind = doc.index('*')
#     if '/' in doc:
#         div_ind = doc.index('/')
        
#     if (mult_ind < div_ind) and (mult_ind != -1):
#         doc = doc[:mult_ind - 1] + [float(doc[mult_ind - 1]) * float(doc[mult_ind + 1])] + doc[mult_ind + 2:]
#     else:
#         doc = doc[:div_ind - 1] + [float(doc[div_ind - 1]) / float(doc[div_ind + 1])] + doc[div_ind + 2:]
        
# while ('+' in doc) or ('-' in doc):
#     sum_ind = -1
#     dif_ind = -1
#     if '+' in doc:
#         sum_ind = doc.index('+')
#     if '-' in doc:
#         dif_ind = doc.index('-')
        
#     if (sum_ind < dif_ind) and (sum_ind != -1):
#         doc = doc[:sum_ind - 1] + [float(doc[sum_ind - 1]) + float(doc[sum_ind + 1])] + doc[sum_ind + 2:]
#     else:
#         doc = doc[:dif_ind - 1] + [float(doc[dif_ind - 1]) - float(doc[dif_ind + 1])] + doc[dif_ind + 2:]
    
# print(doc)
