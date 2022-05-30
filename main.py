import telebot
from telebot import types
import pandas as pd

# http://t.me/movies_revenue_prediction_bot

token = '5216695845:AAFwPhtMXamZYg-nF7HqPplgv4KhJvGeW6k'
bot = telebot.TeleBot(token)

durl='https://www.dropbox.com/s/m7z8uj88smjjhd4/movies_raw_dataset.csv?dl=0'
data1 =pd.read_csv('movies1.csv', delimiter=',', names=['id','belongs_to_collection','budget','genres','homepage','imdb_id','original_language','original_title','overview','popularity','poster_path','production_companies','production_countries','release_date','runtime','spoken_languages','status','tagline','title','Keywords','cast','crew','revenue'])


@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id,
                     'Привет!')

@bot.message_handler(commands=['stop'])
def cmd_start(message):
    bot.send_message(message.chat.id,
                     'Пока!')


@bot.message_handler(commands=['help'])
def cmd_help(message):
    bot.send_message(message.chat.id,
                     'Привет! Я помогу тебе разобраться в моей работе. У меня есть следующие команды: \n \n'
                     '/dataset_info - получить информацию о наборе данных \n'
                     '/models_info - получить описание моделей')


@bot.message_handler(commands=['dataset_info'])
def cmd_dataset_info(message):
    bot.send_message(message.chat.id, 'Dataset доступен по ссылке ' + durl + ' и состоит из полей:')
    bot.send_message(message.chat.id, str(data1.columns.tolist()))
    bot.send_message(message.chat.id, str(data1.describe()))

@bot.message_handler(commands=['top5'])
def cmd_top5(message):
    user_markup = types.ReplyKeyboardMarkup()
    b_button = types.KeyboardButton("По вложенному бюджету")
    p_button = types.KeyboardButton("По популярности")
    r_button = types.KeyboardButton("По длительности фильма")
    user_markup.row(b_button, p_button, r_button)
    bot.send_message(message.chat.id, "ТОП-5 фильмов! Выбери нужную сортировку!", reply_markup=user_markup)

def cmd_top5_link(message):
    if message.text == "По вложенному бюджету":
        data2 = data1.sort_values(by="budget", ascending=False)
        return str(data2.head()[['budget', 'original_title']])
    elif message.text == "По популярности":
        data2 = data1.sort_values(by="popularity", ascending=False)
        return str(data2.head()[['popularity', 'original_title']])
    elif message.text == "По длительности фильма":
        data2 = data1.sort_values(by="runtime", ascending=False)
        return str(data2.head()[['runtime', 'original_title']])
    else:
        return "Something went wrong"

@bot.message_handler(content_types=["text"])
def cmd_top5_reply(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, cmd_top5_link(message), reply_markup=markup)


if __name__ == '__main__':
    bot.infinity_polling()