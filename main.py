from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from confi import TOKEN
from keyboard import menu_1, MI
import requests
from bs4 import BeautifulSoup
import data_base
import sqlite3


bot = Bot(TOKEN)
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
        url = 'https://weather.com/ru-RU/weather/today/l/5ad65038b8ca5303fbb202f94de129249870d2b8c1f8cba70e77231ed1007997'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('span', class_="CurrentConditions--tempValue--3a50n")

        for quote in quotes:
            await message.answer("В городе Сибай:")
            await message.answer(quote.text)
    elif message.text == "БД 😀":
        await message.answer("Ваши данные из БД:")
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        people_id_2 = message.chat.id
        cursor.execute(f"SELECT id FROM user_id WHERE id = {people_id_2}")
        data = cursor.fetchone()
        if data is None:
            await message.answer("Похоже, что вас нет в БД")
            await message.answer("Напишите /start")
        else:
            for i in cursor.execute(f"SELECT name, last_name FROM user_id WHERE id = {people_id_2}"):
                await message.answer(str(i))
    elif message.text == "Курс валют 📈":
        await message.answer("Валюта:", reply_markup=MI)
    elif message.text == "Доллар $":
        url2 = 'https://www.tinkoff.ru/invest/currencies/USDRUB/pulse/'
        response2 = requests.get(url2)
        soup2 = BeautifulSoup(response2.text, 'lxml')
        quotes2 = soup2.find_all('div', class_="SecurityInvitingScreen__price_FSP8P")
        for i in quotes2:
            await message.answer(i.text)
    elif message.text == "Евро €":
        url3 = 'https://www.tinkoff.ru/invest/currencies/EURRUB/'
        response3 = requests.get(url3)
        soup3 = BeautifulSoup(response3.text, 'lxml')
        quotes3 = soup3.find_all('div', class_="SecurityInvitingScreen__price_FSP8P")
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
