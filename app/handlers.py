from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.database.request as rq

import app.keyboards as kb

router = Router()

""" Обработчик команды /start """
@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer_photo(photo='https://nbkk.co.jp/wp-content/uploads/2023/06/yumgo-logo.png')
    await message.answer(f"""
🍔 Добро пожаловать, {message.from_user.first_name}, в YumGo! 🚀
                         
Выбери действие из меню ниже:""", reply_markup=kb.main)
    

""" Обработчик команды /help """
@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("""
📌 Команда /help

🍕 Что умеет этот бот?
С помощью YumGo ты можешь заказать вкусную еду с доставкой прямо домой! 🚗💨

📝 Как это работает?

    📲 Выбери "Меню" (/menu или кнопка ниже) – откроется WebApp с ассортиментом.

    🛍️ Собери заказ – добавляй понравившиеся блюда в корзину.

    📦 Оформи доставку – заполни короткую анкету с адресом.

    ⏳ Жди курьера – осталось только получить вкусняшки! 😋

🔹 Быстрые команды:

    /menu – открыть меню

    /cart – проверить корзину

    /support – помощь оператора
""")


""" Обработчик кнопки "Меню" """
@router.message(F.text == "Меню")
@router.message(Command('menu'))
async def main_menu_mes(message: Message):
    await message.answer("""
Как это работает?
1️⃣ Откроется удобное WebApp-приложение с полным ассортиментом
2️⃣ Выбирай блюда, добавляй в корзину и оформляй заказ в пару кликов!
""", reply_markup=kb.webapp_pril)
    

""" Обработчик кнопки-команды "Проверить корзину" """
@router.message(F.text == "Проверить корзину")
@router.message(Command('cart'))
async def my_cart(message: Message):
    await message.answer("Данная команда находится в разработке, но в скором времени она обязательно заработает!")


""" Обработчик сообщения "Помощь оператора" """
@router.message(F.text == "Помощь оператора")
@router.message(Command('support'))
async def additional_help(message: Message):
    await message.answer("""
🛎️ Нужна помощь?

Не стесняйся обращаться к нашему менеджеру! Он с радостью ответит на все твои вопросы и поможет с заказом. 💬

👉 Напиши сюда: @YumGo_Support

Мы на связи 24/7 и сделаем всё, чтобы твой опыт был идеальным! 🌟
""")