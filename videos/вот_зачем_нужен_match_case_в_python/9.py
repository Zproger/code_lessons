
def get_color(color):
    match color:
        case (r, g, b):
            print("RGB")
        case (r, g, b, a):
            print("RGBA")
        case _:
            print("Такого шаблона нет")

get_color([120, 120, 120])
get_color([120, 120, 120, 120])
get_color([120, 120])  # error
