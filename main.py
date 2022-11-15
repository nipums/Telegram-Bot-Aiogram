from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from confi import TOKEN, BASE
from keyboard import menu_1, MI
import requests
from bs4 import BeautifulSoup
import data_base
import psycopg2


bot = Bot(TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def on_startup(_):
    print("Бот запущен >>> Онлайн")


@dp.message_handler(commands=["start", "help"])
async def welcome(message: types.Message):
    sticker = open("image/Hello2.webp", "rb")
    await message.answer_sticker(sticker)
    await message.answer("Привет, чем я могу помочь тебе?", reply_markup=menu_1)
    data_base.start(message)
    await message.answer("Данные добавлены в БД")


@dp.message_handler(commands=["delete"])
async def delete(message: types.Message):
    data_base.delete(message)
    await message.answer("Данные удалены из БД")


@dp.message_handler()
async def echo(message: types.Message):
    if message.text == "Мой ID 🕵":
        await message.answer("Ваш ID:")
        await message.answer(message.chat.id)
    elif message.text == "Погода 🌧":
        url = 'https://rp5.ru/Погода_в_Сибае'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('span', class_="t_0")

        for quote in quotes:
            await message.answer("В городе Сибай:")
            await message.answer(quote.text)
    elif message.text == "БД 😀":
        await message.answer("Ваши данные из БД:")
        connect = psycopg2.connect(BASE, sslmode="require")
        cursor = connect.cursor()
        people_id_2 = message.chat.id
        cursor.execute(f"SELECT id, name, last_name FROM user_id WHERE id = {people_id_2}")
        data = cursor.fetchall()
        if not data:
            await message.answer("Похоже, что вас нет в БД")
            await message.answer("Напишите /start")
        else:
            for data1 in data:
                text1 = "<strong>ID:</strong> " + str(data1[0])
                text2 = "<strong>Имя:</strong> " + str(data1[1])
                text3 = "<strong>Фамилия:</strong> " + str(data1[2])
                await message.answer(text1)
                await message.answer(text2)
                await message.answer(text3)
    elif message.text == "Курс валют 📈":
        await message.answer("Валюта:", reply_markup=MI)
    elif message.text == "Биткоин ₿":
        url2 = 'https://www.binance.com/ru/price/bitcoin'
        response2 = requests.get(url2)
        soup2 = BeautifulSoup(response2.text, 'lxml')
        quotes2 = soup2.find_all('div', class_="css-12ujz79")
        for i in quotes2:
            await message.answer(i.text)
    elif message.text == "Эфир Ξ":
        url3 = 'https://www.binance.com/ru/price/ethereum'
        response3 = requests.get(url3)
        soup3 = BeautifulSoup(response3.text, 'lxml')
        quotes3 = soup3.find_all('div', class_="css-12ujz79")
        for k in quotes3:
            await message.answer(k.text)
    elif message.text == "Назад ⬅":
        await message.answer("Чем я могу помочь тебе?", reply_markup=menu_1)
    elif message.text == "Коронавирус 🦠":
        url4 = 'https://стопкоронавирус.рф/'
        response4 = requests.get(url4)
        soup4 = BeautifulSoup(response4.text, 'lxml')
        quotes4 = soup4.find_all('div', class_="cv-countdown__item-value _accent-green")
        await message.answer("Выздоровело человек за сегодня:")
        for u in quotes4:
            await message.answer(u.text)
    else:
        await message.answer("Ошибка!")

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
