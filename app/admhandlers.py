from aiogram.types import CallbackQuery
from database import *
from aiogram import Router, types

broadcast_text = ""
broadcast_photo = ""

adm_router = Router()

@adm_router.callback_query(lambda cb: cb.data == 'say_broadcast')
async def send_broadcast(callback_query: CallbackQuery):
    user_count = get_user_count()
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT user_id FROM users')
    users = cursor.fetchall()
    conn.close()

    for user in users:
        user_id = user[0]
        try:
            if broadcast_photo and broadcast_text:
                await callback_query.message.bot.send_photo(user_id, broadcast_photo, caption=broadcast_text)
            elif broadcast_text:
                await callback_query.message.bot.send_message(user_id, broadcast_text)
            elif broadcast_photo:
                await callback_query.message.bot.send_photo(user_id, broadcast_photo)
            else:
                await callback_query.answer('Для начала укажите параметры для рассылки')
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {user_id}: {e}")

    await callback_query.answer(f'📢 Рассылка успешно отправлена всем {user_count} пользователям!')


user_bc_text = {}
user_bc_photo = {}


@adm_router.callback_query(lambda cb: cb.data == 'set_bc_text')
async def set_broadcast_text(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    user_bc_text[user_id] = True
    await callback_query.answer("Введите текст рассылки:")


@adm_router.callback_query(lambda cb: cb.data == 'set_bc_photo')
async def set_broadcast_photo(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    user_bc_photo[user_id] = True
    await callback_query.answer("Отправьте фото для рассылки:")


@adm_router.message(lambda message: message.text and message.from_user.id in user_bc_text)
async def receive_broadcast_text(message: types.Message):
    global broadcast_text
    broadcast_text = message.text
    await message.reply("✅ Текст рассылки установлен!")
    del user_bc_text[message.from_user.id]


@adm_router.message(lambda message: message.photo and message.from_user.id in user_bc_photo)
async def receive_broadcast_photo(message: types.Message):
    global broadcast_photo
    broadcast_photo = message.photo[-1].file_id
    await message.reply("✅ Фото рассылки установлено!")
    del user_bc_photo[message.from_user.id]


@adm_router.callback_query(lambda cb: cb.data == 'delete_bc_text')
async def delete_broadcast_text(callback_query: CallbackQuery):
    global broadcast_text
    broadcast_text = ""
    await callback_query.answer("✅ Текст рассылки удален!")

@adm_router.callback_query(lambda cb: cb.data == 'delete_bc_photo')
async def delete_broadcast_photo(callback_query: CallbackQuery):
    global broadcast_photo
    broadcast_photo = ""
    await callback_query.answer("✅ Фото рассылки удалено!")

@adm_router.callback_query(lambda cb: cb.data == 'get_users')
async def get_users_count(callback: CallbackQuery):
    user_count = get_user_count()
    await callback.message.answer(f'📊 Кол-во пользователей: {user_count}')