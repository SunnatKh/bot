import telebot
import cont

bot = telebot.TeleBot('')

#  bot.send_message(asd, "sdf")

print(bot.get_me())

a = 42
b = "qwerty"
print(type(a), type(b))


def log(message, answer):
    print("\n ~~~~~")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}.(id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print(answer)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, """Чем Вам помочь?""")


@bot.message_handler(commands=['start'])  # команда#
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)  # клавиатура#
    user_markup.row('/start', '/stop')
    user_markup.row('Фото', 'Аудио', 'Документы')
    user_markup.row('Стикер', 'Видео', 'Голос', 'Локации', 'aЛокации')
    user_markup.row('12', '3', '23', '122')
    user_markup.row('122', '43', '423', '122')
    user_markup.row('121', '33', '323', '3122')
    user_markup.row('1212', '13', '223', '2122')
    user_markup.row('1221', '23', '123', '1122')

    bot.send_message(message.from_user.id, "Добро пожаловать...", reply_markup=user_markup)


@bot.message_handler(commands=['stop'])  # команда#
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardMarkup()
    bot.send_message(message.from_user.id, "....", reply_markup=hide_markup)  # убираем клавиатуру#


bot.polling(none_stop=True, interval=0)
