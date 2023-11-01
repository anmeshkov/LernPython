"""
С помощью циклов и генераторов выведите на экран полную таблицу умножения, вместе с числами, которые
участвуют в операции, в таком виде:
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
...
"""

# Определим количество цифр
numbers = range(1, 10)

# Цикл вывода таблицы умножения
for number_a in numbers:
    for number_b in numbers:
        result = number_a * number_b
        print(f'{number_a} * {number_b} = {result}')
