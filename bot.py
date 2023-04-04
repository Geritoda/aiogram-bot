from aiogram import Bot, Dispatcher, types, executor
import logging

TOKEN = '5866465433:AAHX_R16uV5qUycZDzgmMsFozBhEvRcUnjg'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
