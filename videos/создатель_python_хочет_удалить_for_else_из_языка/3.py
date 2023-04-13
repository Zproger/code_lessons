

""" Проверка ввода пользователя на корректность """


def validate_user_input():
    user_input = "abc123"

    for symbol in user_input:
        if not symbol.isalpha():
            print("Input contains invalid characters.")
            break
    else:
        print("Input is valid.")


def validate_user_input_2():
    data = [1, 2, 3, 4, 5]
    for item in data:
        if item < 0 or item > 10:
            print("Invalid data detected!")
            break
    else:
        print("All data is valid.")


if __name__ == "__main__":
    validate_user_input()
    validate_user_input_2()