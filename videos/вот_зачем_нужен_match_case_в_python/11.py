
headers = {
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "content-type": "aadpplication/json"
}

match headers:
    case {"content-type": "application/json"}:
        print("Строка присутствует в headers")
    case other:
        print(f"Результат: {other}")
