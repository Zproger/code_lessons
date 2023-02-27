

def generator():
    num = 5  # возвращается при первом вызове
    while True:
        resp = (yield num)  # возвращает num и получает новое значение
        if resp:
            num = resp  # проверяем и сохраняем новое значение в num


a = generator()
print(next(a))
a.send(200)

print(next(a))
a.send(300)
print(next(a))

