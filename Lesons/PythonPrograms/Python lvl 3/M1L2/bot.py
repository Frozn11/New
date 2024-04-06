from settings import TOKEN
import random
import telebot
import telebot.ext

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\\
""")
    
s_city = None

@bot.message_handler(commands=['quote'])
def joke_handler(message):
    quote = ["Лето — это время года, когда очень жарко, чтобы заниматься вещами, которыми заниматься зимой было очень холодно.", "Нет ничего более раздражающего, чем хороший пример." , "Тот, кто не читает хороших книг, не имеет преимуществ перед человеком, который не умеет читать их.", "Любое упоминание в прессе, даже самое негативное, кроме некролога, это реклама." , "Прощение — это аромат, который фиалка дарит тому, кто её растоптал."]
    quote_replay = random.choice(quote)
    bot.reply_to(message, quote_replay)
    
bot.infinity_polling()