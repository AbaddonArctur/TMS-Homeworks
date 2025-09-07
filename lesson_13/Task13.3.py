# Класс с атрибутами
class Pizza:
    def __init__(self, size=None, cheese=False, pepperoni=False, mushrooms=False, onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        ingredients = []

        if self.cheese:
            ingredients.append("сыр")
        if self.pepperoni:
            ingredients.append("пепперони")
        if self.mushrooms:
            ingredients.append("грибы")
        if self.onions:
            ingredients.append("лук")
        if self.bacon:
            ingredients.append("бекон")

        return f"Пицца:\nРазмер - {self.size}\nНачинка - {', '.join(ingredients) if ingredients else 'нет'}\n"


# Класс с методами наполнения пицц
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        self.pizza.onions = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        return self.pizza


# Класс с методами создания конкретных пицц
class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self, size):
        return self.builder.set_size(size).build()

    def make_cheese_pizza(self, size):
        return self.builder.set_size(size).add_cheese().build()

    def make_pepperoni_pizza(self, size):
        return self.builder.set_size(size).add_cheese().add_pepperoni().build()

    def make_supreme_pizza(self, size):
        return (self.builder.set_size(size).add_cheese().add_pepperoni().add_mushrooms().add_onions().add_bacon()
                .build())


if __name__ == "__main__":
    p_builder = PizzaBuilder()
    director = PizzaDirector(p_builder)

    # Создание простой пиццы только с размером
    pizza1 = director.make_pizza("маленькая")
    print(pizza1)

    # Создание сырной пиццы
    pizza2 = director.make_cheese_pizza("средняя")
    print(pizza2)

    # Создание пиццы пепперони
    pizza3 = director.make_pepperoni_pizza("большая")
    print(pizza3)

    # Создание пиццы со всеми добавками
    pizza4 = director.make_supreme_pizza("большая")
    print(pizza4)

    # Создание своей пиццы без PizzaDirector
    custom_pizza = PizzaBuilder().set_size("средняя").add_cheese().add_mushrooms().add_bacon().build()
    print(custom_pizza)