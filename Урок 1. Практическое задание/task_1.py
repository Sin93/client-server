"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом
формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать строковые представление
в формат Unicode и также проверить тип и содержимое переменных.
"""

WORD_LIST = ['разработка', 'сокет', 'декоратор']
CODE_POINT_WORD_LIST = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
]


def check_type_elements_by_list(word_list: list):
    """Выводит в консоль типы данных элементов списка"""
    for word in word_list:
        print(f'\'{word}\' имеет тип данных {type(word)}')


if __name__ == '__main__':
    check_type_elements_by_list(WORD_LIST)
    check_type_elements_by_list(CODE_POINT_WORD_LIST)
