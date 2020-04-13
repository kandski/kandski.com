from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/assets", StaticFiles(directory="src/web/assets"), name="assets")

templates = Jinja2Templates(directory="src/web/views")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("landing-page.html", {"request": request})


@app.get("/profile")
async def read_root(request: Request):
    return templates.TemplateResponse("profile-page.html", {"request": request})


@app.get("/landing")
async def read_root(request: Request):
    return templates.TemplateResponse("landing-page.html", {"request": request})


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
