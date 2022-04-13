import telebot

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('f6a7f66c1b1ba4d2e7f263ad9b47c056')
mgr = owm.weather_manager()
bot = telebot.TeleBot("5342538361:AAF1apvA7izhxi_Zpo7T_7k21zj7JCoMIec")

	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    observation = mgr.weather_at_place( message.text )
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сегодня " + w.detailed_status +"\n"
    answer += "Температура воздуха примерно " + str(temp) + " градусов цельсия" +"\n\n"

    if temp < 10:
        answer +=("Нахерь не вылазь даже")
    elif temp < 15:
        answer +=("Ну, я б подумал на твоём месте")
    elif temp < 20:
        answer +=("Оденься только нормально")
    else:
        answer +=("Седня ништяк")
        
    bot.send_message(message.chat.id, answer)
bot.infinity_polling()
