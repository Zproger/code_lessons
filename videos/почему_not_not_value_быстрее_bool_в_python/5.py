import timeit


# Сравнение с возвратом значений
def test1(value):
    if bool(value):
        return bool(value)


def test2(value):
    if not not bool(value):
        return not not bool(value)


# Сравнение с возвратом но без преобразования
def test1_2(value):
    if bool(value):
        return value


def test2_2(value):
    if not not bool(value):
        return value


# Сравнение без преобразования
def test3(value):
    if value:
        return value


def test4(value):
    if not not value:
        return value


def main():
    kwargs = {
        "setup": "value=10",
        "globals": globals(),
        "number": 30_000_000
    }

    # test1 = timeit.timeit("test1(value)", **kwargs)
    # test2 = timeit.timeit("test2(value)", **kwargs)

    # print(f"{test1=:.02f}")
    # print(f"{test2=:.02f}")

    # test1_2 = timeit.timeit("test1_2(value)", **kwargs)
    # test2_2 = timeit.timeit("test2_2(value)", **kwargs)

    # print(f"{test1_2=:.02f}")
    # print(f"{test2_2=:.02f}")

    # test3 = timeit.timeit("test3(value)", **kwargs)
    # test4 = timeit.timeit("test4(value)", **kwargs)

    # print(f"{test3=:.02f}")
    # print(f"{test4=:.02f}")




if __name__ == "__main__":
    main()

