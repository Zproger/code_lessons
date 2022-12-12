import timeit


def main():
	kwargs = {
		"setup": "value=10",
		"globals": globals(),
		"number": 50_000_000
	}

	bool_result = timeit.timeit("bool(True)", **kwargs)
	not_result = timeit.timeit("not not True", **kwargs)

	print(f"{bool_result=:.02f}")
	print(f"{not_result=:.02f}")


if __name__ == "__main__":
    main()
