from pydantic import BaseModel

class Note(BaseModel):
    text: str
    secret: str
    note_hash: str = None  # Результат, ссылка на готовую записку

class NotesList(BaseModel):
    all_notes: list[Note] = list()

class NoteID(BaseModel):
    note_id: str
    note_secret: str