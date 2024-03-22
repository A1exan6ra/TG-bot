import telebot 
from telebot import types
from glob import glob 
from random  import choice
import datetime

token = '6770044295:AAFO6JMj4L99gRYWUa3_hiVOSkZqr8sH0bY'

bot=telebot.TeleBot(token)# 1 бот 


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(message.from_user), reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True))


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, text = "Список используемых команд:\n"
                                            "/help - помощь\n"
                                            "/start - начать работу\n"
                                            "/postcards_on - включение отправки открыток\n"
                                            "/postcards_off - выключение отправки открыток\n"
                                            "/day_of_death - команда дата смерти")


@bot.message_handler(commands=['postcards_on'])
def turn_on_postcards(message):
    pic = choice(glob('img/c*.jpg'))
    bot.send_photo(chat_id=message.chat.id, photo=open(pic, 'rb'))
    bot.send_message(message.chat.id, text = "Отправка открыток запущена")


@bot.message_handler(commands=['postcards_off'])
def turn_on_postcards(message):
    bot.send_message(message.chat.id, text = "Отправка открыток преостановлена")


@bot.message_handler(commands=['day_of_death'])
def day_of_death(message):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    bot.send_message(message.chat.id, f"Ты умрёшь: {date}")


bot.polling(none_stop=True)