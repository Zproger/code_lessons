
def main1(values: list | tuple):
    if len(values) == 2 and values[0] == "load":
        print(f"main1, {values=}, link={values[1].__repr__()}")
    else:
       print("default")

def main2(values: list | tuple):
    match values:
        case "load", link:
            print(f"main2, {values=}, {link=}")
        case _:
            print("default")

main1(["load", "123"])
main2(["load", "456"])