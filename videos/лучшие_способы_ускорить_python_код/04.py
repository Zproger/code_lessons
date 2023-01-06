from functools import lru_cache
from time import perf_counter


"""
Пример с lru_cache.
В данном примере мы ограничим сохранение
в кеш до двух элементов.
"""


# FIXME: Если вызвать больше чем указано в
# maxsize, тогда ни одна функция не будет кешироваться.
# Кеширование происходит только в том случае, если вызовов
# функции было <= maxsize
@lru_cache(maxsize=2)
def stress_test(iter_num):
    result = 2
    for num in range(iter_num):
        result **= 2
    return result


def main():
    # Указываем сколько раз запустить функцию
    for _ in range(2):
        start_1 = perf_counter()
        stress_test(28)
        end_1 = perf_counter()
        print(f"stress_test_1: {(end_1 - start_1):.07f}\n")

        start_2 = perf_counter()
        stress_test(27)
        end_2 = perf_counter()
        print(f"stress_test_2: {(end_2 - start_2):.07f}\n")

if __name__ == "__main__":
    main()


