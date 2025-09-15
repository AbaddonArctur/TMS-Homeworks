import os
import re

print(f"\nОперационная система: {os.name}")
print(f"Текущая директория: {os.getcwd()}\n")

# Пути к папкам
task1_dir = "Task1"
docs_dir = os.path.join(task1_dir, "Documents")
pics_dir = os.path.join(task1_dir, "Pictures")
vids_dir = os.path.join(task1_dir, "Videos")

# Создаём папки, если не существуют
os.makedirs(docs_dir, exist_ok=True)
os.makedirs(pics_dir, exist_ok=True)
os.makedirs(vids_dir, exist_ok=True)

# Создаём файлы
open(os.path.join(task1_dir, "Sample_text.txt"), "w").close()
open(os.path.join(task1_dir, "Doc_text.docx"), "w").close()
open(os.path.join(task1_dir, "Gelendzhik2007.png"), "w").close()
open(os.path.join(task1_dir, "Pepe.jpeg"), "w").close()
open(os.path.join(task1_dir, "Amogus.mp4"), "w").close()
open(os.path.join(task1_dir, "Batman.mov"), "w").close()

print(f"Содержимое Task1 до сортировки: {os.listdir(task1_dir)}")

# Итерируемся по файлам в Task1
for file in os.listdir(task1_dir):
    file_path = os.path.join(task1_dir, file)

    # Игнорируем папки
    if os.path.isdir(file_path):
        continue

    # Перемещаем файлы по папкам в зависимости от расширения
    if re.search(r"\.(txt|docx)", file):
        os.replace(file_path, os.path.join(docs_dir, file))
    elif re.search(r"\.(png|jpeg)", file):
        os.replace(file_path, os.path.join(pics_dir, file))
    elif re.search(r"\.(mp4|mov)", file):
        os.replace(file_path, os.path.join(vids_dir, file))

print(f"\nСодержимое Task1/Documents: {os.listdir(docs_dir)}")
print(f"Содержимое Task1/Pictures: {os.listdir(pics_dir)}")
print(f"Содержимое Task1/Videos: {os.listdir(vids_dir)}")

# Переименование файла
old_name = os.path.join(pics_dir, "Pepe.jpeg")
new_name = os.path.join(pics_dir, "Sad_Pepe.jpg")
os.replace(old_name, new_name)

print(f"\nTask1/Pictures после переименования файла: {os.listdir(pics_dir)}")