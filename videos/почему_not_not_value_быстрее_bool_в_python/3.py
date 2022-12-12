import timeit


def bool_execution(value):
	return bool(value)


def not_execution(value):
	# Оставляем ссылку на bool
	temp = bool
	temp = bool()
	return not not value


def main():
	kwargs = {
		"setup": "value=10",
		"globals": globals(),
		"number": 20_000_000
	}

	bool_result = timeit.timeit("bool_execution(value)", **kwargs)
	not_result = timeit.timeit("not_execution(value)", **kwargs)

	print(f"{bool_result=:.02f}")
	print(f"{not_result=:.02f}")


if __name__ == "__main__":
    main()

