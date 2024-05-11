# Задание 2 - Импортируй нужные классы
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class Question:

    def __init__(self, photos, text, answer_id, *options):
        self.__text = text
        self.__photos = photos
        self.__answer_id = answer_id
        self.options = options


    # Задание 1 - Создай геттер для получения текста вопроса
    @property 
    def text(self):
        return self.__text

    @property
    def photos(self):
        return self.__photos

    def gen_markup(self):
        # Задание 3 - Создай метод для генерации Inline клавиатуры
        markup = InlineKeyboardMarkup()
        markup.row_width = len(self.options)

        for i, option in enumerate(self.options):
            # Если порядковый номер ответа - номер правильного ответа, то:
            if i == self.__answer_id:
                markup.add(InlineKeyboardButton(option, callback_data='correct'))
            else:
                markup.add(InlineKeyboardButton(option, callback_data='wrong'))
        return markup

# Задание 4 - заполни список своими вопросами

quiz_questions = [
    Question("None","Что котики делают, когда никто их не видит?", 1, "Спят", "Пишут мемы"),
    Question("None","Как котики выражают свою любовь?", 0, "Громким мурлыканием", "Отправляют фото на Instagram", "Гавкают"),
    Question("images/image1.png","Это кошка?", 0, "да", "нет"),
    Question("None","Какие книги котики любят читать?", 3, "Обретение вашего внутреннего урр-мирения", "Тайм-менеджмент или как выделить 18 часов в день для сна", "101 способ уснуть на 5 минут раньше, чем хозяин", "Пособие по управлению людьми")
]
