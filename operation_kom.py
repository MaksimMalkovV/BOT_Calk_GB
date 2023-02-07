import telebot
import re
import bot_GB 
import telebot

TOKEN = "5831329247:AAFTrRtZUiEtxAz2t3SINEr_QdIy33QzkFs"
bot_GB = telebot.TeleBot(TOKEN)

def sumcalc_kom(message):
    try:
        number1, number2 = re.split(' ', message.text, maxsplit=1)
        try:
            number1 = complex(number1)
            try:
                number2 = complex(number1)
                bot_GB.send_message(
                    message.from_user.id,
                    'Сумма двоих введённых тобой чисел равна - ' +
                    str(number1 + number2))
            except Exception:
                bot_GB.send_message(
                    message.from_user.id,
                    'Вы ввели данные не в правильном формате.\nВы ввели не число.'
                )
        except Exception:
            bot_GB.send_message(
                message.from_user.id,
                'Вы ввели данные не в правильном формате.\nВы ввели не число.')
    except Exception:
        bot_GB.send_message(
            message.from_user.id,
            'Вы ввели данные не в правильном формате.\n*Будьте внимательны*, ввод должен быть формата *"*число * * число*"*.',
            parse_mode='Markdown')
        
def minus_kom(message):
    try:
        number1, number2 = re.split(' ', message.text, maxsplit=1)
        try:
            number1 = complex(number1)
            try:
                number2 = complex(number1)
                bot_GB.send_message(
                    message.from_user.id,
                    'Разность двоих введённых тобой чисел равна - ' +
                    str(number1 + number2))
                bot_GB.start
            except Exception:
                bot_GB.send_message(
                    message.from_user.id,
                    'Вы ввели данные не в правильном формате.\nВы ввели не число.'
                )
        except Exception:
            bot_GB.send_message(
                message.from_user.id,
                'Вы ввели данные не в правильном формате.\nВы ввели не число.')
    except Exception:
        bot_GB.send_message(
            message.from_user.id,
            'Вы ввели данные не в правильном формате.\n*Будьте внимательны*, ввод должен быть формата *"*число * * число*"*.',
            parse_mode='Markdown')

def multiply_kom(message):
    try:
        number1, number2 = re.split(' ', message.text, maxsplit=1)
        try:
            number1 = complex(number1)
            try:
                number2 = complex(number1)
                bot_GB.send_message(
                    message.from_user.id,
                    'Произведение двоих введённых тобой чисел равна - ' +
                    str(number1 + number2))
            except Exception:
                bot_GB.send_message(
                    message.from_user.id,
                    'Вы ввели данные не в правильном формате.\nВы ввели не число.'
                )
        except Exception:
            bot_GB.send_message(
                message.from_user.id,
                'Вы ввели данные не в правильном формате.\nВы ввели не число.')
    except Exception:
        bot_GB.send_message(
            message.from_user.id,
            'Вы ввели данные не в правильном формате.\n*Будьте внимательны*, ввод должен быть формата *"*число * * число*"*.',
            parse_mode='Markdown')
    
def degree_kom(message):
    try:
        number1, number2 = re.split(' ', message.text, maxsplit=1)
        try:
            number1 = complex(number1)
            try:
                number2 = complex(number1)
                bot_GB.send_message(
                    message.from_user.id,
                    'Частное двоих введённых тобой чисел равна - ' +
                    str(number1 + number2))
            except Exception:
                bot_GB.send_message(
                    message.from_user.id,
                    'Вы ввели данные не в правильном формате.\nВы ввели не число.'
                )
        except Exception:
            bot_GB.send_message(
                message.from_user.id,
                'Вы ввели данные не в правильном формате.\nВы ввели не число.')
    except Exception:
        bot_GB.send_message(
            message.from_user.id,
            'Вы ввели данные не в правильном формате.\n*Будьте внимательны*, ввод должен быть формата *"*число * * число*"*.',
            parse_mode='Markdown')