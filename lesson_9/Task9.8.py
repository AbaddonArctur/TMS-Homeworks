import os
import json
import csv
from datetime import datetime

os.makedirs("Task8", exist_ok=True)

employees_file_json = os.path.join("Task8", "employees.json")
employees_file_csv = os.path.join("Task8", "employees.csv")

input_to_write = """[
    {
        "name": "John Smith",
        "birthday": "02.10.1990",
        "height": 175,
        "weight": 76.5,
        "car": true,
        "languages": ["C++", "Python"]
    },
    {
        "name": "Alexey Alexeev",
        "birthday": "05.06.1986",
        "height": 197,
        "weight": 101.2,
        "car": false,
        "languages": ["Pascal", "Delphi"]
    },
    {
        "name": "Maria Ivanova",
        "birthday": "28.08.1998",
        "height": 165,
        "weight": 56.1,
        "car": true,
        "languages": ["C#", "C++", "C"]
    }
]"""

# Записываем данные в employees.json (если не существует)
if not os.path.exists(employees_file_json):
    with open(employees_file_json, "w", encoding='utf-8') as j_file:
        j_file.write(input_to_write)

# Функция чтения employees.json
def read_json(json_file):
    with open(json_file, "r", encoding='utf-8') as j:
        return json.load(j)

# Функция записи в employees.json
def write_json(json_file, data):
    with open(json_file, "w", encoding='utf-8') as j:
        json.dump(data, j, indent=4, ensure_ascii=False)

# Конвертация данных json в csv
def convert_to_csv(json_data):
    while True:
        warn = input("\nЭто действие перезапишет файл employees.csv (если он существует)."
                     " Вы уверены? (да/нет): ").lower().strip()
        if warn == "да":
            with open(employees_file_csv, 'w', newline='', encoding='utf-8') as csv_file:
                fieldnames = list(json_data[0].keys()) # Сохраняем порядок ключ-значение из первого словаря
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames) # Создаем словарь csv
                writer.writeheader() # Заполняем заголовки
                for row in json_data: # Заполняем строки
                    writer.writerow(row)
                print("\nДанные записаны в employees.csv")
                break
        elif warn == "нет":
            break
        else:
            pass
# Добавление нового сотрудника в json
def add_employee_json(json_file):
    print("Введите данные нового сотрудника:\n")

    # Ввод Имени
    while True:
        name = input("Имя: ").strip()
        if name:
            break
        print("Имя не может быть пустым.")

    # Ввод даты рождения
    while True:
        birthday = input("Дата рождения (дд.мм.гггг): ").strip()
        try:
            datetime.strptime(birthday, "%d.%m.%Y")
            break
        except ValueError:
            print("Неверный формат даты. Пример: 28.08.1998")

    # Ввод роста
    while True:
        try:
            height = int(input("Рост (в см): ").strip())
            if height > 0:
                break
            else:
                print("Рост должен быть положительным числом.")
        except ValueError:
            print("Введите целое число.")

    # Ввод веса
    while True:
        try:
            weight = float(input("Вес (в кг): ").strip())
            if weight > 0:
                break
            else:
                print("Вес должен быть положительным числом.")
        except ValueError:
            print("Введите число с точкой (например: 75.5), либо целое число")

    # Ввод информации о наличии машины
    while True:
        car_input = input("Есть машина? (да/нет): ").strip().lower()
        if car_input in ['да', 'нет']:
            car = car_input == 'да'
            break
        else:
            print("Введите 'да' или 'нет'.")

    # Ввод языков программирования
    langs_input = input("Знает языки программирования (через запятую): ").strip()
    languages = [lang.strip() for lang in langs_input.split(',') if lang.strip()]

    new_employee = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": languages
    }

    data = read_json(json_file)
    data.append(new_employee)
    write_json(json_file, data)

    print("\nНовый сотрудник добавлен в JSON.")

