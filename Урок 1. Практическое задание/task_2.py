"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе
без преобразования в последовательность кодов (не используя методы
encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""

WORDS = [b'class', b'function', b'method']


def check_type_and_len_elements_by_list(word_list: list):
    """Выводит в консоль типы данных и длину элементов списка"""
    for word in word_list:
        print(f'\'{word}\' имеет тип данных {type(word)} и содержит {len(word)} символов')


if __name__ == '__main__':
    check_type_and_len_elements_by_list(WORDS)
