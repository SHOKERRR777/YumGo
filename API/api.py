from flask import Flask, render_template, request

from app.database.models import async_session

app = Flask(__name__)

@app.router('/')
def menu_food():
    user_id = request.args.get('tg_id')

    if not user_id:
        return "Доступ запрещен!", 403
    try:
        async def db_init():
            await async_session() # Включаем базу данных в этот файл

        return render_template('menu_food.html')

    except TypeError as e:
        print(f"Ошибка с типами данных: {e}")

# Запуск файла
if __name__ == "__main__":
    app.run(debug=True)