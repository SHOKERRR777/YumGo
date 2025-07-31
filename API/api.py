import os

import uvicorn 
from pathlib import Path

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.database.models import Item, async_session

templates = Jinja2Templates(directory="API/templates")

# Данная конструкция подключает базу данных в этот файл
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with async_session() as session:
        print("Bot is ready")
        yield

app = FastAPI(title="To Do App", lifespan=lifespan)

@app.get("/", response_class=HTMLResponse)
def food_menu(request: Request):
    return templates.TemplateResponse("menu_food.html", food_list=Item)

# Запуск программы 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run("main:app", host="0.0.0.0", port=port) 