class Product:
    def __init__(self, name, store, price):
        self.__name = name # Название товара
        self.__store = store # Название магазина
        self.__price = price # Стоимость товара

    def get_name(self):
        return self.__name

    def get_store(self):
        return self.__store

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"{self.__name} ({self.__store}) — {self.__price} руб."

    # Перегрузка сложения по цене
    def __add__(self, other):
        if isinstance(other, Product):
            return self.__price + other.__price
        raise TypeError("Можно складывать только объекты Product")


class Warehouse:
    def __init__(self):
        self.__products = [] # Закрытый массив товаров

    # Добавление продукта в массив
    def add_product(self, product):
        self.__products.append(product)

    # Поиск по индексу
    def __getitem__(self, index):
        try:
            return self.__products[index]
        except IndexError:
            return None

    # Поиск по имени товара
    def get_by_name(self, name):
        for product in self.__products:
            if product.get_name().lower() == name.lower():
                return product
        return None

    # Сортировка
    def sort_by_name(self):
        self.__products.sort(key=lambda p: p.get_name())

    def sort_by_store(self):
        self.__products.sort(key=lambda p: p.get_store())

    def sort_by_price(self):
        self.__products.sort(key=lambda p: p.get_price())

    # Вывод всех продуктов
    def show_all(self):
        for product in self.__products:
            print(product)

w = Warehouse()

w.add_product(Product("Хлеб", "Евроопт", 2.50))
w.add_product(Product("Молоко 1л", "Корона", 3))
w.add_product(Product("Яблоки 1кг", "Доброном", 8))

print("\nВсе товары:")
w.show_all()

print("\nТовар по индексу 1:")
print(w[1])  # Должен вывести "Молоко 1л..."

print("\nТовар c наименованием 'Хлеб':")
print(w.get_by_name("Хлеб"))  # Должен вывести "Хлеб..."

print("\nСортировка по цене:")
w.sort_by_price()
w.show_all()

p1 = w.get_by_name("Хлеб")
p2 = w.get_by_name("Яблоки 1кг")
print(f"\nСумма цен:\n{p1}\n+\n{p2}\n=\n{p1 + p2}руб.")