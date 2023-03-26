from dataclasses import dataclass


@dataclass(order=True, frozen=True, kw_only=True)
class UserData:
    user_id: int
    username: str
    email: str


user_1 = UserData(user_id=0, username="u1", email="u1@gmail.com")
user_2 = UserData(user_id=1, username="u2", email="u2@gmail.com")

print(f"{(user_1 > user_2)=}")
print(f"{(user_1 < user_2)=}")
print(f"{(user_1 == user_2)=}")

print(user_1)
print(user_2)

# user_1.user_id = 100  # ERROR