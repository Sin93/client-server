"""
4. Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить обратное
преобразование (используя методы encode и decode).
"""

WORD_LIST = ['разработка', 'администрирование', 'protocol', 'standard']


def encode_elements_by_list(word_list: list) -> list:
    """Кодирует слова из списка в байты"""
    print('Слова закодированные в байты:')
    bytes_word_list = [word.encode('utf-8') for word in word_list]

    for b_word in bytes_word_list:
        print(b_word)

    return bytes_word_list


def decode_elements_by_list(word_list: list) -> list:
    """Декодирует слова из списка в utf-8"""
    print('\nСлова декодированные из байтов в utf-8')
    new_word_list = [word.decode('utf-8') for word in word_list]
    print('\n'.join(new_word_list))
    return new_word_list


if __name__ == '__main__':
    encrypted_words = encode_elements_by_list(WORD_LIST)
    decode_elements_by_list(encrypted_words)
