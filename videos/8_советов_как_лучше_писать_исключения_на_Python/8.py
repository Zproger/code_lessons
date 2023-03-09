import sys


"""
Бонус.
Способ заглушить базовые исключения.
"""


def exception_handler(exctype, value, traceback): ...

sys.excepthook = exception_handler


a = 1 / 0
b = blablabla() + 0x10 + test_funct()

class Test:
    lambda x: ttt() - Test + sys