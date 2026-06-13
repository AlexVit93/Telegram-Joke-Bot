import telebot
import requests
import random
from bs4 import BeautifulSoup as b

URL = 'http://anekdotov.net/anekdot/'
TOKEN = ''


def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdotis = soup.find_all('div', class_='anekdot')
    return [c.text for c in anekdotis]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Чтобы быть в теме, введите цифру: ')

@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Привет! Чтобы быть в теме, введите цифру: ')


bot.polling(none_stop=True)


