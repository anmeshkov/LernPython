# Five Finger Death Punch - The wrong side of heaven and the righteous side of hell vol.1(2013)
# Задача: вывести музыкальный альбом в табличном виде.

import json

# open file
file = open('./ffdp.json')
music_albums = json.load(file)

CHARLENGHT = 70

for music_album in music_albums:
    # print('=' * CHARLENGHT + '\n' +
    #       f'{music_album['artist']}\n{music_album['album']}\n{music_album['year']}\n' +
    #       '=' * CHARLENGHT)

    print('=' * CHARLENGHT)
    # generate text
    text_for_artist = music_album['artist'] + (' ' * (CHARLENGHT - len(music_album['artist'])))
    text_for_album = music_album['album'] + (' ' * (CHARLENGHT - len(music_album['album'])))
    text_for_year = str(music_album['year']) + (' ' * (CHARLENGHT - len(str(music_album['year']))))

    # print text in console
    print(f'\033[3m\033[30m\033[42m{text_for_artist}\033[0m')
    print(f'\033[3m\033[30m\033[42m{text_for_album}\033[0m')
    print(f'\033[3m\033[30m\033[42m{text_for_year}\033[0m')

    print('=' * CHARLENGHT)

    # print songs
    numbers_of_song = len(music_album['songs'])
    for i in range(numbers_of_song):
        space_count = CHARLENGHT - len(music_album['songs'][i]) - 11
        print(f'| {str(i + 1).zfill(2)}. | {music_album['songs'][i]} ' + (' ' * space_count) + ' |')

        print('=' * CHARLENGHT + '\n') if (i == numbers_of_song - 1) else print('-' * CHARLENGHT)

# close file
file.close()
