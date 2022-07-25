'''
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
элементов исходной последовательности. Посмотрели, что такое множество? Вот здесь его не используйте.
'''

from random import randint

def get_random_list () -> list:
    list_len = int(input('задай размер списка: '))
    lst = [randint(1, 5) for i in range(list_len)]
    return lst

initial_list = get_random_list()
print(initial_list)

def get_unique_list(numbers):
    unique_list = []
    for i in numbers:
        if i in unique_list:
            continue
        else:
            unique_list.append(i)
    return unique_list
print(get_unique_list(initial_list))