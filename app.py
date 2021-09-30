import telebot
import requests
import json
from config import TOKEN, value
from clases import MoneyPrice, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты, цену которой хотите узнать> \
    <имя валюты, в которой надо узнать цену первой валюты>\n \
    <количество первой валюты> \n Увидить список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands='values')
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for v in value.keys():
        text = '\n'.join((text, v, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types='text', )
def convert(message: telebot.types.Message):
    try:
        val = message.text.split(' ')
        if len(val) != 3:
            raise APIException('Параметров не нужное колличество!!')

        base, quote, amount = val
        total = MoneyPrice.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена{amount} {base} в {quote} равна: {total} '
        bot.send_message(message.chat.id, text)



bot.polling()
