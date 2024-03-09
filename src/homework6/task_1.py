
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels


class Salon(Vehicle):
    def __init__(self, location, cars=None):
        super().__init__(wheels=4)
        self.location = location
        self._cars = cars if cars else []

    @property
    def inventory(self):
        return len(self._cars)

    @staticmethod
    def is_open(hour):
        return 9 <= hour <= 20

    def add_car(self, car):
        self._cars.append(car)

    def __str__(self):
        cars = "\n".join(str(car) for car in self._cars)
        return f"Салон в {self.location} с {self.inventory} автомобилями в наличии:\n{cars}"


toyota_camry = Car("Toyota", "Camry", 2022)
ford_f150 = Car("Ford", "F-150", 2023)
bmw_x5 = Car("BMW", "X5", 2023)
tesla_model_s = Car("Tesla", "Model S", 2024)
audi_q7 = Car("Audi", "Q7", 2023)
salon = Salon("Минске", [toyota_camry, ford_f150, bmw_x5, tesla_model_s, audi_q7])
print(salon)
