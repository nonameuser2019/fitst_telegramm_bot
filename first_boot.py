from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
from setting import TOKEN
from new_post_api import URL
from new_post_api import get_api

logging.basicConfig(format = '%(asctime)s - %(levelname)s  - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(bot, update):
    logging.info('user used /start')
    text = 'Вызван /start'

    update.message.reply_text(text) # отвечаем юсеру в телеграмм на команду start


def talk_to_me(bot, update):
    user_text = 'Привет {} ты написал {}'.format(update.message.chat.first_name ,update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.first_name, update.message.chat.id,
                 update.message.text)
    update.message.reply_text(user_text)# отвечает сообщение назад пользователю

def planet(bot, update):
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.first_name, update.message.chat.id,
                 update.message.text)
    planet = update.message.text.split()
    print(planet[1])
    const = ephem.Mars('05/10/2019')
    print(ephem.constellation(const))
    update.message.reply_text(ephem.constellation(const))


def tracking_new_post(bot, update):
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.first_name, update.message.chat.id,
                 update.message.text)
    user_info = update.message.text.split()
    print(user_info)
    try:
        if len(user_info[1]) == 11 or len(user_info[1]) == 14 :
            return_message = get_api(URL,user_info[1])
            update.message.reply_text(return_message)
        else:
            update.message.reply_text('Вы ввели не коректный номер отслеживания, номер отслеживания должен '
                                      'состоять из 11 или 14 цифр, повторите пожалуйста ввод.')
    except:
        update.message.reply_text('Введенный номер отслеживания не корректен, проверьте его и попробуйте снова')



def main():
    mybot = Updater(TOKEN) # передаем ключ

    logging.info('Bot is running')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(CommandHandler('t',tracking_new_post))

    mybot.start_polling() # бот начинает ломится в телеграмм
    mybot.idle() # будет работать бот пока мы его не остановим



if __name__=='__main__':
    main()

