# Функция возвращает все названия сериалов для заданного жанра
def return_shows_names(shows_dict, show_genre):
    # список в котором будут содержаться все названия сериалов
    all_shows = []

    for show, genre in shows_dict.items():
        # если переданный жанр совпадает с жанром сериала
        # то добавляем название сериала в список
        if show_genre.lower() == genre.lower():
            all_shows.append(show)

    # возвращаем список сериалов
    return all_shows


# Функция возвращает средний рейтинг для сериалов из входного списка.
def return_average_shows_rating(shows_dict, shows_names_list):
    summ = 0        # сумма рейтинга
    counter = 0     # счетчик

    for show_name, show_rating in shows_dict.items():
        # если название фильма есть в переданном списке сериалов
        if show_name in shows_names_list:
            # то увеличиваем сумму рейтинга на значение рейтинга сериала
            summ += float(show_rating)
            # увеличиваем счетчик совпадений
            counter += 1

    # возвращаем средний рейтинг
    return summ / counter
