import telebot
from config import token
# Задание 7 - испортируй команду defaultdict
from logic import quiz_questions, quiz_opsions, quiz_questions_games
from collections import defaultdict

user_responses = {} 
# Задание 8 - создай словарь points для сохранения количества очков пользователя

bot = telebot.TeleBot(token)
points = defaultdict(int)
gamemode = defaultdict(int)

def send_question(chat_id):
    try:
        bot.send_photo(chat_id, photo=open(quiz_questions[user_responses[chat_id]].photos, 'rb'))
    except Exception as e:
        print(f"no photo, Error message: {e}")
    bot.send_message(chat_id, quiz_questions[user_responses[chat_id]].text, reply_markup=quiz_questions[user_responses[chat_id]].gen_markup())

def send_opsions(chat_id):
    bot.send_message(chat_id, quiz_opsions[user_responses[chat_id]].text, reply_markup=quiz_opsions[user_responses[chat_id]].gen_markup())

def send_question_games(chat_id):
    try:   
        bot.send_chat_action(chat_id, 'typing')
        bot.send_photo(chat_id, photo=open(quiz_questions_games[user_responses[chat_id]].photos, 'rb'))
    except Exception as e:
        print(f"no photo, Error message: {e}")
    bot.send_message(chat_id, quiz_questions_games[user_responses[chat_id]].text, reply_markup=quiz_questions_games[user_responses[chat_id]].gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    if call.data == 'Games':
        bot.answer_callback_query(call.id, "Games")
        gamemode[call.message.chat.id] += 1
        send_question_games(call.message.chat.id)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        return
        
    elif call.data == "Memes":
        bot.answer_callback_query(call.id, "Memes")
        send_question(call.message.chat.id)
        gamemode[call.message.chat.id] += 0
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        return    
    
    elif call.data == "correct":
        bot.answer_callback_query(call.id, "Answer is correct")
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        points[call.message.chat.id] += 1
        # Задание 9 - добавь очки пользователю за правильный ответ
    elif call.data == "wrong":
        bot.answer_callback_query(call.id,  "Answer is wrong")
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        ## msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'{quiz_questions[user_responses[chat_id]].text}', reply_markup=None)
    # Задание 5 - реализуй счетчик вопросов

    user_responses[call.message.chat.id] += 1
    if gamemode[call.message.chat.id] == 1:
        if user_responses[call.message.chat.id] >= len(quiz_questions_games):
            bot.send_message(call.message.chat.id, f'The End, you got {points[call.message.chat.id]} points')
            gamemode[call.message.chat.id] = 0
            points[call.message.chat.id] = 0   
        else:
            bot.send_chat_action(call.message.chat.id, 'typing')
            send_question_games(call.message.chat.id)
    else:
        if user_responses[call.message.chat.id] >= len(quiz_questions):
            bot.send_message(call.message.chat.id, f'The End, you got {points[call.message.chat.id]} points')
            points[call.message.chat.id] = 0   
        else:
            bot.send_chat_action(call.message.chat.id, 'typing')
            send_question(call.message.chat.id)



        

    # Задание 6 - отправь пользователю сообщение с количеством его набранных очков, если он ответил на все вопросы, а иначе отправь следующий вопрос




@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id:
        user_responses[message.chat.id] = 0
        gamemode[message.chat.id] = 0
        send_opsions(message.chat.id)


bot.infinity_polling()
