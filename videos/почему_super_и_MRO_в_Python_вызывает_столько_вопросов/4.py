from io import TextIOWrapper


class Logger(TextIOWrapper):
    def __init__(self, *args, **kwargs):
        self.log = []
        super().__init__(*args, **kwargs)

    def write(self, s):
        self.log.append(f"Writing: {s}")
        return super().write(s)

    def read(self, size=-1):
        data = super().read(size)
        self.log.append(f"Reading: {data}")
        return data


with open("example.txt", "wb+") as file:
    example = Logger(
        file,
        encoding="UTF-8",
    )
    example.write("Hello, world!")
    example.seek(0)
    example.read()

    for entry in example.log:
        print(f"Final Cycle | {entry}")
