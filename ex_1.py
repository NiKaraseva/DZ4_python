
# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint as rnd

k = int(input('Введите значение натуральной степени k для первого многочлена: '))

def CreateEquation(size: int) -> dict:
    my_dict = {}
    for key in range(size, -1, -1):
        my_dict[key] = rnd(-100, 100)
    return my_dict


def GetEquation(equation: dict) -> str:
    new_equation = ''
    first = True
    for key, value in equation.items():
        if value != 0:
            if first:
                if value == 1:
                    new_equation += f'x '
                elif value > 1:
                    new_equation += f'{value}*x**{key} '
                elif value == -1:
                    new_equation += f'- x '
                else:
                    new_equation += f'- {value * (-1)}*x**{key} '
                first = False
            else:
                if value == 1:
                    if key == 1:
                        new_equation += f'+ x '
                    elif key == 0:
                        new_equation += f'+ 1 '
                    else:
                        new_equation += f'+ x**{key} '
                elif value > 1:
                    if key == 1:
                        new_equation += f'+ {value}*x '
                    elif key == 0:
                        new_equation += f'+ {value} '
                    else:
                        new_equation += f'+ {value}*x**{key} '
                elif value == -1:
                    if key == 1:
                        new_equation += f'- x '
                    elif key == 0:
                        new_equation += f'- 1 '
                    else:
                        new_equation += f'- x**{key} '
                elif value < 1:
                    if key == 1:
                        new_equation += f'- {abs(value)}*x '
                    elif key == 0:
                        new_equation += f'- {abs(value)} '
                    else:
                        new_equation += f'- {abs(value)}*x**{key} '

    return new_equation + '= 0'

equation_1 = GetEquation(CreateEquation(k))

# # B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# # содержащий сумму многочленов.

k2 = int(input('Введите значение натуральной степени k для второго многочлена: '))

equation_2 = GetEquation(CreateEquation(k2))

with open('equation_1.txt', 'w', encoding='UTF-8') as file:
    file.write(equation_1)

with open('equation_2.txt', 'w', encoding='UTF-8') as file:
    file.write(equation_2)

print(f'Первый многочлен = {equation_1}')
print(f'Второй многочлен = {equation_2}')


def DivideEquation(equation: str) -> dict:
    dictionary = {}
    equation = equation.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').replace('- ', '-').split(' ')
    for item in equation:
        if not ('x' in item):
            dictionary[0] = int(item)
        elif not ('**' in item):
            item = item.split('x')
            if item[0] is None:
                dictionary[1] = 1
            elif item[0] == '-':
                dictionary[1] = -1
            else:
                dictionary[1] = int(item[0][:-1])
        else:
            item = item.split('**')
            i = int(item[1])
            if item[0] == 'x':
                dictionary[i] = 1
            elif item[0] == '-x':
                dictionary[i] = -1
            else:
                dictionary[i] = int(item[0][:-2])
    return dictionary

dict_1 = DivideEquation(equation_1)
dict_2 = DivideEquation(equation_2)
print(f'Словарь из коэффициентов первого многочлена = {dict_1}')
print(f'Словарь из коэффициентов второго многочлена = {dict_2}')


def SumEquation(dictionary1: dict, dictionary2: dict) -> dict:
    for key in dictionary1:
        if dictionary2.get(key, False) == False:
            dictionary2[key] = dictionary1[key]
        else:
            dictionary2[key] += dictionary1[key]
    return dict(sorted(dictionary2.items())[::-1])

sum_dictionary = SumEquation(dict_1, dict_2)
print(f'Сумма двух словарей = {sum_dictionary}')

sum_equation = GetEquation(sum_dictionary)
print(f'Многочлен суммы = {sum_equation}')

with open('sum_equation.txt', 'w', encoding='UTF-8') as file:
    file.write(sum_equation)