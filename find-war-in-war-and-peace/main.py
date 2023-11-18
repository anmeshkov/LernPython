# читаем файл построчно в список file
with open('./Tolstoj-Lev-Vojna-i-mir-Kniga-1.txt', 'r') as f:
    file = f.readlines()

WORD_TO_FIND = 'война'  # искомое слово
counter = 0             # счетчик
symbols_to_remove = ',.!?'

# ищем совпадения искомого слова
for i in range(len(file)):
    # разбиваем файл на списки
    arr = file[i].split(' ')

    for word in range(len(arr)):
        # берем конкретное слово из списка и приводим его к нижнему регистру
        concurrent_word = arr[word].lower()
        # далее нужно очистить строку от спецсимволов
        for symbol in symbols_to_remove:
            concurrent_word = concurrent_word.replace(symbol, '')
        # сравниваем искомое значение со строкой которую получили
        if WORD_TO_FIND.lower() == concurrent_word:
            # в случае успеха увеличиваем счетчик
            counter += 1

# выводим сообщение в консоль с результатом
print(f'Слово "{WORD_TO_FIND}" встречается {counter} раз')