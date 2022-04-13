from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('f6a7f66c1b1ba4d2e7f263ad9b47c056')
mgr = owm.weather_manager()

place = input("где?:")

observation = mgr.weather_at_place('place')
w = observation.weather

temp = w.temperature('celsius')["temp"]

print("В городе " + place + " сегодня " + w.detailed_status)
print("Температура воздуха примерно " + str(temp) + " градусов цельсия")

if temp < 10:
    print("Нахерь не вылазь даже")
elif temp < 15:
    print("Ну, я б подумал на твоём месте")
elif temp < 20:
    print("Оденься только нормально")
else:
    print("Седня ништяк")
