
values = ["user", "password"]

match values:
    case "admin" | "root" as access, password:
        print(f"Доступ: {access}, Пароль: {password}")
    case _:
        print("Необходимо войти в аккаунт root")

