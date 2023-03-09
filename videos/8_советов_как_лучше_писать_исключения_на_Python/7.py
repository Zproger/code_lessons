

"""
Манипуляция стектрейсом
"""


def clown_implementation():
    try:
        a = 1 / 0
    except ZeroDivisionError as err:
        try:
            raise RuntimeError("First call") from err
        except RuntimeError as err2:
            try:
                a = [1, 2, 3]
                print(a[255])
            except IndexError as index_err:
                raise RuntimeError("Second challenge") from index_err


def easy_implementation():
    try:
        a = 1 / 0
    except ZeroDivisionError as err:
        raise RuntimeError("First call") from err


def main():
    clown_implementation()
    easy_implementation()


if __name__ == "__main__":
    main()