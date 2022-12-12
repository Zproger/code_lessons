import dis
import timeit


def bool_execution(value):
	return bool(value)


def not_execution(value):
	return not not value


def main():
    print("bool_execution:")
    dis.dis(bool_execution)

    print("\nnot_execution:")
    dis.dis(not_execution)


if __name__ == "__main__":
    main()

