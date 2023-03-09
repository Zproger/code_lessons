

"""
Иерархия вызовов исключений при наследовании
"""


class FileException(Exception): ...

class FileNotFound(FileException): ...

# FIXME: Следует наследоваться от FileException,
# так как это базовый класс, но в данном случае
# это используется для демонстрации иерархии
class FileNotAvailable(FileNotFound): ...


for error in [FileException, FileNotFound, FileNotAvailable]:
    try:
        raise error()

    # Влияет порядок, если первым указать базовый класс,
    # то обрабатываться первым делом будет именно он,
    # так как Exception подходит под любое исключение
    except FileNotAvailable:
        print("FileNotAvailable")
    except FileNotFound:
        print("FileNotFound")
    except FileException:
        print("FileException")


# output:
# FileException
# FileNotFound
# FileNotAvailable