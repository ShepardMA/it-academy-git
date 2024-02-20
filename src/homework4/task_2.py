# The Cities

def find_country():
    motherland = {city: country for _ in range(int(input("Введите количество стран: "))) for country,
                  *cities in [input("Введите название страны и города через пробел: ").split()] for city in cities}
    for _ in range(int(input("Введите количество запросов: "))):
        city_name = input("Введите название города: ")
        print(motherland.get(city_name, "Город не найден"))


find_country()
