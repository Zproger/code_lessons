from traceback import format_exc


class Logger:
    def write_to_log(text):
        print('=' * 40)
        print(text)
        print('=' * 40)


def bad_implementation():
    """
    Риски вызова: ZeroDivisionError, ValueError, KeyboardInterrupt.

    В случае вызова любой из этих ошибок, они все отработают также, как
    и KeyboardInterrupt.
    
    Использовать Exception стоит только для сбора всех ошибок, но следует это делать
    не в самой функции, а на самом верхнем уровне, откуда эта функция вызывается.
    """

    print("bad_implementation")

    try:
        # FIXME: Нет проверки типа данных и валидации ввода пользователя
        age = int(input("Enter your age: "))
        work_experience = int(input("Enter your age: "))
        print(f"result: {age / work_experience}")
    
    # FIXME: except никогда не должен быть пустым
    except:
        print("\nПрограмма успешно завершена\n")


def good_implementation():
    print("good_implementation")

    try:
        age = int(input("Enter your age: "))
        work_experience = int(input("Enter your age: "))
        print(f"result: {age / work_experience}")
    except ZeroDivisionError:
        print(f"\nОшибка деления на 0 - [{age=} / {work_experience=}]\n")
    except ValueError:
        print(f"\nОжидается тип данных integer, передан str\n")
    except KeyboardInterrupt:
        print("\nПрограмма успешно завершена\n")



if __name__ == "__main__":
    try:
        bad_implementation()
        good_implementation()
    except Exception:
        Logger.write_to_log(format_exc())
