# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.

import ex_1
from random import randint as rnd

k1 = int(input('Введите значение натуральной степени k для первого многочлена: '))
k2 = int(input('Введите значение натуральной степени k для второго многочлена: '))


equation_1 = ex_1.GetEquation(k1)
print(equation_1)

equation_2 = ex_1.GetEquation(k2)
print(equation_2)
#
# data1 = open('equation_1.txt', 'w')
# data1.writelines(equation_1)
# data1.close()
#
# data2 = open('equation_2.txt', 'w')
# data2.writelines(equation_2)
# data2.close()


def Divide(string):
    string = string.replace(' ','')
    string = string[:-2].split('+')

    dictionary = {}

    for item in string:
        if not ('x' in item):
            dictionary[0] = int(item)
        elif not ('**' in item):
            item = item.split('x')
            if item[0] is None:
                dictionary[1] = 1
            else:
                dictionary[1] = int(item[0][:-1])
        else:
            item = item.split('**')
            i = int(item[1])
            if item[0] is None:
                dictionary[i] = 1
            else:
                dictionary[i] = int(item[0][:-2])
    return dictionary

dict_1 = Divide(equation_1)
dict_2 = Divide(equation_2)
print(dict_1)
print(dict_2)

sum_dict = {}
for key in dict_1:
    if dict_1.get(key, False) == False:
        dict_1[key] = dict_2[key]
    elif dict_2.get(key, False) == False:
        dict_2[key] = dict_1[key]
    else:
        sum_dict[key] = dict_2[key] + dict_1[key]

print(sum_dict)







