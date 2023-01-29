from time import perf_counter


"""
Сравнение enumerate и доступа по индексам

enumerate_example:
10 PUSH_NULL
12 LOAD_NAME                1 (enumerate)
14 LOAD_NAME                0 (numbers)
16 PRECALL                  1
20 CALL                     1
30 GET_ITER
32 FOR_ITER                 5 (to 44)
34 UNPACK_SEQUENCE          2
38 STORE_NAME               2 (index)
40 STORE_NAME               3 (num)

index_access:
44 PUSH_NULL
46 LOAD_NAME                4 (range)
48 PUSH_NULL
50 LOAD_NAME                5 (len)
52 LOAD_NAME                0 (numbers)
54 PRECALL                  1
58 CALL                     1
68 PRECALL                  1
72 CALL                     1
82 GET_ITER
84 FOR_ITER                 2 (to 90)
86 STORE_NAME               3 (num)
88 JUMP_BACKWARD            3 (to 84)
90 LOAD_CONST               2 (None)
92 RETURN_VALUE
"""


def index_access():
    temp = 0
    numbers = [num for num in range(1_000_000)]

    for num in range(len(numbers)):
        temp = numbers[num]
    print(temp)


def enumerate_example():
    temp = 0
    numbers = [num for num in range(1_000_000)]

    for index, num in enumerate(numbers):
        temp = num
    print(temp)


if __name__ == "__main__":
    start = perf_counter()
    index_access()
    print(f"time: {(perf_counter() - start):.02f}")

    start = perf_counter()
    enumerate_example()
    print(f"time: {(perf_counter() - start):.02f}")

