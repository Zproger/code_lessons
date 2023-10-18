from icecream import ic

DEBUG = True

def is_debug():
    return ic(DEBUG)

def new_print(value):
    print(f"What? Value: {value}")

if new_print(ic(is_debug())) is None:
    print("finish")

