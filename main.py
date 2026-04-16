import telebot




# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("8465530054:AAFw8TyAaSsbawKsce6xMA1hxGOcdtioNX8")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /article, /mem или /facts  ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Ну что начнем изучать глобальное потепление или посмеемся?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Всё, давай! Заходи в свободное время!")