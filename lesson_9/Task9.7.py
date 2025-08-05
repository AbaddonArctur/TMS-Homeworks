import os

os.makedirs("Task7", exist_ok=True)
input_file = os.path.join("Task7", "input.txt")
output_file = os.path.join("Task7", "output.txt")

# Шифруемый текст
text_to_write = """Hello, World!
Python.
Это 3-я строка, таким же будет и сдвиг.
Шифр Цезаря может быть здесь."""

with open(input_file, "w", encoding='utf-8') as inp_file:
    inp_file.write(text_to_write)

with open(input_file, "r", encoding='utf-8') as inp_file:
    print(f"\nИсходный текст:\n{inp_file.read()}")

# Выбор алфавита
while True:
    alphabet_choice = input("\nВыберите алфавит (рус / eng): ").strip().lower()

    if alphabet_choice == "рус":
        low_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        upp_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        break
    elif alphabet_choice == "eng":
        low_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        upp_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        break
    else:
        print("Ошибка: нужно ввести 'рус' или 'eng'")

alphas = len(low_alphabet)

# Функция шифрования строки с заданным шагом
def caesar_encrypt(text, steps):
    result = ""
    for char in text:
        if char in low_alphabet:
            index = low_alphabet.index(char)
            result += low_alphabet[(index + steps) % alphas]
        elif char in upp_alphabet:
            index = upp_alphabet.index(char)
            result += upp_alphabet[(index + steps) % alphas]
        else:
            result += char  # Не в алфавите - не меняем
    return result

# Построчная обработка файла
with open(input_file, "r", encoding='utf-8') as inp_file, \
     open(output_file, "w", encoding='utf-8') as out_file:
    for line_num, line in enumerate(inp_file, start=1):
        step = line_num  # Шаг = номер строки
        encrypted_line = caesar_encrypt(line.strip(), step)
        out_file.write(f"{encrypted_line}\n")

# Вывод результата
print("\nЗашифрованный текст:")
with open(output_file, "r", encoding='utf-8') as result_file:
    print(result_file.read())