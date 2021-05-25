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
import logging, ephem, datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# PROXY = {
#     'proxy_url': 'socks5://t1.learn.python.ru:1080',
#     'urllib3_proxy_kwargs': {
#         'username': 'learn',
#         'password': 'python'
#     }
# }


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def planet(update, context):
    planet = update.message.text.split()
    if "mercury" in planet:
      mercury = ephem.Mercury(datetime.date.today())
      planet = ephem.constellation(mercury)
    else:
      if "venus"in planet:
        venus = ephem.Venus(datetime.date.today())
        planet = ephem.constellation(venus)
      else:
          if 'earth' in planet:
            earth = ephem.Earth(datetime.date.today())
            planet = ephem.constellation(earth)
          else:
              if 'mars'in planet:
                mars = ephem.Mars(datetime.date.today())
                planet = ephem.constellation(mars)
              else:
                  if 'jupiter' in planet:
                    jupiter = ephem.Jupiter(datetime.date.today())
                    planet = ephem.constellation(jupiter)
                  else:
                      if 'saturn' in planet:
                        saturn = ephem.Saturn(datetime.date.today())
                        planet = ephem.constellation(saturn)
                      else:
                          if 'uranus' in planet:
                            uranus = ephem.Uranus(datetime.date.today())
                            planet = ephem.constellation(uranus)
                          else:
                              if 'neptune'in planet:
                                neptune = ephem.Neptune(datetime.date.today())
                                planet = ephem.constellation(neptune)
                              else:
                                  planet = 'unknown planet'
     
    update.message.reply_text(planet)
    
    
def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater("1887880943:AAHVX6-ECQ5RpoWBuMsN9Y5PhGh0rwuHwow", use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
