# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

my_list = []
for _ in range(int(input('Введите длину списка: '))):
    my_list.append(random.randint(-21, 21))
print(my_list)

num_min = int(input('Введите минимум: '))
num_max = int(input('Введите максимум: '))
res_list = []
for i in range(1, len(my_list)):
    if num_min <= my_list[i] <= num_max:
        res_list.append(i)
print(res_list)
