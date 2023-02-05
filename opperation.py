import telebot
import re

TOKEN = "5831329247:AAFTrRtZUiEtxAz2t3SINEr_QdIy33QzkFs"
bot = telebot.TeleBot(TOKEN)


def sumcalc(message):
    try:
        number1, number2 = re.split(' ', message.text, maxsplit=1)
        try:
            number1 = float(number1)
            try:
                number2 = float(number2)
                bot.send_message(
                    message.from_user.id,'Сумма двоих введённых тобой чисел равна - ' +str(number1 + number2))
            except Exception:
                bot.send_message(
                    message.from_user.id,'Вы ввели данные не в правильном формате.\nВы ввели не число.')
        except Exception:
            bot.send_message(message.from_user.id,
                'Вы ввели данные не в правильном формате.\nВы ввели не число.')
    except Exception:
        bot.send_message(
            message.from_user.id,
            'Вы ввели данные не в правильном формате.\n*Будьте внимательны*, ввод должен быть формата *"*число * * число*"*.',
            parse_mode='Markdown')


def minus(message):
    try:
        number1, number2 = re.split(' ', message.text, maxsplit=1)
        try:
            number1 = float(number1)
            try:
                number2 = float(number2)
                bot.send_message(
                    message.from_user.id,'Разность двоих введённых тобой чисел равна - ' +str(number1 - number2))
            except Exception:
                bot.send_message(
                    message.from_user.id,'Вы ввели данные не в правильном формате.\nВы ввели не число.')
        except Exception:
            bot.send_message(message.from_user.id,
                'Вы ввели данные не в правильном формате.\nВы ввели не число.')
    except Exception:
        bot.send_message(
            message.from_user.id,
            'Вы ввели данные не в правильном формате.\n*Будьте внимательны*, ввод должен быть формата *"*число * * число*"*.',
            parse_mode='Markdown')
        

def multiply(message):
    try:
        number1, number2 = re.split(' ', message.text, maxsplit=1)
        try:
            number1 = float(number1)
            try:
                number2 = float(number2)
                bot.send_message(
                    message.from_user.id,'Произведение двоих введённых тобой чисел равна - ' +str(number1 * number2))
            except Exception:
                bot.send_message(
                    message.from_user.id,'Вы ввели данные не в правильном формате.\nВы ввели не число.')
        except Exception:
            bot.send_message(message.from_user.id,
                'Вы ввели данные не в правильном формате.\nВы ввели не число.')
    except Exception:
        bot.send_message(
            message.from_user.id,
            'Вы ввели данные не в правильном формате.\n*Будьте внимательны*, ввод должен быть формата *"*число * * число*"*.',
            parse_mode='Markdown')
        

def degree(message):
    try:
        number1, number2 = re.split(' ', message.text, maxsplit=1)
        try:
            number1 = float(number1)
            try:
                number2 = float(number2)
                bot.send_message(
                    message.from_user.id,'Частное двоих введённых тобой чисел равна - ' +str(number1 / number2))
            except Exception:
                bot.send_message(
                    message.from_user.id,'Вы ввели данные не в правильном формате.\nВы ввели не число.')
        except Exception:
            bot.send_message(message.from_user.id,
                'Вы ввели данные не в правильном формате.\nВы ввели не число.')
    except Exception:
        bot.send_message(
            message.from_user.id,
            'Вы ввели данные не в правильном формате.\n*Будьте внимательны*, ввод должен быть формата *"*число * * число*"*.',
            parse_mode='Markdown')
        

def degree_integer(message):
    try:
        number1, number2 = re.split(' ', message.text, maxsplit=1)
        try:
            number1 = float(number1)
            try:
                number2 = float(number2)
                bot.send_message(
                    message.from_user.id,'Целочисленное частное двоих введённых тобой чисел равна - ' +str(number1 // number2))
            except Exception:
                bot.send_message(
                    message.from_user.id,'Вы ввели данные не в правильном формате.\nВы ввели не число.')
        except Exception:
            bot.send_message(message.from_user.id,
                'Вы ввели данные не в правильном формате.\nВы ввели не число.')
    except Exception:
        bot.send_message(
            message.from_user.id,
            'Вы ввели данные не в правильном формате.\n*Будьте внимательны*, ввод должен быть формата *"*число * * число*"*.',
            parse_mode='Markdown')
        
def degree_remainder(message):
    try:
        number1, number2 = re.split(' ', message.text, maxsplit=1)
        try:
            number1 = float(number1)
            try:
                number2 = float(number2)
                bot.send_message(
                    message.from_user.id,'Получение остатка от частного двоих введённых тобой чисел равна - ' +str(number1 % number2))
            except Exception:
                bot.send_message(
                    message.from_user.id,'Вы ввели данные не в правильном формате.\nВы ввели не число.')
        except Exception:
            bot.send_message(message.from_user.id,
                'Вы ввели данные не в правильном формате.\nВы ввели не число.')
    except Exception:
        bot.send_message(
            message.from_user.id,
            'Вы ввели данные не в правильном формате.\n*Будьте внимательны*, ввод должен быть формата *"*число * * число*"*.',
            parse_mode='Markdown')
        

# def main_menu(message):
#     global keyboard
#     if message.text == "Рациональный":
#         bot.send_message(message.chat.id, "Рациональный режим работы")
#         bot.register_next_step_handler(message, keyboard_op)

#     elif message.text == "Комплексный":
#         bot.send_message(message.chat.id, "Комплексный режим работы")