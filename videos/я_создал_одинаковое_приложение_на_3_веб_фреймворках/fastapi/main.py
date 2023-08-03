from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from handlers import get_info_by_ip

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# pip install fastapi
# pip install "uvicorn[standard]"

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process_ip", response_class=HTMLResponse)
async def process_ip(ip_address: str = Form(...), request: Request = Request):
    ip_info = get_info_by_ip(ip_address)
    result = f"{ip_address}: {ip_info}"
    return templates.TemplateResponse("index.html", {"request": request, "result": result})
