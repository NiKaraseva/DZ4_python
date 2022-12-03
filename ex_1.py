
# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint as rnd

# k = int(input('Введите значение натуральной степени k: '))
# print(k)

def GetEquation(size):
    my_list = []
    for i in range(size + 1):
        my_list.append(rnd(0, 100))

    my_dict = {}
    for i in range(len(my_list)):
        my_dict[i] = my_list[i]

    items = list(my_dict.items())
    new_dict = {k: v for k, v in reversed(items)}
    # print(new_dict)

    equation = ''
    for key, value in new_dict.items():
        if value != 0:
            if value == 1:
                if key == 1:
                    equation += f'x + '
                elif key == 0:
                    equation += f'1'
                else:
                    equation += f'x**{key} + '
            else:
                if key == 1:
                    equation += f'{value}*x + '
                elif key == 0:
                    equation += f'{value}'
                else:
                    equation += f'{value}*x**{key} + '
    return equation + ' = 0'

# print(GetEquation(k))



