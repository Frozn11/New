import telebot
from setting import token


def main(token):
  thai_bot = telebot.telebot(token)
  thai_bot.polling()
  print(f'Start bot {token}')

if __name__ == '__main__':
 main(token)