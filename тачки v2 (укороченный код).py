# Нужно запустить прогу, ввести марку машины, модель этой марки, и страну производителя, где она произведена, если верно, то программа закончится, если нет,
# то она начинается с начала, пока решение не будет верным

Audi = ["Audi", "audi", "ауди", "Ауди", "AUDI", "АУДИ"]
Mercedes_Benz = ["Mercedes-Benz", "mercedes", "mers", "merc", "benz", "мерс", "Mercedes", "мерседес", "мерин", "Мерседес-бенц"]
BMW = ["BMW", "bmw", "bnw", "Bmw", "бмв", "бэха", "бумер", "БМВ", "Бэха", "Бумер"]
Volkswagen = ["Volkswagen", "Wolksvagen", "VW", "vw", "wv", "WV", "Vw", "Wv", "Фольцваген", "Вольксваген", "Фольксваген", "Фольц", 'фольц', "ФОЛЬЦ"]
Skoda = ["Skoda", "skoda", "SKODA", "шкода", "Шкода", "ШКОДА"]
Honda = ["Honda", "honda", "HONDA", "хонда", "Хонда", "ХОНДА"]
Mitsubishi = ["Mitsubishi", "mitsubishi", "mitsu", "Mitsu", "MITSUBISHI", "MITSU", "Митсубиси", "Митсубиши", "митсубиси", "МИТСУБИСИ", "мицубиси", "МИЦУБИСИ", "мицуба", "МИЦУБА"]
Toyota = ["Toyota", "TOYOTA", "toyota", "ТОЙОТА", "Тойота", "тойота", "тоёта", "Тоёта", "ТОЁТА"]
Mazda = ["Mazda", "MAZDA", "mazda", "мазда", "Мазда", "МАЗДА"]
Ford = ["Ford", "FORD", "ford", "форд", "ФОРД", "Форд"]
Chevrolet = ["Chevrolet", "chevrolet", "CHEVROLET", "CHEVY", "Chevy", "chevy", "шевроле", "Шевроле", "ШЕВРОЛЕ", "шевролет", "Шевролет", "ШЕВРОЛЕТ"]
Dodge = ["Dodge", 'dodge', 'DODGE', "Додж", 'додж', 'ДОДЖ']

# марки тачек

modelaudi = ["A4", "A6", "A8", "TT", "RS4", "RS6", "R8", "S8"]
modelmerc = ["S", "C", "E", "ML", "G", "A", "B"]
modelbmw = [1, 3, 4, 5, 6, 8, "X5", "X6", "X7"]
modelvw = ["Golf", "Tiguan", "Touareg", "Passat", "Jetta", "Scirocco"]
modelskoda = ["Rapid", "Yeti", "Fabia", "Octavia", "Roomster"]
modelhonda = ["Civic", "HRV", "CRV", "S2000", "Accord"]
modelmitsu = ["Galant", "Eclipse", "L200", "Pajero", "Lancer"]
modeltoyota = ["Prius", "Corolla", "Land Cruiser", "Avensis", "Mark 2"]
modelmazda = [3, 6, "CX7", "CX9", "RX7", "RX8"]
modelford = ["Mustang", "F150", "Crown Victoria", "GT40", "Focus"]
modelchevy = ["Camaro", "Suburban", "Impala", "Tahoe", "Cruze"]
modeldodge = ["Viper", "RAM", "Caliber", "Neon",]
models = [modelaudi, modelmerc, modelbmw, modelvw, modelskoda, modelhonda, modelmitsu, modeltoyota, modelmazda, modelford, modelchevy, modeldodge]

# модели тачек

countryger = ["Germany", "Германия", "GERMANY", "germany", "ГЕРМАНИЯ", "германия", "germany"]
countryjap = ["Japan", "japan", "JAPAN", "япония", "Япония", "ЯПОНИЯ"]
countryusa = ["USA", "usa", "Usa", "америка", "Америка", "АМЕРИКА", "США", "сша", "Сша"]
countrysw = ["Sweden", "sweden", "SWEDEN", "Швеция", "ШВЕЦИЯ", "швеция"]

# страны изготовители тачек

running = True
while running:
    marc = input("Назовите марку автомобиля: ")
    model = input("Назовите модель этой марки: ")
    country = input("В какой стране производится эта машина?: ")
    if marc in Audi and model in modelaudi and country in countryger:
        print("--Молодец")
        running = False

    elif marc in Mercedes_Benz and model in modelmerc and country in countryger:
        print("--Молодец")
        running = False

    elif marc in BMW and model in modelbmw and country in countryger:
        print("--Молодец")
        running = False

    elif marc in Volkswagen and model in modelvw and country in countryger:
        print("--Молодец")
        running = False

    elif marc in Skoda and model in modelskoda and country in countrysw:
        print("--Молодец")
        running = False

    elif marc in Honda and model in modelhonda and country in countryjap:
        print("--Молодец")
        running = False

    elif marc in Mitsubishi and model in modelmitsu and country in countryjap:
        print("--Молодец")
        running = False

    elif marc in Toyota and model in modeltoyota and country in countryjap:
        print("--Молодец")
        running = False

    elif marc in Mazda and model in modelmazda and country in countryjap:
        print("--Молодец")
        running = False

    elif marc in Ford and model in modelford and country in countryusa:
        print("--Молодец")
        running = False

    elif marc in Chevrolet and model in modelchevy and country in countryusa:
        print("--Молодец")
        running = False

    elif marc in Dodge and model in modeldodge and country in countryusa:
        print("--Молодец")
        running = False
    else:
        print("--Чёто не правильно, пробуй заново")

print("Конец")
