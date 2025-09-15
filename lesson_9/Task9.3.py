import os
import re

os.makedirs("Task3", exist_ok=True)

input_file = os.path.join("Task3", "input.txt")
output_file = os.path.join("Task3", "output.txt")

# Текст для файла по которому будем проводить поиск
data_to_write = """10101010010.
Мама мыла раму, рама мыла маму.
Тестовое предложение. А что за предложение? Я согласен на предложение.
Кошка прыгнула в окно. Кошка В С Ё.
За пределами света. Вне досягаемости тьмы."""

# Создаем и заполняем файл с текстом
with open(input_file, "w", encoding='utf-8') as in_file:
    in_file.write(data_to_write)

with open(input_file, "r", encoding="utf-8") as in_file:
    print(f"\nИсходный текст:\n{in_file.read()}")

# Открываем файлы input.txt и output.txt на чтение и запись соответственно
with open(input_file, "r", encoding="utf-8") as in_file, \
     open(output_file, "w", encoding="utf-8") as out_file:

    # Итерируемся по строкам файла input.txt
    for line in in_file:
        # Приводим к нижнему регистру и извлекаем слова
        words = re.findall(r"\b[а-яёА-ЯЁa-zA-Z]+\b", line.lower())

        # Если нет буквенных символов, то нет слов
        if not words:
            out_file.write("Нет слов\n")
            continue

        # Считаем количество повторений каждого слова
        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        # Находим слово с максимальной частотой
        most_common_word = max(word_counts, key=word_counts.get)
        count = word_counts[most_common_word]

        # Записываем результат в output.txt
        out_file.write(f"Слово '{most_common_word}' повторилось {count} раз(а)\n")

with open(output_file, "r", encoding="utf-8") as out_file:
    print(f"\nРезультат:\n{out_file.read()}")