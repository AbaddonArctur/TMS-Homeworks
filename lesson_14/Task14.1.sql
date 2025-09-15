CREATE TABLE Employees (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(50),
    Position VARCHAR(50),
    Department VARCHAR(50),
    Salary NUMERIC(10,2)
);

INSERT INTO Employees (Name, Position, Department, Salary)
VALUES ('Биггус Дикус', 'Director', 'Administration', '25000'),
       ('Инконтинентия Баттокс', 'Specialist', 'Sales', '3000'),
       ('Иероним Лекс', 'Manager', 'Sales', '4200'),
       ('Паровозик Томас', 'Senior QA Engineer', 'IT', '8000'),
       ('Альтьера Каннингем', 'Junior Assembler Developer', 'IT', '10000'),
       ('Томас Бебри', 'Project Manager', 'IT', '15000');

UPDATE Employees
SET Position = 'Manager',
    Department = 'Cleaning',
    Salary = '2000'
WHERE Name = 'Альтьера Каннингем';

ALTER TABLE Employees
ADD COLUMN HireDate DATE;

UPDATE Employees
SET HireDate = '2012-12-21' WHERE Name = 'Биггус Дикус';
UPDATE Employees
SET HireDate = '2013-01-03' WHERE Name = 'Инконтинентия Баттокс';
UPDATE Employees
SET HireDate = '2015-05-08' WHERE Name = 'Иероним Лекс';
UPDATE Employees
SET HireDate = '2017-02-27' WHERE Name = 'Паровозик Томас';
UPDATE Employees
SET HireDate = '2016-08-14' WHERE Name = 'Альтьера Каннингем';
UPDATE Employees
SET HireDate = '2015-06-11' WHERE Name = 'Томас Бебри';

CREATE OR REPLACE FUNCTION GetManagers()
RETURNS TEXT
AS $$
DECLARE
    all_managers TEXT;
BEGIN
    SELECT string_agg(Name, ', ') INTO all_managers FROM Employees WHERE  Position = 'Manager';
    RETURN all_managers;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION GetHighSalaryEmployees()
RETURNS TEXT
AS $$
DECLARE
    high_salary TEXT;
BEGIN
    SELECT string_agg(Name, ', ') INTO high_salary FROM Employees WHERE  Salary > 5000;
    RETURN high_salary;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION GetSalesEmployees()
RETURNS TEXT
AS $$
DECLARE
    all_sales TEXT;
BEGIN
    SELECT string_agg(Name, ', ') INTO all_sales FROM Employees WHERE Department = 'Sales';
    RETURN all_sales;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION GetAverageSalary()
RETURNS  NUMERIC AS $$
DECLARE
    avg_salary NUMERIC;
BEGIN
    SELECT AVG(Salary) INTO avg_salary FROM Employees;
    RETURN avg_salary;
END;
$$ LANGUAGE plpgsql;

SELECT GetManagers();
SELECT GetHighSalaryEmployees();
SELECT GetSalesEmployees();
SELECT GetAverageSalary();

DROP TABLE Employees;