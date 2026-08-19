from urllib import request

from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(request, "index.html", {})

@app.get("/games", response_class=HTMLResponse)
def gamespage(request: Request):
    return templates.TemplateResponse(request, "games.html", {})

@app.get("/books", response_class=HTMLResponse)
def bookspage(request: Request):
    return templates.TemplateResponse(request, "books.html", {})

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)