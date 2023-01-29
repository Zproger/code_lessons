from time import perf_counter


"""
Не используем циклы для выполнения встроенных задач.
Если их можно заменить оптимизированным действием,
лучше это сделать.
"""


def cycle_example():
    result = 0
    numbers = [num for num in range(1_000_000)]

    for num in numbers:
        result += num
    print(result)


def sum_example():
    numbers = [num for num in range(1_000_000)]
    print(sum(numbers))


# Более оптимизированный вариант, нежели sum_example
def summary():
    res = sum(range(1_000_000))
    print(res)


if __name__ == "__main__":
    start = perf_counter()
    cycle_example()
    print(f"time: {(perf_counter() - start):.02f}")

    start = perf_counter()
    sum_example()
    print(f"time: {(perf_counter() - start):.02f}")

