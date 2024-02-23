# The Cities

def find_country():
    motherland = {
        "moscow": "russia",
        "petersburg": "russia",
        "novgorod": "russia",
        "kaluga": "russia",
        "kiev": "ukraine",
        "donetsk": "ukraine",
        "odessa": "ukraine"}
    queries = ["moscow", "kiev", "odessa", "paris"]
    for city_name in queries:
        country = motherland.get(city_name, "Город не найден")
        print(f"Город {city_name.capitalize()} находится в стране {country.capitalize()}.")


find_country()
