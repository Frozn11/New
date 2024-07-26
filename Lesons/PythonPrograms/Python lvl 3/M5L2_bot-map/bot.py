import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import *
from logic import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который может показывать города на карте. Напиши /help для списка команд.")

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Доступные команды: \n\nстарт бота /start \n\nпоказывает город с указанным именем /show_city \n\nсохраняет название города /remember_city \n\nпоказывать список городов /show_my_cities \n\nпоказывать контур страны /line")
    # Допиши команды бота


@bot.message_handler(commands=['show_city'])
def handle_show_city(message):
    city_name = message.text.split()[-1]
    # Реализуй отрисовку города по запросу
    user_id = message.chat.id
    manager.create_grapf(f'{user_id}.png', [city_name])
    with open(f'{user_id}.png', 'rb') as map:
        bot.send_photo(user_id, map)


@bot.message_handler(commands=['line'])
def handle_remember_line(message):
    markup = InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton('контур', callback_data='line')
    button2 = telebot.types.InlineKeyboardButton('без контур', callback_data='noline')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, 'выберите хотите ли вы без контура или с контура карту', reply_markup=markup)

@bot.message_handler(commands=['remember_city'])
def handle_remember_city(message):
    user_id = message.chat.id
    city_name = message.text.split()[-1]
    if manager.add_city(user_id, city_name):
        bot.send_message(message.chat.id, f'Город {city_name} успешно сохранен!')
    else:
        bot.send_message(message.chat.id, 'Такого города я не знаю. Убедись, что он написан на английском!')

@bot.message_handler(commands=['show_my_cities'])
def handle_show_visited_cities(message):
    cities = manager.select_cities(message.chat.id)
    user_id = message.chat.id
    print(cities)
    # Реализуй отрисовку всех городов
    if cities:
        # Создание карты для всех городов
        manager.create_grapf(f'{user_id}.png', [cities])
        # Открытие и отправка карты
        with open(f'{user_id}.png', 'rb') as map:
            bot.send_photo(user_id, map)
        # отправка осуществляется с помощью метода send_photo
        return
    else:
        bot.send_message(message.chat.id, "У вас пока нет сохраненных городов.")

# @bot.callback_query_handler(func=lambda call: True)

# def callback_query(call):

#     if call.data == 'line':

#         bot.send_message(call.message.chat.id, 'контур')
#         gamemode[call.message.chat.id] += 1

#     elif call.data == 'noline':

#         bot.send_message(call.message.chat.id, 'без контур')
#         gamemode[call.message.chat.id] += 0


if __name__=="__main__":
    manager = DB_Map(DATABASE)
    bot.polling()
