import random


"""
Файл может быть недоступен по множеству причин, но проблема этого
кода в том, что любая ошибка работы с файлом, будет вызывать класс
Exception, что вообще не дает никакой информации о том, из-за чего
исключение произошло.

Поэтому также нельзя использовать except, но стоит передавать классы
исключений напрямую, например явно добавить SystemExit и т.д.
"""


def file_available(filename):
    return 0


def main():
    try:
        result = file_available("test.txt")
        if not result:
            raise Exception("File not available")
    except:
        raise


if __name__ == "__main__":
    main()
