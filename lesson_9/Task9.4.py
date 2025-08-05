import os
import re

os.makedirs("Task4", exist_ok=True)

stop_words_file = os.path.join("Task4", "stop_words.txt")
input_file = os.path.join("Task4", "input.txt")
output_file = os.path.join("Task4", "output.txt")

# Текст для файла сос топ-словами
stop_to_write = "друж хорош бним улки теб лю"
# Текст для файла, в котором будем искать стоп-слова
input_to_write = "Эй, дРУжок, хоРошо выглядишь! Я тебя обНИму! Я не люблю БУЛКИ! Но люблю тебя"

# Записываем стоп-слова в файл
with open(stop_words_file, "w", encoding='utf-8') as stop_file:
    stop_file.write(stop_to_write)

# Записываем текст, по которому будем проводить поиск стоп-слов
with open(input_file, "w", encoding='utf-8') as in_file:
    in_file.write(input_to_write)

# Разбиваем стоп-слова по пробелам и приводим к нижнему регистру
with open(stop_words_file, "r", encoding='utf-8') as stop_file:
    stop_words = stop_file.read().split()
    print(f"Список стоп-слов:\n{stop_words}") # Вывод в консоль стоп-слов
    stop_words = [word.lower() for word in stop_words]

# Чтение текста в котором ищем стоп-слова записываем в переменную
with open(input_file, "r", encoding='utf-8') as in_file:
    inp_text = in_file.read()
print(f"\nИсходный текст:\n{inp_text}") # Вывод в консоль текста в котором ищем стоп-слова

# Функция замены стоп-слов на '*'
def mask_stop_parts(text, s_words):
    # Вложенная функция, вызывается для каждого слова
    def replacer(match):
        word = match.group()      # Слово из текста, в котором ищем стоп-слова
        word_lower = word.lower() # Приводим к нижнему регистру
        masked = list(word)       # Посимвольный список оригинального слова

        # Итерируемся по каждому стоп-слову
        for stop in s_words:
            # Ищем все вхождения стоп-слова в текущем слове
            for m in re.finditer(re.escape(stop), word_lower):
                start, end = m.span() # Позиция вхождения
                # Заменяем символы, соответствующие стоп-слову, на '*'
                for i in range(start, end):
                    masked[i] = '*'

        return ''.join(masked) # Собираем результат в строку и возвращаем

    return re.sub(r'\w+', replacer, text, flags=re.UNICODE)

# Записываем результат в файл
with open(output_file, "w", encoding='utf-8') as out_file:
    out_file.write(mask_stop_parts(inp_text, stop_words))

# Вывод в консоль результата
with open(output_file, "r", encoding='utf-8') as out_file:
    print(f"\nРезультат:\n{out_file.read()}")