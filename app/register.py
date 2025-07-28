from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm import state

router = Router()

""" Специальный класс для регистрации"""
class Reg(StatesGroup):
    name = State()
    number = State()
    adres = State()

@router.message(Command('reg'))
async def reg_name(message: Message):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer("Для регистрации в систему для начала введите Ваше имя:")

@router.message(Reg.number)
async def reg_number(message: Message):
    await state.update_data(number=message.text)
    await state.set_state(Reg.adres)
    await message.answer("Отлично, теперь введите ваш номер телефона (89...):")

@router.message(Reg.adres)
async def reg_adres(message: Message):
    await state.update_data(adres=message.text)
    await message.answer("Регистрация прошла успешно!")
    await state.clear()