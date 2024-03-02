"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

import logging
import ephem


from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters



logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Доброго времени суток тебе, пользователь!')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def get_name_planet(update, context):
    # locale.setlocale(locale.LC_TIME, 'ru_RU.UTF8')
    # date = datetime.date.today()
    date = datetime.now().strftime("%Y/%d/%m")
    user_text = update.message.text
    print(user_text)
    planet_name = user_text.split()[1].capitalize()
    if planet_name == 'Sun':
        planet_name = ephem.Sun(date)
        planet_constellation = ephem.constellation(planet_name)
    elif planet_name == 'Mercury':
        planet_name = ephem.Mercury(date)
        planet_constellation = ephem.constellation(planet_name)
    elif planet_name == 'Venus':
        planet_name = ephem.Venus(date)
        planet_constellation = ephem.constellation(planet_name)
    elif planet_name == 'Earth':
        planet_name = ephem.Earth(date)
        planet_constellation = ephem.constellation(planet_name)
    elif planet_name == 'Moon':
        planet_name = ephem.Moon(date)
        planet_constellation = ephem.constellation(planet_name)
    elif planet_name == 'Mars':
        planet_name = ephem.Mars(date)
        planet_constellation = ephem.constellation(planet_name)
    elif planet_name == 'Jupiter':
        planet_name = ephem.Jupiter(date)
        planet_constellation = ephem.constellation(planet_name)
    elif planet_name == 'Saturn':
        planet_name = ephem.Saturn(date)
        planet_constellation = ephem.constellation(planet_name)
    elif planet_name == 'Uranus':
        planet_name = ephem.Uranus(date)
        planet_constellation = ephem.constellation(planet_name)
    elif planet_name == 'Neptune':
        planet_name = ephem.Neptune(date)
        planet_constellation = ephem.constellation(planet_name)
    elif planet_name == 'Pluto':
        planet_name = ephem.Pluto(date)
        planet_constellation = ephem.constellation(planet_name)
    else:
        planet_constellation = 'Не знаю.'

    planet_name = str(planet_name).split()[1]
    update.message.reply_text(f'{planet_name} - хороший выбор планеты!')
    update.message.reply_text(f'{planet_name} - {date} находится в данном созвездии: {planet_constellation}')


def main():
    mybot = Updater("TOKEN", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_name_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот начал работу")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
