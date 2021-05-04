"""
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить
в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить
в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().

### 2. Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными.
Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря
в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

### 3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
YAML-формата.
Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим
в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла
с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import os
import csv
import json
import random
import re
import yaml

from chardet import detect
from datetime import date

PATTERNS = {
    'sys_manufacture_list': r'зготовитель системы:',
    'os_name_list': r'Название ОС:',
    'product_code_list': r'Код продукта:',
    'sys_type_list': r'ип системы:'
}

DATA_DIR = os.path.join(os.getcwd(), 'data')


def get_data():
    main_data_dict = {
        'sys_manufacture_list': [],
        'os_name_list': [],
        'product_code_list': [],
        'sys_type_list': []
    }  # изначально пишу в словарь, просто потому-что удобнее
    files = os.listdir(DATA_DIR)  # Получаем список файлов в директории
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(DATA_DIR, file), 'rb') as read_binary:
                for line in read_binary:
                    encoding = detect(line)['encoding']
                    line = line.decode(encoding)
                    for name, pattern in PATTERNS.items():
                        # проверяем каждую строку подходит ли она под один из паттернов
                        search_result = re.search(pattern, line)
                        if search_result:
                            # Разбивать строку по трём пробелам и брать последний элемент - это такое себе,
                            # если нужно, могу придумать что-нибудь получше, мне было главное сделать рабочую вариацию
                            search_result = search_result.string.split('   ')[-1].strip()
                            main_data_dict[name].append(search_result)
    data = []
    for key, value in main_data_dict.items():
        # перегоняем списки из словаря в отдельный список
        data.append(value)

    # транспонируем полученную "Матрицу"
    main_data = [[itm.pop(0) for itm in data] for _ in range(len(data[0]))]
    # добавляем заголовки в начало
    main_data.insert(0, ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'])
    return main_data


def write_to_csv():
    data = get_data()
    with open(os.path.join(DATA_DIR, 'product_data.csv'), 'w') as file:
        writer = csv.writer(file)
        for itm in data:
            writer.writerow(itm)
    print('Задание по созданию файла csv с данными о товарах - выполнено')


def get_json():
    with open(os.path.join(DATA_DIR, 'orders.json')) as file:
        try:
            return json.load(file)
        except json.decoder.JSONDecodeError:
            # если файл пустой по какой-то причине
            return {'orders': []}


def write_json(current_data):
    with open(os.path.join(DATA_DIR, 'orders.json'), 'w') as file:
        file.write(json.dumps(current_data, indent=4))


def create_order():
    # Проверяем существует ли такой файл, если нет, то базовый словарь берём {'orders': []}
    if os.path.exists(os.path.join(DATA_DIR, 'orders.json')):
        current_data = get_json()
    else:
        current_data = {'orders': []}

    # Генерация случайных данных
    current_data['orders'].append({
        'item': random.randint(1000, 9999),
        'quantity': random.randint(1, 5),
        'price': random.randint(1000, 9999),
        'buyer': random.randint(100000, 999999),
        'date': date.today().strftime('%D:%M:%Y')
    })
    write_json(current_data)


def write_yaml(data):
    with open(os.path.join(DATA_DIR, 'data.yaml'), 'w') as file:
        yaml.dump(data, file, default_flow_style=True, allow_unicode=True)


def read_yaml():
    with open(os.path.join(DATA_DIR, 'data.yaml')) as file:
        return yaml.full_load(file)


if __name__ == '__main__':
    # Задание 1
    write_to_csv()
    # Задание 2
    for _ in range(3):
        create_order()
    print('Задание по записи новых заказов в json - выполнено')
    # Задание 3
    data_for_yaml = {
        'list': ['value1', 'value2', 'value3'],
        'integer': 5,
        'dict': {'key1': 'value with €', 'key2': 'value with Ǚ'}
    }
    write_yaml(data_for_yaml)
    data_from_yaml = read_yaml()
    assert data_for_yaml == data_from_yaml  # Проверка, что начальный словарь и полученный из файла - совпадают
    print('Задание по записи и чтению YAML - выполнено')
