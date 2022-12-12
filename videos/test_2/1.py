import timeit


def bool_execution(value):
    return bool(value)


def not_execution(value):
    return not not value


def compare():
    value = True
    return bool(value) == (not not value)
    

def main():
    print(f"{compare()=}")
    
    ranges = [
        10_000_000,
        20_000_000,
        30_000_000,
        40_000_000,
        50_000_000,
        100_000_000
    ]

    for iteration in ranges:
        kwargs = {
            "setup": "value=10",
            "globals": globals(),
            "number": iteration
        }

        not_result = timeit.timeit("not_execution(value)", **kwargs)
        bool_result = timeit.timeit("bool_execution(value)", **kwargs)

        print(f"[{iteration}] - {not_result=:.02f}")
        print(f"[{iteration}] - {bool_result=:.02f}\n")


if __name__ == '__main__':
    main()
