from icecream import ic

def int_handler(value):
    if isinstance(value, int):
        return f"[type: int, value: {value}]"
    return repr(value)

ic.configureOutput(argToStringFunction=int_handler)
ic(2, "hello")