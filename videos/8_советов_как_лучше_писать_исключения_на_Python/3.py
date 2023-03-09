from contextlib import suppress


# Подавление ошибок с помощью except pass
def bad_implementation(x, y):
    try:
        result = x / y
        print(f"result: {result}")
    except:
        pass


# Подавление ошибок с помощью contextlib.suppress
def good_implementation(x, y):
    with suppress(ZeroDivisionError):
        result = x / y
        print(f"result: {result}")


# Пример с подавлением нескольких исключений
def read_file_implementation(filename):
    with suppress(FileNotFoundError, PermissionError):
        with open(filename) as file:
            content_chars = len(file.read())
            print(f"File characters: {content_chars}")


if __name__ == "__main__":
    bad_implementation(10, 0)
    good_implementation(10, 0)

    read_file_implementation("2.py")
    read_file_implementation("2222.py")  # error