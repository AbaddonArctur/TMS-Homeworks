import os

os.makedirs("Task5", exist_ok=True)

input_file = os.path.join("Task5", "input.txt")

input_to_write = """Арктур - 5
Цефей - 3
Сириус - 2
Канопус - 1
Ригель - 4
Вега - 5
Капелла - 2
Ригил - 1
Хадар - 3
Бетельгейзе - 2
Альтаир - 4
"""

with open(input_file, "w", encoding='utf-8') as inp_file:
    inp_file.write(input_to_write)

with open(input_file, "r", encoding='utf-8') as inp_file:
    print(f"\nИсходные данные:\n{inp_file.read()}")

print("Меньше 3 баллов:")
with open(input_file, "r", encoding='utf-8') as inp_file:
    # Итерируемся по строкам в input.txt
    for line in inp_file:
        # Удаляем пробелы и перенос строки по краям
        line = line.strip()
        if not line:
            continue  # Пропускаем пустые строки

        # Разбиваем строку по " - " на имя и оценку
        name, score_str = line.split(" - ")
        score = int(score_str)

        if score < 3:
            print(name)