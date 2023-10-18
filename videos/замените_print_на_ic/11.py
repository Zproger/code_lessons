from icecream import ic

class Counter:
    value: int = 0

    @classmethod
    def increment(cls):
        cls.value += 1
        return f"{cls.value}) | "

ic.configureOutput(prefix=Counter.increment)
ic("hello")
ic("world")
ic("world")
ic("world")
ic("world")

