from abc import ABC, abstractmethod


# Базовый интерфейс животного
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# Конкретные животное
class Dog(Animal):
    def speak(self):
        return "Гав-гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу-мяу!"


# Базовый интерфейс фабрики
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

    def make_and_speak(self):
        # Вызов фабричного метода для получения объекта-животного
        animal = self.create_animal()
        return f"Животное говорит: {animal.speak()}"


# Конкретные фабрики
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()


if __name__ == "__main__":
    dog_factory = DogFactory()
    print(dog_factory.make_and_speak())

    cat_factory = CatFactory()
    print(cat_factory.make_and_speak())