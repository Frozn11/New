#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from config import *
from logic import Text2ImageAPI
import os
bot = telebot.TeleBot(TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Напиши мне промп, чтобы я отправил сгенерированную картинк")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    message_send = bot.send_message(message.chat.id, 'Генерирую картинку...')
    name_file = 'yeah.png'
    prompt = message.text
    bot.send_chat_action(message.chat.id, 'typing')
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', API_TOKEN, SECRET_KEY)
    model_id = api.get_model()
    uuid = api.generate(prompt, model_id)
    images = api.check_generation(uuid)[0]
    api.save_image(images, 'yeah.png')
    with open(name_file, 'rb') as photo:
        bot.delete_message(message.chat.id, message_send.message_id)
        bot.send_photo(message.chat.id, photo)
    os.remove(name_file)
bot.infinity_polling()