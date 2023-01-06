from time import perf_counter
from functools import wraps


"""
Реализация кэша в памяти.
После перезапуска прогресс теряется.
"""


def memory(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Изначально (10,) поэтому делаем распаковку
        key = str(*args)

        if key not in cache:
            print("Was not in the cache")
            cache[key] = func(*args, **kwargs)
        else:
            print("Return from cache")

        return cache[key]
    return wrapper


@memory
def stress_test(iter_num):
    result = 2
    for num in range(iter_num):
        result **= 2
    return result


def main():
    # Указываем сколько раз запустить функцию
    for _ in range(3):
        start = perf_counter()
        stress_test(30)
        end = perf_counter()
        print(f"stress_test: {(end - start):.07f}\n")


if __name__ == "__main__":
    main()


