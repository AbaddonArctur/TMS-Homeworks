import re
import os
from datetime import datetime


class User:
    """
    Класс для представления пользователя.
    Хранит имя и email.
    """

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        """
        Возвращает строковое представление пользователя.
        """
        return f"{self.username}: {self.email}"

    @staticmethod
    def from_string(line):
        """
        Создаёт объект User из строки формата 'username: email'.
        """
        username, email = line.strip().split(": ")
        return User(username, email)


class Validator:
    """
    Класс для проверки корректности данных.
    """

    EMAIL_REGEX = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')  # шаблон для email

    @staticmethod
    def validate_email(email):
        """
        Возвращает True, если email корректен, иначе False.
        """
        return re.match(Validator.EMAIL_REGEX, email) is not None

    @staticmethod
    def validate_username(username):
        """
        Возвращает True, если имя корректно, иначе False.
        """
        return len(username) >= 2


class UserManager:
    """
    Класс для управления пользователями.
    Работает с файлом (чтение, запись, удаление).
    """

    def __init__(self, filename = "users.txt"):
        self.filename = filename

        # Если файла нет – создаём пустой
        if not os.path.exists(self.filename):
            open(self.filename, "w").close()

    def add_user(self, username, email):
        """
        Добавляет нового пользователя в файл.
        """
        Validator.validate_username(username)
        Validator.validate_email(email)
        user = User(username, email)

        # Запись в конец файла
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(str(user) + "\n")

        return user

    def list_users(self):
        """
        Возвращает список пользователей из файла.
        """
        users = []
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():  # пропускаем пустые строки
                    users.append(User.from_string(line))
                    pass
        return users

    def delete_user(self, username):
        """
        Удаляет пользователя по имени.
        Возвращает True, если пользователь найден и удалён.
        """
        users = self.list_users()
        new_users = [u for u in users if u.username != username]

        # Перезаписываем файл без удалённого пользователя
        with open(self.filename, "w", encoding="utf-8") as f:
            for u in new_users:
                f.write(str(u) + "\n")

        return len(users) != len(new_users)


class Logger:
    """
    Логирование событий в консоль и в log.txt.
    """

    LOGFILE = "log.txt"

    @staticmethod
    def clear_log():
        """
        Очищает лог-файл при старте программы.
        """
        open(Logger.LOGFILE, "w", encoding="utf-8").close()

    @staticmethod
    def log(message):
        """
        Записывает сообщение в консоль и лог-файл.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text = f"[{timestamp}] {message}"
        print(text)
        with open(Logger.LOGFILE, "a", encoding="utf-8") as f:
            f.write(text + "\n")


class Application:
    """
    Главный класс приложения.
    Управляет меню и взаимодействием пользователя с программой.
    """

    def __init__(self):
        self.manager = UserManager()

    @staticmethod
    def input_valid_username():
        """
        Запрашивает имя, пока оно не будет корректным.
        """
        while True:
            username = input("\nВведите имя (мин. 2 символа): ")
            if Validator.validate_username(username):
                return username
            Logger.log("Некорректное имя. Попробуйте снова.")

    @staticmethod
    def input_valid_email():
        """
        Запрашивает email, пока он не будет корректным.
        """
        while True:
            email = input("\nВведите email: ")
            if Validator.validate_email(email):
                return email
            Logger.log("Некорректный email. Попробуйте снова.")

    def run(self):
        """
        Запуск меню программы.
        """
        Logger.clear_log() # очистка логов при каждом старте
        Logger.log("Программа запущена")

        while True:
            print("\n--- Меню ---")
            print("1. Добавить пользователя")
            print("2. Показать пользователей")
            print("3. Удалить пользователя")
            print("4. Выход")

            choice = input("\nВыберите действие: ")

            if choice == "1":
                username = self.input_valid_username()
                email = self.input_valid_email()
                user = self.manager.add_user(username, email)
                Logger.log(f"Добавлен {user}")

            elif choice == "2":
                users = self.manager.list_users()
                if users:
                    Logger.log("Список пользователей:")
                    for u in users:
                        print("-", u)
                else:
                    Logger.log("Список пуст")

            elif choice == "3":
                username = input("\nВведите имя для удаления: ")
                if self.manager.delete_user(username):
                    Logger.log(f"Пользователь {username} удалён")
                else:
                    Logger.log(f"Пользователь {username} не найден")

            elif choice == "4":
                Logger.log("Программа завершена")
                break

            else:
                Logger.log("Неизвестная команда")


if __name__ == "__main__":
    Application().run()