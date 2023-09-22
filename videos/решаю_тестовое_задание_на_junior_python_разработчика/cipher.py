import hashlib

# salt это соль, вместо нее юзаем секретный код
def get_note_id(text: str, salt: str) -> str:
    return hashlib.sha256(
        text.encode("UTF-8") + salt.encode("UTF-8")
    ).hexdigest()
