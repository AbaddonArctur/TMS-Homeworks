DROP TABLE IF EXISTS books CASCADE;
DROP TABLE IF EXISTS genres CASCADE;
DROP TABLE IF EXISTS authors CASCADE;

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_id INT REFERENCES authors(id) ON DELETE CASCADE,
    genre_id INT REFERENCES genres(id) ON DELETE SET NULL,
    publication_year INT
);

INSERT INTO authors (name)
VALUES ('Дэн Браун'),
       ('Джордж Мартин'),
       ('Говард Лавкрафт'),
       ('Стивен Кинг'),
       ('Братья Стругацкие'),
       ('Дмитрий Глуховский');

INSERT INTO genres (name) VALUES
('Триллер'),
('Ужасы'),
('Драма'),
('Фэнтези'),
('Постапокалиптика'),
('Фантастика');

INSERT INTO books (title, author_id, genre_id, publication_year)
VALUES ('Точка обмана', 1, 1, 2001),
       ('Ангелы и демоны', 1, 1, 2000),
       ('Код да Винчи', 1, 1, 2003),
       ('Инферно', 1, 1, 2013),
       ('Происхождение', 1, 1,  2017),
       ('Игра престолов', 2, 4, 1996),
       ('Межевый рыцарь', 2, 4, 1998),
       ('Танец с драконами', 2, 4, 2011),
       ('Зов Ктулху', 3, 2, 1926),
       ('Сомнамбулический поиск неведомого Кадата', 3, 4, 1927),
       ('Цвет иного мира', 3, 2, 1927),
       ('Хребты Безумия', 3, 2, 1931),
       ('Тень над Иннсмутом', 3, 2, 1931),
       ('Противостояние', 4, 5, 1978),
       ('Оно', 4, 2, 1986),
       ('Зелёная миля', 4, 3, 1996),
       ('Ловец снов', 4, 2, 2001),
       ('Понедельник начинается в субботу', 5, 6, 1965),
       ('Обитаемый остров', 5, 6, 1969),
       ('Пикник на обочине', 5, 6, 1972),
       ('Метро 2033', 6, 5, 2005),
       ('Будущее', 6, 6, 2013);

-- Удаление жанра
DELETE FROM genres WHERE name = 'Драма';

-- Редактирование автора
UPDATE authors SET name = 'Говард Филипс Лавкрафт' WHERE id = 3;

-- Редактирование жанра
UPDATE books SET genre_id = 2 WHERE title = 'Зелёная миля';

-- Вывод всех книг с авторами и жанрами
SELECT b.title, a.name AS author, g.name AS genre, b.publication_year
FROM books b
JOIN authors a ON b.author_id = a.id
LEFT JOIN genres g ON b.genre_id = g.id;

-- Поиск книг по жанру
SELECT b.title, a.name AS author, b.publication_year
FROM books b
JOIN genres g ON b.genre_id = g.id
JOIN authors a ON b.author_id = a.id
WHERE g.name = 'Ужасы';

-- Поиск книг по автору
SELECT b.title, b.publication_year, g.name AS genre
FROM books b
JOIN authors a ON b.author_id = a.id
LEFT JOIN genres g ON b.genre_id = g.id
WHERE a.name = 'Джордж Мартин';

-- Поиск по частичному совпадению (название)
SELECT * FROM books WHERE title ILIKE '%снов%';

-- Поиск по частичному совпадению (автор)
SELECT * FROM authors WHERE name ILIKE '%брат%';