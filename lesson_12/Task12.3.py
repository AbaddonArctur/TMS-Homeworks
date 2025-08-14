from dataclasses import dataclass, field

@dataclass
class Bus:
    max_seats: int # Максимальное ко-во посадочных мест в автобусе
    max_speed: int # Максимально допустимая скорость автобуса
    speed: int = 0 # Текущая скорость автобуса (по умолчанию 0)
    passengers: list = field(default_factory=list)  # Список фамилий пассажиров
                                                    # (default_factory=list создаёт новый список для каждого объекта)
    has_free_seats: bool = True # Флаг наличия свободных мест
    seat_map: dict = field(init=False)  # Словарь мест в автобусе, в __init__ не передаём, заполняем позже

    def __post_init__(self):
        """
        Этот метод вызывается автоматически после того,
        как dataclass закончил стандартную инициализацию.
        Создаём словарь мест вида {1: None, 2: None, ...}
        """
        self.seat_map = {i + 1: None for i in range(self.max_seats)}
        self._update_free_seats_flag() # Обновляем флаг свободных мест

    def _update_free_seats_flag(self):
        """
        Проверяем, есть ли хотя бы одно свободное место (None) в seat_map,
        и обновляем флаг has_free_seats.
        """
        self.has_free_seats = any(p is None for p in self.seat_map.values())

    def board(self, *names):
        """
        Посадка одного или нескольких пассажиров.
        Ищем первое свободное место для каждого пассажира.
        Если мест нет — выводим сообщение.
        """
        for name in names:
            if None in self.seat_map.values():
                for seat, passenger in self.seat_map.items():
                    if passenger is None:
                        self.seat_map[seat] = name
                        self.passengers.append(name)
                        break
            else:
                print(f"Нет свободных мест для {name}!")
        self._update_free_seats_flag()

    def disembark(self, *names):
        """
        Высадка одного или нескольких пассажиров по фамилии.
        Удаляем их из списка пассажиров и освобождаем место.
        Если пассажир не найден — выводим сообщение.
        """
        for name in names:
            if name in self.passengers:
                self.passengers.remove(name)
                for seat, passenger in self.seat_map.items():
                    if passenger == name:
                        self.seat_map[seat] = None
                        break
            else:
                print(f"Пассажир {name} не найден!")
        self._update_free_seats_flag()

    def change_speed(self, delta: int):
        """
        Изменение скорости на delta км/ч (может быть отрицательным).
        Скорость ограничена от 0 до max_speed.
        """
        self.speed += delta
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.max_speed:
            self.speed = self.max_speed

    # Перегрузки операторов
    def __contains__(self, name: str) -> bool:
        """
        Перегрузка оператора `in`.
        Позволяет проверять наличие пассажира в автобусе.
        """
        return name in self.passengers

    def __add__(self, name: str):
        """
        Перегрузка оператора +=
        Позволяет сажать пассажира.
        """
        self.board(name)
        return self

    def __sub__(self, name: str):
        """
        Перегрузка оператора -=
        Позволяет высаживать пассажира.
        """
        self.disembark(name)
        return self

    def __str__(self):
        """
        Текстовое представление объекта.
        Вызывается при print(bus).
        """
        return (f"Скорость: {self.speed} км/ч\n"
                f"Пассажиры ({len(self.passengers)}/{self.max_seats}): {', '.join(self.passengers) or '—'}\n"
                f"Свободные места: {'Да' if self.has_free_seats else 'Нет'}\n"
                f"Схема мест: {self.seat_map}")


if __name__ == "__main__":
    bus = Bus(max_seats=5, max_speed=120)

    # Посадка через оператор +=
    bus += "Иванов"
    bus += "Петров"

    # Посадка нескольких пассажиров
    bus.board("Сидоров", "Кузнецов")

    print(bus)

    # Увеличение скорости на 60
    bus.change_speed(60)

    # Высадка через оператор -=
    bus -= "Петров"

    print("\nПосле изменений:")
    print(bus)

    print("")
    # Проверка наличия пассажира
    print("Иванов" in bus)