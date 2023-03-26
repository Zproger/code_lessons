from dataclasses import dataclass


@dataclass(kw_only=True)
class UserSettings:
    notifications_enabled: bool
    language: str
    theme: str


@dataclass(kw_only=True)
class UserData:
    username: str
    email: str
    age: int


@dataclass(kw_only=True)
class UserAccount(UserData, UserSettings):
    ...


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