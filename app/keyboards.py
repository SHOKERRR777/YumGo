from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='меню', callback_data='webapppril')],
    [InlineKeyboardButton(text='Проверить корзину', callback_data='check_cart')],
    [InlineKeyboardButton(text='помощь оператора', callback_data='help_operator')]
], 
                        resize_keyboard=True)

webapp_pril = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text='Чтобы сделать заказ, нажми на эту кнопку 🥰',
        web_app=WebAppInfo(url='https://taxi-report.onrender.com/')
    )]
])
