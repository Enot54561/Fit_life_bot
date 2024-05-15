import telebot
from telebot import types

import cal_weight
import config

API_TOKEN = config.API_TOKEN
channel_id = config.channel_id
bot = telebot.TeleBot(API_TOKEN)
begin_text = config.beginning_text
height = 0
weight = 0


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def start(message):
    text_message = f'<b><i>Привет,{message.from_user.first_name}!</i></b> \n\n' + begin_text
    markup_inline = types.InlineKeyboardMarkup()
    item_dowload = types.InlineKeyboardButton(text="Скачть гайд", callback_data='download')
    item_calc = types.InlineKeyboardButton(text="Расчитать БЖУ", callback_data='calc')
    markup_inline.add(item_dowload, item_calc)

    bot.send_message(message.chat.id, text_message, parse_mode='HTML', reply_markup=markup_inline)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Для возврата в стартовое меню бота нажмите /start")


def check_member(call):
    user_id = call.from_user.id
    try:
        chat_member = bot.get_chat_member(channel_id, user_id)
        if chat_member.status != 'left':
            return 1
        else:
            return 2
    except Exception as e:
        return 3


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'download':
            if check_member(call) == 1:
                with open('file/123.txt', 'rb') as doc:
                    bot.send_document(call.message.chat.id, document=open('file/123.txt', 'rb'))
            elif check_member(call) == 2:
                bot.send_message(call.message.chat.id,
                                 "Вы не подписаны на канал @fit_life_world.\n\n"
                                 "Пожалуйста, подпишитесь, чтобы продолжить.")
            elif check_member(call) == 3:
                bot.send_message(call.message.chat.id, "При проверке ыозникла ошибка. Попробуйте позже")
        if call.data == 'calc':
            msg1 = bot.send_message(call.message.chat.id, "Введите ваш рост в см.")
            bot.register_next_step_handler(msg1, msg2)
    bot.answer_callback_query(callback_query_id=call.id, show_alert=False)


def msg2(message):
    try:
        var1 = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, "Вы ввели не число. Начните с начала\n"
                                          "Нажмите /start")
    if type(var1) == int:
        global height
        height = var1
        msg3 = bot.send_message(message.chat.id, "Введите ваш вес")
        bot.register_next_step_handler(msg3, msg4)


def msg4(message):
    try:
        var1 = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, "Вы ввели не число. Начните с начала\n"
                                          "Нажмите /start")
    if type(var1) == int:
        global weight
        weight = var1
        res = str(cal_weight.calc_weight(height, weight))
        bot.send_message(message.chat.id, res)


if __name__ == '__main__':
    print("Бот запущен")

bot.infinity_polling()
