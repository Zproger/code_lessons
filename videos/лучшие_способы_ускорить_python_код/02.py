import os
import shelve
from time import perf_counter
from functools import wraps


"""
Реализация кэша с локальным файлом.
После перезапуска прогресс не теряется.
"""


def memory(func):
    cache_filename = "cache"

    # Создаем файл для хранения кеша если его нет
    # FIXME: Использовать shelve опасно!
    #  это может вызвать выполнение произвольного кода.
    #  Данный пример нужен чисто для демонстрации хранения данных
    if not os.path.exists(cache_filename):
        with shelve.open(cache_filename, "c") as db:
            ...

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(*args)

        # FIXME: Заменить на безопасный и более быстрый
        # способ хранения данных
        with shelve.open(cache_filename) as db:
            try:
                return db[key]
                print("Return from cache")
            except KeyError:
                db[key] = func(*args, **kwargs)
                print("Was not in the cache")
            finally:
                return db[key]

    return wrapper


@memory
def stress_test(iter_num):
    result = 2
    for num in range(iter_num):
        result **= 2
    return result


def main():
    # Указываем сколько раз запустить функцию
    for _ in range(2):
        start = perf_counter()
        stress_test(30)
        end = perf_counter()
        print(f"stress_test: {(end - start):.07f}\n")


if __name__ == "__main__":
    main()


