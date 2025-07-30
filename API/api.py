import uvicorn 

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.database.models import Item, async_session

from pathlib import Path


templates = Jinja2Templates(directory="templates")

app = FastAPI(title="To Do App")

# Данная конструкция
@asynccontextmanager
async def lifesppan(app: FastAPI):
    await async_session
    print("Bot is ready")
    yield

@app.route("/", response_class=HTMLResponse)
def food_menu(request: Request):
    return templates.TemplateResponse("menu_food.html", food_list=Item)

# Запуск программы 
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True) #reload=True для того, чтобы автоматически обновлялось при изменениях