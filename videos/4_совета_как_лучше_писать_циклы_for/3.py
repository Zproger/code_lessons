from time import perf_counter


"""
Сравнение zip и обычного подхода с циклами
"""


# FIXME: Есть риск выйти за пределы списка
def stupid_example():
    res = 0
    a = [num for num in range(1_000_000)]
    b = [num for num in range(1_000_000)]

    for index in range(len(a)):
        res = a[index] + b[index]
    print(res)


def zip_example():
    res = 0
    a = [num for num in range(1_000_000)]
    b = [num for num in range(1_000_000)]

    for a_val, b_val in zip(a, b):
        res = a_val + b_val
    print(res)


if __name__ == "__main__":
    start = perf_counter()
    stupid_example()
    print(f"time: {(perf_counter() - start):.02f}")

    start = perf_counter()
    zip_example()
    print(f"time: {(perf_counter() - start):.02f}")

