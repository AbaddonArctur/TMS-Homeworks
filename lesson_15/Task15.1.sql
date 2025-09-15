/*-----1-----*/

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_id INT REFERENCES authors(id) ON DELETE CASCADE,
    publication_year INT
);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    book_id INT REFERENCES books(id) ON DELETE CASCADE,
    quantity INT
);

INSERT INTO authors (first_name, last_name)
VALUES ('Дэн', 'Браун'),
       ('Джордж', 'Мартин'),
       ('Говард', 'Лавкрафт'),
       ('Стивен', 'Кинг'),
       ('Братья', 'Стругацкие'),
       ('Дмитрий', 'Глуховский'),
       ('Абаддон', 'Арктур'),
       ('Ариандель', 'Лоуренс');

INSERT INTO books (title, author_id, publication_year)
VALUES ('Точка обмана', 1, 2001),
       ('Ангелы и демоны', 1, 2000),
       ('Код да Винчи', 1, 2003),
       ('Инферно', 1, 2013),
       ('Происхождение', 1, 2017),
       ('Игра престолов', 2, 1996),
       ('Межевый рыцарь', 2, 1998),
       ('Танец с драконами', 2, 2011),
       ('Зов Ктулху', 3, 1926),
       ('Сомнамбулический поиск неведомого Кадата', 3, 1927),
       ('Цвет иного мира', 3, 1927),
       ('Хребты Безумия', 3, 1931),
       ('Тень над Иннсмутом', 3, 1931),
       ('Противостояние', 4, 1978),
       ('Оно', 4, 1986),
       ('Зелёная миля', 4, 1996),
       ('Ловец снов', 4, 2001),
       ('Понедельник начинается в субботу', 5, 1965),
       ('Обитаемый остров', 5, 1969),
       ('Пикник на обочине', 5, 1972),
       ('Метро 2033', 6, 2005),
       ('Будущее', 6, 2013);

INSERT INTO books (title, publication_year)
VALUES ('Некрономикон', 666),
       ('Библия', 0),
       ('Огма Инфиниум', 9999);

INSERT INTO sales (book_id, quantity)
VALUES (1, 1000),
       (2, 1520),
       (3, 5000),
       (4, 4000),
       (5, 3500),
       (6, 10000),
       (7, 1200),
       (8, 2300),
       (9, 1480),
       (10, 900),
       (11, 770),
       (12, 800),
       (13, 1230),
       (14, 1160),
       (15, 2800),
       (16, 5400),
       (17, 2600),
       (18, 520),
       (19, 1990),
       (20, 2740),
       (21, 9210),
       (22, 3260),
       (23, 1),
       (24, 100000),
       (25, null);

/*-----2-----*/

SELECT b.title AS book_title,
       a.first_name AS first_name,
       a.last_name AS last_name
FROM books b
INNER JOIN authors a ON b.author_id = a.id;

SELECT a.first_name AS first_name,
       a.last_name AS last_name,
       b.title AS book_title
FROM authors a
LEFT JOIN books b ON a.id = b.author_id;

SELECT b.title AS book_title,
       a.first_name AS first_name,
       a.last_name AS last_name
FROM authors a
RIGHT JOIN books b ON a.id = b.author_id;

/*-----3-----*/

SELECT b.title AS book_title,
       a.first_name AS first_name,
       a.last_name AS last_name,
       s.quantity AS quantity
FROM authors a
INNER JOIN books b ON a.id = b.author_id
INNER JOIN sales s ON b.id = s.book_id;

SELECT a.first_name AS first_name,
       a.last_name AS last_name,
       b.title AS book_title,
       s.quantity AS quantity
FROM authors a
LEFT JOIN books b ON a.id = b.author_id
LEFT JOIN sales s ON b.id = s.book_id;

/*-----4-----*/

SELECT a.first_name AS first_name,
       a.last_name AS last_name,
       SUM(s.quantity) AS total_sold
FROM authors a
INNER JOIN books b ON a.id = b.author_id
INNER JOIN sales s ON b.id = s.book_id
GROUP BY a.first_name, a.last_name;

SELECT a.first_name AS first_name,
       a.last_name AS last_name,
       COALESCE(SUM(s.quantity), 0) AS total_sold
FROM authors a
LEFT JOIN books b ON a.id = b.author_id
LEFT JOIN sales s ON b.id = s.book_id
GROUP BY a.first_name, a.last_name;

/*-----5-----*/

SELECT a.first_name AS first_name,
       a.last_name AS last_name,
       SUM(s.quantity) AS total_sold
FROM authors a
JOIN books b ON a.id = b.author_id
JOIN sales s ON b.id = s.book_id
GROUP BY a.first_name, a.last_name
HAVING SUM(s.quantity) = (
    SELECT MAX(total_sales)
    FROM (
        SELECT SUM(s2.quantity) AS total_sales
        FROM authors a2
        JOIN books b2 ON a2.id = b2.author_id
        JOIN sales s2 ON b2.id = s2.book_id
        GROUP BY a2.id
    ) sub
);

SELECT
    b.title AS book_title,
    a.first_name AS first_name,
    a.last_name AS last_name,
    SUM(s.quantity) AS total_sold
FROM books b
LEFT JOIN authors a ON b.author_id = a.id
LEFT JOIN sales s ON b.id = s.book_id
GROUP BY b.title, a.first_name, a.last_name
HAVING SUM(s.quantity) > (
    SELECT AVG(total_sales)
    FROM (
        SELECT SUM(s2.quantity) AS total_sales
        FROM books b2
        JOIN sales s2 ON b2.id = s2.book_id
        GROUP BY b2.id
    ) sub
);