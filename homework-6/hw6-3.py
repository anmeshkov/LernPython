"""
Напишите программу, которая находит в текущей папке все файлы типа *.dat, поочередно считывает и выводит
на экран их содержимое.
"""

import os

DIR = '.'
file_extension = 'dat'


def print_data(file_n):
    if file_n.split('.')[-1] == file_extension:
        try:
            with open(DIR + '/' + file_n, 'r') as f:
                content = f.read()
        except Exception as e:
            print(f'Не возможно открыть файл {file_name} {e}')
        else:
            print('-' * 10 + file_n + '-' * 10)
            print(content)


dir_list_files = os.listdir(DIR)
for file_name in dir_list_files:
    # print(file_name)
    print_data(file_name)




