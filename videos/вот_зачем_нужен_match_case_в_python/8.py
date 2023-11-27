
values = {"name": "Alex", "age": 17}

match values:
    case {"name": name, "age": 12 | 17 as age}:
        print(values, age, sep="|")
    case _:
        print("Ошибка")

