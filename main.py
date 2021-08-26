from flask import Flask, request
from telebot import types
import telebot

bot = telebot.TeleBot('')
bot.set_webhook(url="")
app = Flask(__name__)


@app.route('/', methods=["POST"])
def webhook():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]
    )
    return "ok"


main_keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
button_add = types.KeyboardButton(text="Добавить")
button_change = types.KeyboardButton(text="Изменить")
button_delete = types.KeyboardButton(text="Удалить")
main_keyboard.add(button_add, button_change, button_delete)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "привет я помогу с таблетосами", reply_markup=main_keyboard)


@bot.message_handler(regexp='Добавить')
def add_med(message):
    bot.send_message(message.chat.id, 'ща добавим')
    bot.send_message(message.chat.id, 'еще помочь?', reply_markup=main_keyboard)


@bot.message_handler(regexp='Изменить')
def change_med(message):
    bot.send_message(message.chat.id, 'ща изменим')
    bot.send_message(message.chat.id, 'еще помочь?', reply_markup=main_keyboard)

@bot.message_handler(regexp='Удалить')
def delete_med(message):
    bot.send_message(message.chat.id, 'ща удалим')
    bot.send_message(message.chat.id, 'еще помочь?', reply_markup=main_keyboard)


if __name__ == "__main__":
    app.run()
