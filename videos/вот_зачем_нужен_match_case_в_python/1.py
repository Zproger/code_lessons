
arg = "I love shawarma"

match arg:
    case "i love shawarma":
        print(1)
    case "I don't like shawarma":
        print(2)
    case other:
        print(other)
