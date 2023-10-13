"""
Напишите программу, которая получает на вход зарплату трех членов семьи,
а затем подсчитывает среднюю зарплату и выводит ее на экран.
"""

# Количество людей в семье
number_of_people = 3


# Функция подсчета средней зарплаты
def get_middle_salary(people=1):
    salary = 0

    # Цикл в котором просим ввести зарплату членов семьи
    for i in range(people):
        while True:
            try:
                salary += int(input(f'Введите зарплату {i + 1}го члена семьи: ').strip())
                break
            except Exception:
                print('Ошибка! Зарплата должна быть указана цифрами. Пример: 35000')

    return salary / people


# Вызываю функцию
print(f'Средняя зарплата: {get_middle_salary(number_of_people)}')

