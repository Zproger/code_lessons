
object = type("object", (object,), {
    "zproger_top": lambda x: print("Surprise")
})

class IPV4:
    def zproger_top1(self):
        print("IPV4")

class IPV6:
    def zproger_top2(self):
        print("IPV6")

class Request(IPV4, IPV6, object):
    pass

a = Request()
a.zproger_top()

