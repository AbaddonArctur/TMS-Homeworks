from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)  # SERIAL
    name = Column(String(255), unique=True, nullable=False)

    books = relationship("Book", back_populates="author", cascade="all, delete")

class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, autoincrement=True)  # SERIAL
    name = Column(String(255), unique=True, nullable=False)

    books = relationship("Book", back_populates="genre")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)  # SERIAL
    title = Column(String(255), nullable=False)
    published_year = Column(Integer)

    author_id = Column(Integer, ForeignKey("authors.id", ondelete="CASCADE"))
    genre_id = Column(Integer, ForeignKey("genres.id", ondelete="SET NULL"))

    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")