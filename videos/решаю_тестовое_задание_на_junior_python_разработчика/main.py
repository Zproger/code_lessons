from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from schemes import Note, NotesList, NoteID
from cipher import get_note_id

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # Тут шаблоны
notes_list = NotesList()

@app.get("/", response_class=HTMLResponse)
async def get_home_page(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "notes_count": len(notes_list.all_notes)
    })

@app.post("/create_note")
async def send_notes(note_data: Note):
    # Генерируем ID записки
    note_id = get_note_id(text=note_data.text, salt=note_data.secret)
    note_data.note_hash = note_id
    notes_list.all_notes.append(note_data)
    return {"response": "ok", "note_id": note_id}

@app.get("/result/{note_id}", response_class=HTMLResponse)
async def get_result_id(request: Request, note_id: str):
    return templates.TemplateResponse("hash_storage.html", {
        "request": request,
        "note_id": note_id
    })

@app.post("/get_note")
async def get_note(note_data: NoteID):
    for note in notes_list.all_notes:  # по уже добавленным запискам
        if (note_data.note_id == note.note_hash and
            note_data.note_secret == note.secret):
                note_index = notes_list.all_notes.index(note)
                notes_list.all_notes.pop(note_index)
                return {"response": "ok", "note_final_text": note.text}
    return {"response": "ok", "note_final_text": "Such a note does not exist"}

@app.get("/note_page/{note_text}", response_class=HTMLResponse)
async def get_result_note(request: Request, note_text: str):
    return templates.TemplateResponse("note_page.html", {
        "request": request,
        "note_text": note_text
    })