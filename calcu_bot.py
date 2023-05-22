import telebot
import requests
from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
# from datetime import datetime


TOKEN = 'x'


TIME_KEY = 'x'


WEATHER_KEY = 'x'


bot = telebot.TeleBot(TOKEN)


Status = InlineKeyboardButton(text='Status', url='https://t.me/LegendBotsNews')
Projects = InlineKeyboardButton(text='Projects', url='https://t.me/NullLegend01')
channels = InlineKeyboardMarkup([[Projects,Status]])

# /start

@bot.message_handler(commands=['start'])

@bot.message_handler(func = lambda message: '/start' in message.text)

def start_message(message):
    username = message.from_user.username
    first_name = message.from_user.first_name

    bot.send_message(message.chat.id, f"Hello dear {first_name}!\nI'm Calculator - Finder Bot.\n\nSend me a simple math expression to calculate it: /calculate\n\nReceive time of a city: /time\n\nReceive weather information of a city:\n/weather\n\nJoin our channel @NullLegend01\n\nUpdates and News @BotsUpdatesNews",reply_markup=channels)


# /calculate

@bot.message_handler(commands=['calculate'])
@bot.message_handler(func=lambda message: '/calculate' in message.text)
def evaluate_expression(message):
    bot.send_message(message.chat.id ,"Please send me a math expression: ")
    bot.register_next_step_handler(message, process_expression)
def process_expression(message):
    try:
        process_expression = message.text
        result = eval(process_expression)
        bot.reply_to(message,f"{process_expression} = {result}")
    except:
        calculateError = 'Note that you can just send English numbers and [+][-][/][*] characters.\nPlease try again: /calculate'
        bot.reply_to(message, f"INVALID SYNTAX!\nExplain: {calculateError}")





# /time

@bot.message_handler(commands=['time'])
@bot.message_handler(func=lambda message: '/time' in message.text)
def get_time(message):
    bot.send_message(message.chat.id, "Please send me a city or country name: ")
    bot.register_next_step_handler(message, process_time)

def process_time(message):
    try:
        city = message.text
        response = requests.get(f'https://api.ipgeolocation.io/timezone?apiKey={TIME_KEY}&location={city}')
        data = response.json()
        time_str = data['time_24']
        bot.reply_to(message, f"Time in {city}: {time_str}")
    except:
        bot.reply_to(message, "City Not Found! Please try again: /time")


# /weather

@bot.message_handler(commands=['weather'])
@bot.message_handler(func=lambda message: '/weather' in message.text)
def get_weather(message):
    msg = bot.send_message(message.chat.id, "Please enter a city name:")
    bot.register_next_step_handler(msg, process_city_step)

def process_city_step(message):
    try:
        weather = message.text
        url = f'http://api.weatherapi.com/v1/current.json?key={WEATHER_KEY}&q={weather}&aqi=no'
        response = requests.get(url).json()

        if 'error' not in response:
            location = response['location']['name'] + ', ' + response['location']['region'] + ', ' + response['location']['country']
            temperature = response['current']['temp_c']
            weather_description = response['current']['condition']['text']
            humidity = response['current']['humidity']
            wind_speed = response['current']['wind_kph']

            weather_info = f'Weather in {location}:\n\nDescription: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind speed: {wind_speed} km/h'

            bot.send_message(message.chat.id, weather_info)
        else:
            bot.send_message(message.chat.id, 'City not found! Please try again: /weather')
    except Exception as e:
        bot.send_message(message.chat.id, 'Something went wrong. Please try again later.')


@bot.message_handler(commands = ['info'])
@bot.message_handler(func=lambda message: '/info' in message.text)
def info_message(message):
        bot.send_message(message.chat.id,"List of Tools and Services that I use:\n\nUsage\n-Find time & weather inforamtion\n-Calculate math expressions\n\nProgramming Language = Python\n\nLibrary = pyTelegramBotAPI\n\nHosting Service = PythonAnywhere\n\nDeveloper information: /developer")

t = InlineKeyboardButton(text="Telegram",url="https://telegram.me/NullLegend01")
ig = InlineKeyboardButton(text="Instagram",url="https://Instagram.com/nulllegend01")
yt = InlineKeyboardButton(text="YouTube",url="https://youtube.com/@NullLegend01")
gh = InlineKeyboardButton(text="GitHub",url="https://github.com/ArtinMoghadasi")
landingpage =InlineKeyboardButton(text="Socials & Links",url="https://zil.ink/ArtinMoghadasi")
dev = InlineKeyboardMarkup([[t,gh],[ig,yt],[landingpage]])

@bot.message_handler(commands = ['developer'])
@bot.message_handler(func=lambda message: '/developer' in message.text)
def developer_message(message):
    bot.send_message(message.chat.id,"I'm Developed by @NullLegend01\n\nIf you have any ideas or problems feel free to tell me @NullLegend\n\nTo see other projects & contact or collaborate with me use these links",reply_markup=dev)

helpbuttons = InlineKeyboardButton(text="Contact",url="https://t.me/NullLegend")
helpBTNHandler = InlineKeyboardMarkup([[helpbuttons]])
@bot.message_handler(commands = ['help'])
@bot.message_handler(func=lambda message: '/help' in message.text)
def help_message(message):
    bot.send_message(message.chat.id,"List of commands:\n/weather - Weather Information\n/time - Time finder\n/calculate - Calculator\n/info - Bot information\n/developer - Developer information\n/help - See this message again!\n\n-If you have any problem or ideas feel free to contact me @NullLegend",reply_markup=helpbuttons)


 



bot.polling()


















# /date

# @bot.message_handler(commands=['date'])

# @bot.message_handler(func=lambda message: '/date' in message.text)

# def date_message(message):

#     response = requests.get('http://www.w3.org/TR/2014/NOTE-calendar-api-20140114/')

#     data = response.json()

#     date_string = data

#     date = datetime.datetime.strptime(date_string, '%Y-%m-%d')

#     formatted_date = date.strftime('%m/%d/%Y')

#     bot.reply_to(message, "OK, Today's date: ")

#     bot.send_message(message.chat.id, formatted_date)


# @bot.message_handler(commands=['help'])
# @bot.message_handler(commands=['info'])
# @bot.message_handler(commands=['contact'])
# @bot.message_handler(commands=['date'])
# @bot.message_handler(commands=['advanced'])
# @bot.message_handler(commands=['currency'])

