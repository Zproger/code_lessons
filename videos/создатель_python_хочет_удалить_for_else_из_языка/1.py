

def func_for_else():
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        if num == 0:
            print("The list contains a zero.")
            break
    else:
        print("The list does not contain a zero.")


def func_while_else():
    count = 0
    while count < 5:
        print("Count is", count)
        count += 1
    else:
        print("Count reached 5.")


if __name__ == "__main__":
    func_for_else()
    func_while_else()

