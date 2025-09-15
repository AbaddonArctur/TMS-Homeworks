import os
import re

os.makedirs("Task6", exist_ok=True)

input_file = os.path.join("Task6", "input.txt")

input_to_write = "123 ааа456 1x2y3z 4 5 6" # Сумма 600

with open(input_file, "w", encoding='utf-8') as inp_file:
    inp_file.write(input_to_write)

with open(input_file, "r", encoding='utf-8') as inp_file:
    content = inp_file.read()
    print(f"Исходный текст: {content}")
    # Ищем все группы цифр \d+
    numbers = re.findall(r'\d+', content)

    # Преобразуем строки в числа и считаем сумму
    total = [int(num) for num in numbers]
    total_sum = sum(total)

    print("Сумма всех чисел в файле:", total_sum)