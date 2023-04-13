

"""
Почему можно обойтись без for else, и почему он редко используется?
Основная причина в том, что обычно после рефакторинга, код можно сделать
намного лучше и читабельней, чем с использованием for else напрямую.
"""

my_list = [1, 2, 3, 4, 5]
search_element = 6


def search_for():
    if search_element in my_list:
        print("Element found!")
    else:
        print("Element not found.")


if __name__ == "__main__":
    search_for()