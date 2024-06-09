class NewStr(str):
    def __init__(self, value):
        super().__init__()

    def underlining(self):
        return f"-- {self} --"

    def upper(self):
        return NewStr(super().upper())
    

text = NewStr("Hello World")
print(text.underlining())
print(text.underlining().upper())
print(text.upper().underlining())

