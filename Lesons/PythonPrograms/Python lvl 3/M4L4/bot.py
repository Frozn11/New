from logic import DB_Manager
from config import *
from telebot import TeleBot
import secrets
import os
from moviepy.editor import VideoFileClip

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Я бот-менеджер проектов
Помогу тебе сохранить твои проекты и информацию о них!) 
""")

@bot.message_handler(['weather'])
def wather_command(message):
    wather_info = 'да'
    bot.send_message(message.chat.id, {wather_info})
    

@bot.message_handler(['convert'])
def convert_command(message):

    bot.send_message(message.chat.id, "отправти видео")

    bot.register_next_step_handler(message, convert_vid)

@bot.message_handler(content_types=['video'])
def convert_vid(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        file_id = message.video.file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        simvols = "+-!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        random_name = ""
        for i in range(15):
            random_name += ''.join(secrets.choice(simvols))
        print(random_name)
        with open(f'vid/{random_name}.mp4', 'wb') as f:
            f.write(downloaded_file)
        file_stat = os.stat(f'vid/{random_name}.mp4')
        note = VideoFileClip(f'vid/{random_name}.mp4')
        width, height = note.size
        print(f"Resolution: {width}x{height}")
        note.close()
        if file_stat.st_size < 4933902 and width == 384 and height == 384:
            with open(f'vid/{random_name}.mp4', 'rb') as video:
                # print(message)
                bot.send_video_note(message.chat.id, video)
            os.remove(f'vid/{random_name}.mp4')
        else:
            os.remove(f'vid/{random_name}.mp4')
            bot.send_message(message.chat.id, "Разрешение видео не должно быть больше чем 384x384 и видео не должно быть слишком длинная(не больше минуты) и видео не может быть больше чем 4,9MB")
            # bot.send_message(message.chat.id, "dummass the file is too big or the resolution is wrong and the video can't be over a minute(the file can't be bigger than 4.9 MB and resolution must be 384x384)")
    except Exception as e:
        # print(e)
        bot.send_message(message.chat.id, "Разрешение видео не должно быть больше чем 384x384 и видео не должно быть слишком длинная(не больше минуты) и видео не может быть больше чем 4,9MB")
        try:
            os.remove(f'vid/{random_name}.mp4')
        except:
            pass  
        


if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.infinity_polling()