class NetworkCore:
    @classmethod
    def get_ip(cls, address="127.0.0.1"):
        print(f"IP Address: {address} | Object: {cls}")

class HTTP(NetworkCore):
    @classmethod
    def get_ip(cls, address="0.0.0.0"):
        print(f"HTTP: {address} | Object: {cls}")
        super().get_ip(address)

class FTP(NetworkCore):
    def get_ip(self, address="192.168.0.1"):
        print(f"\nFTP: {address} | Object: {self}")
        super().get_ip(address)

HTTP.get_ip()
FTP().get_ip()
