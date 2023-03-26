

class DebugInfo:
    def __repr__(self):
        cls_name = self.__class__.__name__
        attrs = [f"{key}={value}" for key, value in self.__dict__.items()]
        return f"{cls_name}({', '.join(attrs)})"


class UserSettings:
    def __init__(self, *, notifications_enabled: bool, language: str, theme: str):
        self.notifications_enabled = notifications_enabled
        self.language = language
        self.theme = theme

    def __repr__(self):
        return f"UserSettings({self.notifications_enabled=}, {self.language=}, {self.theme=})"


class UserData:
    def __init__(self, *, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age

    def __repr__(self):
        return f"UserData({self.username=}, {self.email=}, {self.age=})"


class UserAccount:
    def __init__(
        self, *, notifications_enabled: bool, language: str, theme: str,
        username: str, email: str, age: int
    ):
        self.notifications_enabled = notifications_enabled
        self.language = language
        self.theme = theme
        self.username = username
        self.email = email
        self.age = age

    def __repr__(self):
        result = f"{self.notifications_enabled=}, {self.language=}, {self.theme=} " + \
                 f"{self.username=}, {self.email=}, {self.age}"
        return f"UserAccount({result})"


user_data = UserData(username="u1", email="u1@gmail.com", age=17)
user_setting = UserSettings(notifications_enabled=True, language="EN", theme="Dark")

user_account = UserAccount(
    notifications_enabled=True,
    language="EN",
    theme="Dark",
    username="u2",
    email="u2@gmail.com",
    age=18
)

print(user_data)
print(user_setting)
print(user_account)