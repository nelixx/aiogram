import requests 
from bs4 import BeautifulSoup as BS
import logging
from aiogram import Bot, Dispatcher, types, executor     

bot = Bot(token='6541815968:AAEfV3dipxQ3sCgQNJsid7fKt7JzQiJBvdU')
dp = Dispatcher(bot)

def travel_list(travel: str):
    url=(f"https://travelist.pl/search/channel:/dates:/price:0,1000/sortType:/tags:/rooms:[2,[]]/page:1")
    html = BS('.content' , 'html.parser')

for el in html.select('.items > .stat-wrapper'):
    title = el.select('.caption > a')
    print(title[0].text)
    responce=requests.get(url)

#@dp.message_handler(commands=["start"])
#async def process_start1(message: types.Message):
#    await bot.send_message(message.from_user.id, 'Привіт, я твій помічник в шуканні відпочинку наиши /help щоб я вам надав допомогу')

#@dp.message_handler(commands=["start"])
#async def process_start1(message: types.Message):
#    await bot.send_message(message.from_user.id, 'Виберіть країну в яку хочите полетіти /travel')

#@dp.message_handler(commands=["travel"])
#async def process_start1(message: types.Message):
#    await bot.send_message(message.from_user.id, 'Ну що вже не так? Ну добре щоб розпочати напиши /start. Якщо виникли проблеми з ботом пишіть https://t.me/flamingokun')

#@dp.message_handler(commands=["help"])
#async def process_start1(message: types.Message):
#    await bot.send_message(message.from_user.id, 'Ну що вже не так? Ну добре щоб розпочати напиши /start. Якщо виникли проблеми з ботом пишіть https://t.me/flamingokun')


if __name__ == "__main__":
    print(travel_list)