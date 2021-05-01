"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
from chardet import detect

WORD_LIST = ['сетевое программирование', 'сокет', 'декоратор']

# Запись в файл в не родной кодировке, у меня по умолчанию utf-8,
# по этому принудительно задал другую
with open('test_file.txt', 'w', encoding='cp866') as write_file:
    for word in WORD_LIST:
        write_file.write(f'{word}\n')

# Читаем файл как бинарник, определяем кодировку, запоминаем содержимое файла
with open('test_file.txt', 'rb') as bynary_file:
    ENCODING = detect(bynary_file.read())['encoding']
    print(f'Кодировка файла: {ENCODING}\n')
    DATA = []
    for line in bynary_file.readlines():
        DATA.append(line.decode(ENCODING))

# переписываем файл в utf-8
with open('test_file.txt', 'w', encoding='utf-8') as write_file:
    for word in WORD_LIST:
        write_file.write(f'{word}\n')

# открываем файл в utf-8
with open('test_file.txt', 'r', encoding='utf-8') as read_file:
    print(read_file.read())
