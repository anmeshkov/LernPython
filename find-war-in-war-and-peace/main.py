# читаем файл построчно в список file
with open('./Tolstoj-Lev-Vojna-i-mir-Kniga-1.txt', 'r') as f:
    file = f.readlines()


WORD_TO_FIND = 'война'  # искомое слово
counter = 0             # счетчик

# ищем совпадения искомого слова
for i in range(len(file)):
    arr = file[i].split(' ')

    for word in range(len(arr)):
        if WORD_TO_FIND.lower() == arr[word].lower():
            counter += 1

# выводим сообщение в консоль с результатом
print(f'Слово "{WORD_TO_FIND}" встречается {counter} раз')