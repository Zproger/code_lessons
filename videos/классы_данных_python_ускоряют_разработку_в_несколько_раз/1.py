from functools import total_ordering


# @total_ordering
class UserData:
    def __init__(self, *, user_id: int, username: str, email: str):
        self.__user_id = user_id
        self.__username = username
        self.__email = email

    @property
    def user_id(self):
        return self.__user_id

    @property
    def username(self):
        return self.__username

    @property
    def email(self):
        return self.__email

    def __eq__(self, other):
        return ((self.__user_id, self.__username, self.__email) ==
                (other.__user_id, other.__username, other.__email))

    def __ne__(self, other):
        return ((self.__user_id, self.__username, self.__email) !=
                (other.__user_id, other.__username, other.__email))

    def __lt__(self, other):
        return ((self.__user_id, self.__username, self.__email) <
                (other.__user_id, other.__username, other.__email))

    def __le__(self, other):
        return ((self.__user_id, self.__username, self.__email) <=
                (other.__user_id, other.__username, other.__email))

    def __gt__(self, other):
        return ((self.__user_id, self.__username, self.__email) >
                (other.__user_id, other.__username, other.__email))

    def __ge__(self, other):
        return ((self.__user_id, self.__username, self.__email) >=
                (other.__user_id, other.__username, other.__email))

    def __repr__(self):
        return f"UserData({self.__user_id=}, {self.__username=}, {self.__email=})"


user_1 = UserData(user_id=0, username="u1", email="u1@gmail.com")
user_2 = UserData(user_id=1, username="u2", email="u2@gmail.com")

print(f"{(user_1 > user_2)=}")
print(f"{(user_1 < user_2)=}")
print(f"{(user_1 == user_2)=}")

print(user_1)
print(user_2)

# user_1.user_id = 100  # ERROR