import datetime as dt


DATABASE = {
    'Серега': 'Омск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
}

UTS_OFFSET = {
    'Москва': 3,
    'Омск': 6,
    'Красноярск': 7,
    'Пермь': 5,
}


def what_time(friend):
    now = datetime.datetime.now(datetime.UTC)
    city = DATABASE[friend]

    return (now + datetime.timedelta(hours=UTS_OFFSET[city])).strftime(f'У друга {friend} в городе {city} сейчас %H:%M:%S')


print('-' * 20)
print(what_time('Серега'))
