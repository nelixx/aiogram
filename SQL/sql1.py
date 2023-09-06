import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


TOKEN='5892621513:AAGa0SD7CZsopc5_Jziy_nZqSN94rGbUZ9Y'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())





if __name__ == '__main__':
    executor.start_polling(dp)
