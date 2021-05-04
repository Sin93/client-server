"""
3. Определить, какие из слов «attribute», «класс», «функция»,
«type» невозможно записать в байтовом типе.
"""

WORD_LIST = ['attribute', 'класс', 'функция', 'type']


def check_possibility_convert_to_bytes(word_list: list):
    """Проверяет возможность записать слова из списка в байтовом типе"""
    for word in word_list:
        try:
            word = bytes(word, 'ascii')
            print(f'Слово {word} можно записать в виде байтовой строки с помощью b\'\'')
        except UnicodeEncodeError:
            print(f'Слово \'{word}\' невозможно записать в виде байтовой строки с помощью b\'\'')


if __name__ == '__main__':
    check_possibility_convert_to_bytes(WORD_LIST)
