from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb
from config import *
from database import *

my_router = Router()

@my_router.message(CommandStart())
async def cmd_start(message: Message):
    id_user = message.from_user.id
    add_user_to_db(user_id=id_user) # добавление в бд

    print(f'{message.from_user.username} | {message.from_user.id}: Запустил бота')

    if id_user in ADMIN_IDS:
        await message.answer_sticker(WELCOME_STICKER)
        await message.reply(f'<b>{WELCOME_CHAR} Добро пожаловать в ... </b> \n \n'
                            f'<i>{DESCRIPT_CHAR} Я могу помочь тебе...</i>',
                            parse_mode='HTML', reply_markup=kb.adm_keyboard)

    else:
        await message.answer_sticker(WELCOME_STICKER)
        await message.reply(f'<b>{WELCOME_CHAR} Добро пожаловать в ... </b> \n \n'
                            f'<i>{DESCRIPT_CHAR} Я могу помочь тебе...</i>',
                            parse_mode='HTML', reply_markup=kb.main)


# пример обработчика текста
@my_router.message(lambda msg: msg.text == 'текст')
async def snow_radar(message: types.Message):
    print(f'{message.from_user.username} | {message.from_user.id}: ...')
    await message.reply('...')

# пример инлайн
@my_router.callback_query(lambda cb: cb.data == 'inline')
async def close(query: CallbackQuery):
    await query.message.answer('...')


@my_router.message(lambda msg: msg.text == '👨‍💻Админ-панель')
async def admin_panel(message: Message):
    user_id = message.from_user.id
    if user_id in ADMIN_IDS:
        await message.answer('Выберите пункт', reply_markup=kb.admin_panel)
    else:
        return


@my_router.callback_query(lambda cb: cb.data == 'close')
async def close(query: CallbackQuery):
    await query.message.delete()
