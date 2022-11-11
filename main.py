from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

TOKEN = "5531484359:AAEPLhL1hoZHkb83orE8aaJSW5zz5Deb2Y8"

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
