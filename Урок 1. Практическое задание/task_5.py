"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
результаты из байтовового в строковый тип на кириллице.
"""
import subprocess
import chardet


ARGS_YANDEX = ['ping', 'yandex.ru']
ARGS_YOUTUBE = ['ping', 'youtube.com']


def main(args: list, steps: int = 5):
    """Пингует указанный в args сервер и выводит step-количество строк
    stdout'а в консоль, в кодировке utf-8"""
    subprocess_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for num, line in enumerate(subprocess_ping.stdout):
        encoding = chardet.detect(line)['encoding']
        print(line.decode(encoding).encode('utf-8').decode('utf-8'))
        # в линукс процесс пинга сам не останавливается, по этому я поставил 5 шагов
        if num+1 == steps:
            subprocess_ping.kill()


if __name__ == '__main__':
    main(ARGS_YANDEX)
    main(ARGS_YOUTUBE)
