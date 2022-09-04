from telegram.ext import Updater, CommandHandler
import requests


url = 't.me/MontenegroDrive_bot'
data = requests.get(url) # requests data from API
data = data.json() # converts return data to json

# Retrieve values from API
curr_temp = data['curr_temp']
cad_rate = data['usd_rates']['CAD']
eur_rate = data['usd_rates']['EUR']
zar_rate = data['usd_rates']['ZAR']


def return_weather():
    return'Hello. The current temperature in Cape Town is: '+str(curr_temp)+" celsius."

def return_rates():
    return "Hello. Today, USD conversion rates are as follows: USD->CAD = "+str(cad_rate)+ ", USD->EUR = "+str(eur_rate)+", USD->ZAR = "+str(zar_rate)

def weather(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=return_weather())

def currency(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=return_rates())

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hi! I respond to /weather and /currency. Try these!')

def main():
    import os
    TOKEN = os.getenv('BOTAPIKEY')
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    weather_handler = CommandHandler('weather', weather)
    currency_handler = CommandHandler('currency',currency)
    start_handler = CommandHandler('start',start)

    dispatcher.add_handler(weather_handler)
    dispatcher.add_handler(currency_handler)
    dispatcher.add_handler(start_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()

