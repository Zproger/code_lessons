
class Base:
    def __init__(self, value):
        self.value = value
        print(f"Base init: {self.value}")

class A(Base):
    def __init__(self, value):
        super().__init__(value)
        self.a_value = value * 2
        print(f"A init: {self.a_value}")

class B(Base):
    def __init__(self, value):
        super().__init__(value)
        self.b_value = value * 3
        print(f"B init: {self.b_value}")

class C(A, B):
    def __init__(self, value):
        super().__init__(value)

c = C(5)
print(C.__mro__)
