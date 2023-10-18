from icecream import ic

class App:
    version: float = 1.0
    comment: str | None = None

a = App()
print(f"{a.comment=}")  # используя print
print(f"ic| a.comment: None")  # альтернативный вывод для сравнения
ic(a.comment)  # используя ic