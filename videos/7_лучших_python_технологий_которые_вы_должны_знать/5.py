

def summary(a, b):
    """
    Возвращает сумму двух чисел.

    >>> [summary(x, x) for x in range(10)]
    [0, 2, 4, 6, 8, 10, 1112, 14, 16, 18]
    >>> summary(10, 20)
    30
    """

    return a + b



if __name__ == "__main__":
    import doctest
    doctest.testmod()