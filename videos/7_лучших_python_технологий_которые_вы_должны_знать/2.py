from functools import total_ordering


@total_ordering
class Euro:

    """
    Класс должен определить один из:
    __lt__(), __le__(), __gt__(), или же __ge__()

    Кроме того, класс должен предоставить __eq__() метод
    """

    def __init__(self, value: int):
        self.__value = value

    # Оператор ==
    def __eq__(self, other):
        return self.__value == other.__value

    # Оператор >
    def __gt__(self, other):
        return self.__value > other.__value

    def hyperinflation(self):
        self.__value = 0


a = Euro(100)
b = Euro(200)

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


a.hyperinflation()
b.hyperinflation()
print(a == b)