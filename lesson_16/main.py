from database import SessionLocal
import crud

def run():

    db = SessionLocal()

    print("=== Добавляем авторов и жанры ===")
    den = crud.create_author(db, "Дэн Браун")
    martin = crud.create_author(db, "Джордж Мартин")
    tril = crud.create_genre(db, "Триллер")
    fant = crud.create_genre(db, "Фэнтези")

    print("=== Добавляем книги ===")
    book1 = crud.create_book(db, "Точка обмана", den.id, tril.id, 2001)
    book2 = crud.create_book(db, "Игра престолов", martin.id, fant.id, 1996)

    print("\nВсе книги Дэна Брауна:")
    for b in crud.get_books_by_author(db, "браун"):
        print(f"- {b.title} ({b.published_year})")

    print("\n=== Изменение имени автора ===")
    updated_author = crud.update_author_name(db, den.id, "Дэн Герхард Браун")
    print("Обновлённый автор:", updated_author.name)

    print("\n=== Изменение названия книги ===")
    updated_book = crud.update_book_title(db, book1.id, "Deception Point")
    print("Обновлённая книга:", updated_book.title)

    print("\n=== Удаление жанра ===")
    deleted_genre = crud.delete_genre(db, tril.id)
    print("Удалён жанр:", deleted_genre.name)

    print("\n=== Удаление книги ===")
    deleted_book = crud.delete_book(db, book2.id)
    print("Удалена книга:", deleted_book.title)

    print("\n=== Удаление автора ===")
    deleted_author = crud.delete_author(db, martin.id)
    print("Удалён автор:", deleted_author.name)

    db.close()

if __name__ == '__main__':
    run()