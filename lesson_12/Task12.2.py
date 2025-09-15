class BeeElephant:
    def __init__(self, bee_part, elephant_part):
        self.bee = bee_part # Часть пчелы
        self.elephant = elephant_part # Часть слона

    def fly(self):
        return self.bee >= self.elephant

    def trumpet(self):
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        """
        Если "nectar", то слон теряет value, пчела получает value.
        Если "grass", то пчела теряет value, слон получает value.
        Иначе - ошибка.
        При этом части не могут быть < 0 или > 100.
        """
        if meal == "nectar":
            self.bee = min(100, self.bee + value)
            self.elephant = max(0, self.elephant - value)
        elif meal == "grass":
            self.elephant = min(100, self.elephant + value)
            self.bee = max(0, self.bee - value)
        else:
            raise ValueError("Необходимо ввести 'nectar' или 'grass'")

p = BeeElephant(40,60)
print(p.bee, p.elephant)
print(p.fly())
print(p.trumpet())

p.eat("nectar", 30)
print(f"\n{p.bee} {p.elephant}")
print(p.fly())
print(p.trumpet())

p.eat("grass", 20)
print(f"\n{p.bee} {p.elephant}")
print(p.fly())
print(p.trumpet())