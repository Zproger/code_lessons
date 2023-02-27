import ftplib


class RemoteFile:
    def __init__(self, filename, mode='r', server_ip='127.0.0.1', port='4444'):
        self.__filename = filename
        self.__mode = mode
        self.__server_ip = server_ip
        self.__port = port
        self.__fp = None

    # custom write method
    def remote_write(self, text: str):
        if self.__fp:
            print(f"connect to the server: {self.__server_ip}:{self.__port}")
            self.__fp.write(text)

    def __enter__(self):
        print("__enter__")
        self.__fp = open(self.__filename, mode=self.__mode)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self.__fp.close()

    # <open file 'server.log', mode 'r' at 0x21a22abf1>
    def __repr__(self):
        info = f"open remote file '{self.__filename}', mode '{self.__mode}' "
        info += f"at {hex(id(self.__fp))}"
        return info


with RemoteFile("server.log", "w") as file:
    print(file)
    file.remote_write("hello world")


 