# Добавляем нового сотрудника в csv
def add_employee_csv(csv_file):
    print("Введите данные нового сотрудника:\n")

    # Ввод имени
    while True:
        name = input("Имя: ").strip()
        if name:
            break
        print("Имя не может быть пустым.")

    # Ввод даты рождения
    while True:
        birthday = input("Дата рождения (дд.мм.гггг): ").strip()
        try:
            datetime.strptime(birthday, "%d.%m.%Y")
            break
        except ValueError:
            print("Неверный формат даты. Пример: 28.08.1998")

    # Ввод роста
    while True:
        try:
            height = int(input("Рост (в см): ").strip())
            if height > 0:
                break
            else:
                print("Рост должен быть положительным числом.")
        except ValueError:
            print("Введите целое число.")

    # Ввод веса
    while True:
        try:
            weight = float(input("Вес (в кг): ").strip())
            if weight > 0:
                break
            else:
                print("Вес должен быть положительным числом.")
        except ValueError:
            print("Введите число с точкой (например: 75.5)")

    # Ввод информации о наличии машины
    while True:
        car_input = input("Есть машина? (да/нет): ").strip().lower()
        if car_input in ['да', 'нет']:
            car = car_input == 'да'
            break
        else:
            print("Введите 'да' или 'нет'.")

    # Ввод языков программирования
    langs_input = input("Знает языки программирования (через запятую): ").strip()
    languages = [lang.strip() for lang in langs_input.split(',') if lang.strip()]
    languages_str = ', '.join(languages)

    # Словарь нового сотрудника
    new_employee = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": languages_str
    }

    # Определяем, нужно ли записывать заголовок
    file_exists = os.path.exists(csv_file)
    write_header = not file_exists or os.stat(csv_file).st_size == 0

    with open(csv_file, 'a', newline='', encoding='utf-8') as f:
        fieldnames = ["name", "birthday", "height", "weight", "car", "languages"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if write_header:
            writer.writeheader()

        writer.writerow(new_employee)

    print("\nНовый сотрудник добавлен в CSV.")

# Ищем сотрудника по имени
def find_employee_by_name(json_file):
    name_to_find = input("Введите полное имя сотрудника для поиска: ").strip().lower()

    found = False
    for emp in read_json(json_file):
        # Сравниваем без учёта регистра
        if emp["name"].lower() == name_to_find:
            print("\nИнформация о сотруднике:")
            for key, value in emp.items():
                print(f"{key.capitalize()}: {value}")
            found = True
            break

    if not found:
        print("Сотрудник не найден.")

# Ищем сотрудников, владеющих определённым языком
def filter_by_language(json_file):
    language_to_find = input("Введите язык программирования для поиска: ").strip().lower()

    print(f"\nСотрудники, владеющие языком '{language_to_find}':\n")

    found = False
    for emp in read_json(json_file):
        # Проверяем, есть ли ключ languages и является ли он списком
        if "languages" in emp and isinstance(emp["languages"], list):
            langs_lower = [lang.lower() for lang in emp["languages"]]
            if language_to_find in langs_lower:
                print(f"- {emp['name']}")
                found = True

    if not found:
        print("Никто из сотрудников не владеет этим языком.")

# Находим средний рост всех сотрудников, у которых год рождения меньше заданного
def average_height_before_year(json_file):
    data = read_json(json_file)
    while True:
        year_input = input("\nВведите граничный год рождения (например, 1990): ").strip()

        if year_input.isdigit() and len(year_input) == 4:
            year_input = int(year_input)
            heights = []

            for emp in data:
                birthday_str = emp.get("birthday", "")
                try:
                    # Преобразуем строку 'дд.мм.гггг' в объект datetime
                    birth_date = datetime.strptime(birthday_str, "%d.%m.%Y")
                    birth_year = birth_date.year
                except ValueError:
                    continue  # Пропускаем некорректные даты

                if birth_year < year_input:
                    height = emp.get("height")
                    if isinstance(height, (int, float)):
                        heights.append(height)

            if heights:
                avg_height = round(sum(heights) / len(heights), 2)
                print(f"\nСредний рост сотрудников, родившихся до {year_input}: {avg_height} см")
                break
            else:
                print("\nНет сотрудников, подходящих под условие.")
                break
        else:
            print("\nНеверный формат года. Введите 4 цифры, например: 1990")

while True:
    print("")
    head = "СОТРУДНИКИ"
    print(head.center(42, "-"))
    print("1) Прочитать JSON файл\n2) Записать в CSV файл\n3) Добавить нового сотрудника в JSON файл\n"
          "4) Добавить нового сотрудника в CSV файл\n5) Поиск сотрудника по имени\n6) Поиск сотрудника по языкам\n"
          "7) Средний рост сотрудников до n года\n8) Выход\n")
    user_input = input("Введите номер запроса (например '1' или '1)'): ").strip()
    if user_input == "1" or user_input == "1)":
        print(f"\nДанные employees.json:\n{read_json(employees_file_json)}")
    elif user_input == "2" or user_input == "2)":
        convert_to_csv(read_json(employees_file_json))
    elif user_input == "3" or user_input == "3)":
        add_employee_json(employees_file_json)
    elif user_input == "4" or user_input == "4)":
        add_employee_csv(employees_file_csv)
    elif user_input == "5" or user_input == "5)":
        find_employee_by_name(employees_file_json)
    elif user_input == "6" or user_input == "6)":
        filter_by_language(employees_file_json)
    elif user_input == "7" or user_input == "7)":
        average_height_before_year(employees_file_json)
    elif user_input == "8" or user_input == "8)":
        end = "КОНЕЦ"
        print(end.center(42, "-"))
        exit()
    else:
        print("\nНекорректный ввод, попробуйте ещё раз")