
class A:
    def get(self):
        print("A")

class B:
    def get(self):
        print("B")

class C(A, B):
    def get(self):
        A.get(self)
        B.get(self)

c = C()
c.get()
