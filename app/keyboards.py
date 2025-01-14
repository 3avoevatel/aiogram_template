from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

# для юзеров
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Кнопка 1'), KeyboardButton(text='Кнопка 2')],
    [KeyboardButton(text='Кнопка 3'), KeyboardButton(text='Кнопка 4')],
    [KeyboardButton(text='Кнопка 5'), KeyboardButton(text='Кнопка 6')],
], resize_keyboard=True, input_field_placeholder='Выберите пункт в меню <3')

# для админов
adm_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Кнопка 1'), KeyboardButton(text='Кнопка 2')],
    [KeyboardButton(text='Кнопка 3'), KeyboardButton(text='Кнопка 4')],
    [KeyboardButton(text='Кнопка 5'), KeyboardButton(text='Кнопка 6')],
    [KeyboardButton(text='👨‍💻Админ-панель')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт в меню <3')


# пример инлайн клавиатуры
inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Кнопка 1', callback_data='inl1')],
    [InlineKeyboardButton(text='Кнопка 2', callback_data='inl2')],
    [InlineKeyboardButton(text='Кнопка 3', callback_data='inl3')],
    [InlineKeyboardButton(text='Кнопка 4', callback_data='inl4')]
])


# при нажатии на сообщение оно удалится
close = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='✖️ Закрыть', callback_data='close')]
])

# адм панель
admin_panel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📊Статистика', callback_data='get_users')],
    [InlineKeyboardButton(text='📢Рассылка', callback_data='say_broadcast')],
    [InlineKeyboardButton(text='📝Текст рассылки', callback_data='set_bc_text')],
    [InlineKeyboardButton(text='🗑Стереть текст', callback_data='delete_bc_text')],
    [InlineKeyboardButton(text='🖼Фото рассылки', callback_data='set_bc_photo')],
    [InlineKeyboardButton(text='🗑Стереть фото', callback_data='delete_bc_photo')]
])
