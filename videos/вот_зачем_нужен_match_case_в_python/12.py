
args = ["start", "--help"]

match args:
    case ["start", ("-h" | "--help" | "help")]:
        print("help")
    case _:
        print("default")