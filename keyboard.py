from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

BTN_1 = KeyboardButton("Погода 🌧")
BTN_2 = KeyboardButton("Курс валют 📈")
BTN_3 = KeyboardButton("Коронавирус 🦠")
BTN_4 = KeyboardButton("БД 😀")
BTN_5 = KeyboardButton("Мой ID 🕵")
BTN_6 = KeyboardButton("Биткоин ₿")
BTN_7 = KeyboardButton("Эфир Ξ")
BTN_8 = KeyboardButton("Назад ⬅")
BTN_5_1 = KeyboardButton("Галерея фото 🌇")
menu_1 = ReplyKeyboardMarkup(resize_keyboard=True).add(BTN_1, BTN_2, BTN_3, BTN_4, BTN_5)

MI = ReplyKeyboardMarkup(resize_keyboard=True).add(BTN_6, BTN_7, BTN_8)