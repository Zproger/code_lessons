

"""
Поиск элемента в списке:
Мы хотим проверить наличие определенного элемента, и в случае если он найден,
мы завершаем цикл и обходим вызов else. Но если объект не найден, то else будет
вызван с сообщением: "Element not found".
"""

my_list = [1, 2, 3, 4, 5]
search_element = 6


def search_for_else():
    for element in my_list:
        if element == search_element:
            print("Element found!")
            break
    else:
        print("Element not found.")


def search_default():
    available = False
    for element in my_list:
        if element == search_element:
            available = True
            print("Element found!")
            break
    
    if not available:
        print("Element not found.")


if __name__ == "__main__":
    search_for_else()
    search_default()