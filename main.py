import requests
import telebot

# http://t.me/movies_revenue_prediction_bot

token = '5216695845:AAFwPhtMXamZYg-nF7HqPplgv4KhJvGeW6k'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def cmd_start(message):



@bot.message_handler(commands=['help'])
def cmd_help(message):



@bot.message_handler(commands=['dataset_info'])
def cmd_dataset_info(message):



@bot.message_handler(commands=['models_info'])
def cmd_models_info(message):