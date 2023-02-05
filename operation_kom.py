import telebot
import re

TOKEN = "5831329247:AAFTrRtZUiEtxAz2t3SINEr_QdIy33QzkFs"
bot = telebot.TeleBot(TOKEN)

# Надо сделать комплекс
def sumcalc(message):
    try:
        number1, number2 = re.split(' ', message.text, maxsplit=1)
        try:
            number1 = float(number1)
            try:
                number2 = float(number2)
                bot.send_message(
                    message.from_user.id,
                    'Сумма двоих введённых тобой чисел равна - ' +
                    str(number1 + number2))
            except Exception:
                bot.send_message(
                    message.from_user.id,
                    'Вы ввели данные не в правильном формате.\nВы ввели не число.'
                )
        except Exception:
            bot.send_message(
                message.from_user.id,
                'Вы ввели данные не в правильном формате.\nВы ввели не число.')
    except Exception:
        bot.send_message(
            message.from_user.id,
            'Вы ввели данные не в правильном формате.\n*Будьте внимательны*, ввод должен быть формата *"*число * * число*"*.',
            parse_mode='Markdown')