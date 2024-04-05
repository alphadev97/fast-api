# from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://dev095162:m2yFKlG9WboX90cK@cluster0.zvnpvpz.mongodb.net/")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDoc = []
    for doc in docs:
        newDoc.append({
            "id": doc["_id"],
            "note": doc["note"]
        })
    return templates.TemplateResponse(
        request=request, name="index.html", context={"newDoc" : newDoc}
    )


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}