from abc import ABC, abstractmethod

# Базовый интерфейс стратегии
class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


# Конкретные стратегии
class Addition(Strategy):
    def execute(self, a, b):
        return a + b


class Subtraction(Strategy):
    def execute(self, a, b):
        return a - b


class Multiplication(Strategy):
    def execute(self, a, b):
        return a * b


class Division(Strategy):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b


# Класс, использующий стратегии
class Calculator:
    def __init__(self, strategy = None):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def calculate(self, a, b):
        if not self._strategy:
            raise ValueError("Стратегия не установлена")
        return self._strategy.execute(a, b)


if __name__ == "__main__":
    calc = Calculator()

    while True:
        title = "КАЛЬКУЛЯТОР"
        print(title.center(35, "-"))

        inp = input("1) сложение\n2) вычитание\n3) умножение\n4) деление\n5) выйти\n")

        try:
            if inp.replace(" ", "") == "1" or inp.replace(" ", "") == "1)":
                calc.set_strategy(Addition())

                x = float(input("\nПервое слагаемое: "))
                y = float(input("Второе слагаемое: "))

                print(f"Сумма: {calc.calculate(x, y)}\n")

            elif inp.replace(" ", "") == "2" or inp.replace(" ", "") == "2)":
                calc.set_strategy(Subtraction())

                c = float(input("\nУменьшаемое: "))
                d = float(input("Вычитаемое: "))

                print(f"Разность: {calc.calculate(c, d)}\n")

            elif inp.replace(" ", "") == "3" or inp.replace(" ", "") == "3)":
                calc.set_strategy(Multiplication())

                e = float(input("\nПервый множитель: "))
                f = float(input("Второй множитель: "))

                print(f"Произведение: {calc.calculate(e, f)}\n")

            elif inp.replace(" ", "") == "4" or inp.replace(" ", "") == "4)":
                calc.set_strategy(Division())

                g = float(input("\nДелимое: "))
                h = float(input("Делитель: "))

                print(f"Частное: {calc.calculate(g, h)}\n")

            elif inp.replace(" ", "") == "5" or inp.replace(" ", "") == "5)":
                break

            else:
                print("\nНекорректный ввод, попробуйте 1, 2, 3, 4 или 5\n")

        except ValueError:
            print(
                "\nНекорректный ввод, введите числовое значение.\nДля для записи дробных чисел используйте '.'\nНапример: 123.45\n")
        except ZeroDivisionError:
            print("\nНельзя делить на ноль\n")
        except OverflowError:
            print("\nРезультат операции слишком велик для представления.\nПопробуйте с меньшими значениями\n")