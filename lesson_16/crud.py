from sqlalchemy.orm import Session
from models import Author, Book, Genre

# ---------- Автор ----------
def create_author(db: Session, name: str):
    author = Author(name=name)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

def get_author_by_name(db: Session, name: str):
    return db.query(Author).filter(Author.name.ilike(f"%{name}%")).all()

def update_author_name(db: Session, author_id: int, new_name: str):
    author = db.query(Author).filter(Author.id == author_id).first()
    if author:
        author.name = new_name
        db.commit()
        db.refresh(author)
    return author

def delete_author(db: Session, author_id: int):
    author = db.query(Author).filter(Author.id == author_id).first()
    if author:
        db.delete(author)
        db.commit()
    return author

# ---------- Жанр ----------
def create_genre(db: Session, name: str):
    genre = Genre(name=name)
    db.add(genre)
    db.commit()
    db.refresh(genre)
    return genre

def update_genre_name(db: Session, genre_id: int, new_name: str):
    genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if genre:
        genre.name = new_name
        db.commit()
        db.refresh(genre)
    return genre

def delete_genre(db: Session, genre_id: int):
    genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if genre:
        db.delete(genre)
        db.commit()
    return genre

# ---------- Книга ----------
def create_book(db: Session, title: str, author_id: int, genre_id: int, year: int):
    book = Book(title=title, author_id=author_id, genre_id=genre_id, published_year=year)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_books_by_author(db: Session, author_name: str):
    return (db.query(Book)
              .join(Author)
              .filter(Author.name.ilike(f"%{author_name}%"))
              .all())

def get_books_by_genre(db: Session, genre_name: str):
    return (db.query(Book)
              .join(Genre)
              .filter(Genre.name.ilike(f"%{genre_name}%"))
              .all())

def update_book_title(db: Session, book_id: int, new_title: str):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        book.title = new_title
        db.commit()
        db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book