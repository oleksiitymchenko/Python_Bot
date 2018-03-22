import json

import apiai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import GetShedule

updater = Updater(token='379622667:AAG9JvSMl-LuttVSxBfwqRUCEdkkqxbe4nM')
dispatcher = updater.dispatcher

def start( bot, update ):
    bot.send_message(chat_id=update.message.chat_id, text="Привет, Я говорящая картошка")

def mondayMessage(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=GetShedule.dayShedule(1))

def tuesdayMessage(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=GetShedule.dayShedule(2))

def wednesdayMessage(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=GetShedule.dayShedule(3))

def thursdayMessage( bot, update ):
    bot.send_message(chat_id=update.message.chat_id, text=GetShedule.dayShedule(4))

def fridayMessage(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=GetShedule.dayShedule(5))

def saturdayMessage(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=GetShedule.dayShedule(6))


def textmessage( bot, update ):
    request = apiai.ApiAI('b54f55d0e85b4548886e880fdfe89c71').text_request()
    request.lang = 'ru'
    request.session_id = 'PotatoAiBot'
    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Я вас не понял чуть менее чем полностью')


def main():
    start_handler = CommandHandler('start', start)
    textmessage_handler = MessageHandler(Filters.text, textmessage)
    monday_handler = CommandHandler('monday',mondayMessage)
    tuesday_handler = CommandHandler('tuesday',tuesdayMessage)
    wednesday_handler = CommandHandler('wednesday', wednesdayMessage)
    thursday_handler = CommandHandler('thursday', thursdayMessage)
    friday_handler = CommandHandler('friday', fridayMessage)
    saturday_handler = CommandHandler('saturday', saturdayMessage)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(textmessage_handler)
    dispatcher.add_handler(monday_handler)
    dispatcher.add_handler(tuesday_handler)
    dispatcher.add_handler(wednesday_handler)
    dispatcher.add_handler(thursday_handler)
    dispatcher.add_handler(friday_handler)
    dispatcher.add_handler(saturday_handler)
    updater.start_polling(timeout=100, poll_interval=0.5)
    updater.idle()


if __name__ == '__main__':
    main()
