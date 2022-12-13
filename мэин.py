from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


bot = Bot('TOKEN')
dp = Dispatcher(bot)

# 1212121212


start_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
start_button1 = KeyboardButton(text='Первый юрыль')
start_button2 = KeyboardButton(text='Второй кульбэк')
start_keyboard.add(start_button1, start_button2)

urlkeyboard = InlineKeyboardMarkup(row_width=1)
google_inline_button = InlineKeyboardButton(text='гулугуле', url='https://www.google.ru/')
yandex_inline_button = InlineKeyboardButton(text='великий и не повторимый', url='https://ya.ru/')
urlkeyboard.add(google_inline_button, yandex_inline_button)

callback_inline_keyboard = InlineKeyboardMarkup(row_width=1)
first_callback = InlineKeyboardButton(text='Ну тут выбор очевиден', callback_data='он выбрал это')
callback_inline_keyboard.add(first_callback)

@dp.message_handler(commands=(['start']))
async def start(message: types.Message):
    await message.answer('Начало', reply_markup=start_keyboard)

@dp.message_handler()
async def body(message: types.Message):
    if message.text == 'Первый юрыль':
        await message.answer(text='Выбор за тобой', reply_markup=urlkeyboard)
    elif message.text == 'Второй кульбэк':
        await message.answer(text='Жми сук', reply_markup=callback_inline_keyboard)
    else:
        await message.answer(text='МЕНЯЙ СУК')

@dp.callback_query_handler()
async def onecall(callback: types.CallbackQuery):
    if callback.data == 'он выбрал это':
        await callback.answer(text='12345')
# https://api.telegram.org/bot5733141109:AAEuwSAskLBqyKQtChRXvSw0ixkMgy2E448/setWebhook?url=http://dmitrii1101.pythonanywhere.com/

if __name__ == '__main__':
    executor.start_webhook(dispatcher=dp, webhook_url='http://dmitrii1101.pythonanywhere.com/webhook/5733141109:AAEuwSAskLBqyKQtChRXvSw0ixkMgy2E448',
                           webhook_path='5733141109:AAEuwSAskLBqyKQtChRXvSw0ixkMgy2E448',
                           webhook_host='http://dmitrii1101.pythonanywhere.com/',
                           host='0.0.0.0',
                           port='8000'
                           )
