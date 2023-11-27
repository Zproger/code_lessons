
def human_inspection(arg) -> bool:
    if arg == "I love shawarma":
        return True
    elif arg == "I don't like shawarma":
        return False

if __name__ == "__main__":
    human_inspection("I love shawarma")