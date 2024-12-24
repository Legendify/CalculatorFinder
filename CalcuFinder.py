import telebot
import requests
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telebot.types import Message

API_TOKEN = '5802882726:AAGN2LnDv_7IYYZyvDAc40kEQRrjQVXMnW0'

TIME_KEY = '8389a060b23a4bda9bff870bcd62d57d'

WEATHER_KEY = 'a4a3d96ee2e4437cacb145554231304'

bot = telebot.TeleBot(API_TOKEN)

#channel_id = '@Telegend01'

#@bot.message_handler(content_types=['new_chat_members'])
#def check_user_membership(message: Message):
#    for member in message.new_chat_members:
#        if member.username == 'username_to_check':
#            # قفل ربات باز شود
#            bot.set_chat_permissions(channel_id, telebot.types.ChatPermissions())
#            bot.send_message(channel_id, f'{member.username} عضو کانال شد.')
#            break
#        else:
#            # کاربر عضو صحیح نیست، قفل ربات باقی بماند
#           bot.set_chat_permissions(channel_id, telebot.types.ChatPermissions(can_send_messages=False))
#            bot.send_message(channel_id, f'{member.username} به عنوان عضو مورد تایید نیست.')
#            break

Status = InlineKeyboardButton(text='Status', url='https://t.me/LegendBotz')
Developer = InlineKeyboardButton(text='Developer', url='https://t.me/LegendCoders')
channels = InlineKeyboardMarkup([[Status,Developer]])

# /start
@bot.message_handler(commands=['start'])
@bot.message_handler(func = lambda message: '/start' in message.text)
def start_message(message):
    username = message.from_user.username
    first_name = message.from_user.first_name
    bot.send_message(message.chat.id, f"Hello Dear {first_name} !\nI'm Calculator - Finder Bot.\n\nCalculate Simple Expressions: /calculate\n\nReceive Time of a Country or City: /time\n\nReceive Weather Information of a City:\n/weather\n\nDeveloper @LegendCoders\n\nNews @LegendBotz",reply_markup=channels)

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
        bot.reply_to(message,f"{process_expression} = {result}",reply_markup=channels)
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
        bot.reply_to(message, f"Time in {city}: {time_str}",reply_markup=channels)
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

            bot.reply_to(message, weather_info,reply_markup=channels)
        else:
            bot.send_message(message.chat.id, 'City not found! Please try again: /weather')
    except Exception as e:
        bot.send_message(message.chat.id, 'Something went wrong. Please try again later.')

# info
@bot.message_handler(commands = ['info'])
@bot.message_handler(func=lambda message: '/info' in message.text)
def info_message(message):
    bot.send_message(message.chat.id,"Tools and Services that I use\n\nProgramming Language = Python\n\nLibrary = pyTelegramBotAPI\n\nHosting Service = PythonAnywhere\n\nDeveloper information: /developer",reply_markup=channels)

t = InlineKeyboardButton(text="Telegram",url="https://telegram.me/ArtinMoghadasi")
ig = InlineKeyboardButton(text="Instagram",url="https://Instagram.com/artin.mgs")
# yt = InlineKeyboardButton(text="YouTube",url="https://youtube.com/@NullLegend01")
gh = InlineKeyboardButton(text="GitHub",url="https://github.com/ArtinMoghadasi")
landingpage =InlineKeyboardButton(text="Social Media",url="https://linktr.ee/ArtinMoghadasi")
dev = InlineKeyboardMarkup([[t],[gh],[landingpage]])

@bot.message_handler(commands = ['developer'])
@bot.message_handler(func=lambda message: '/developer' in message.text)
def developer_message(message):
    bot.send_message(message.chat.id,"I'm Developed by @LegendCoders\n\nContact @Legendify\n\nUse the Following Buttons to Reach other Projects and More!",reply_markup=dev)

helpbuttons = InlineKeyboardButton(text="Contact",url="https://t.me/Legendify")
helpBTNHandler = InlineKeyboardMarkup([[helpbuttons]])
@bot.message_handler(commands = ['help'])
@bot.message_handler(func=lambda message: '/help' in message.text)
def help_message(message):
    bot.send_message(message.chat.id,"Commands List\n\n/weather - Weather Information\n/time - Time Finder\n/calculate - Calculator\n/info - Bot Information\n/developer - Developer Information\n/help - See This Message Again!\n\nIf you have any problem or ideas feel free to tell me @Legendify",reply_markup=helpBTNHandler)

# https://api.telegram.org/bot[5802882726:AAGN2LnDv_7IYYZyvDAc40kEQRrjQVXMnW0]/getChatMembersCount

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

