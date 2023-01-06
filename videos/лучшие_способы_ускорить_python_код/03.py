from functools import cache
from time import perf_counter


"""
Внутренняя потокобезопасная реализация.

Преимущество lru_cache в том, что есть возможность
указать max_size, то есть сколько запросов
нужно кешировать.
"""


@cache
def stress_test(iter_num):
    result = 2
    for num in range(iter_num):
        result **= 2
    return result


def main():
    # Указываем сколько раз запустить функцию
    for _ in range(2):
        start = perf_counter()
        stress_test(28)
        end = perf_counter()
        print(f"stress_test: {(end - start):.07f}\n")


if __name__ == "__main__":
    main()


