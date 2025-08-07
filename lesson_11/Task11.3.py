class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведён")

    def finish(self):
        print("Автомобиль заглушен")

    def set_color(self, color):
        self.color = color

    def set_type(self, type):
        self.type = type

    def set_year(self, year):
        self.year = year

    def show_info(self):
        print(self.color)
        print(self.type)
        print(self.year)

toyota = Car("Черный", "Седан", 2001)

print("Старая тойота")
toyota.start()
toyota.show_info()
toyota.finish()

print("\nТойота")
toyota.start()
toyota.set_color("Желтый")
toyota.set_type("Хэтчбек")
toyota.set_year(2003)
toyota.show_info()
toyota.finish()