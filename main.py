from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from decouple import config


TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start", "help"])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Пиветствую {message.from_user.first_name}!")


@dp.message_handler(commands=["quiz"])
async def quiz_1(message: types.Message):
    marcup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    marcup.add(button_call_1)

    question = "Если 24% числа равно 96, то число равно?"
    answers = [
        "560",
        "450",
        "400",
        "100"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        explanation="Иди заново в 5-ый класс!",
        open_period=10,
        reply_markup=marcup
    )


@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):

    question = "(+15) + (-7) =?"
    answers = [
        "-22",
        "8",
        "-8",
        "22"

    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=1,
        explanation="Иди заново в 5-ый класс!",
        open_period=10
    )


@dp.message_handler(commands=["mem"])
async def mem_handler(message: types.Message):

    photo = open("media/download.jpg", "rb")

    await bot.send_photo(message.from_user.id, photo=photo)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text)**2)
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
