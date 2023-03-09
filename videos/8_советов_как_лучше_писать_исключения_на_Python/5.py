from collections import namedtuple


"""
Исправлено в > Python 3.8
"""


user = {
    "name": "barakuda2000",
    "status": "unlocked"
}


class BannedException(Exception):
    ...


def banned_user(user: dict):
    try:
        set_banned_status(user)
    except:
        raise BannedException(f"Не удалось заблокировать {user['name']}")


def set_banned_status(user: dict):
    userrrr["status"] = "banned"  # error


if __name__ == "__main__":
    banned_user(user)