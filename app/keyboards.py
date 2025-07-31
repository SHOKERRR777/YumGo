from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Меню")],
    [KeyboardButton(text="Проверить корзину")], [KeyboardButton(text="Помощь оператора")]
],                       
                        resize_keyboard=True)

webapp_pril = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text='Чтобы сделать заказ, нажми на эту кнопку 🥰',
        web_app=WebAppInfo(url='https://yumgo.onrender.com/')
    )]
])
