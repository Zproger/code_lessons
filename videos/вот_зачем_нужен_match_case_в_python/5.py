
def client_hello(server_code):
    match server_code:
        case 1 | 2 | 3:
            print("Connection established")
        case _:
            print("No connection")

client_hello(1)
client_hello("2")