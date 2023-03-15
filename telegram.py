import telebot
from telebot import types
import os
from dotenv import load_dotenv, find_dotenv



load_dotenv(find_dotenv())
bot = telebot.TeleBot(os.getenv('TOKEN'))

#start = types.KeyboardButton("Старт")
#bot.send_message(message.chat.id, text="Нажимай", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if (message.text == "Старт"):
        bot.send_message(message.chat.id, text="Привет, спасибо что посетил нашего бота!")
        btn1 = types.KeyboardButton("Каталог")
        btn2 = types.KeyboardButton("Контакты")
        btn3 = types.KeyboardButton("Возможности")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Ну давай выбирай", reply_markup=markup)
    elif (message.text == "Контакты"):
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="ну тут как бы кому надо, у всех есть мой номер так что можешь уйти", reply_markup=markup)

    elif (message.text == "Каталог"):
        bot.send_message(message.chat.id, text="Ну подики, жижечки там здесь)")
        message.text = catalog_devices(message)

    elif (message.text == "Возможности"):
        bot.send_message(message.chat.id, "Тут будет писок чего нибудь того что я умею")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Можешь вернуться", reply_markup=markup)

    elif message.text == "Вернуться в главное меню":
        bot.send_message(message.chat.id, text="Привет, спасибо что посетил нашего бота!")
        btn1 = types.KeyboardButton("Каталог")
        btn2 = types.KeyboardButton("Контакты")
        btn3 = types.KeyboardButton("Возможности")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Ну давай выбирай", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, text="Напииш ч")
# g
def catalog_devices(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton("Вернуться в главное меню")
    markup.add(back)
    bot.send_message(message.chat.id, text="Вы сейчас реально попали в каталог", reply_markup=markup)
    if message.text == 'Вернуться в главное меню':
        return message
bot.polling(none_stop=True, interval=0)