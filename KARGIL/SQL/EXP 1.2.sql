--EXP 1.2
CREATE TABLE Students (
    student_id INT,
    name VARCHAR(50),
    city VARCHAR(50),
    percentage DECIMAL(5,2)
);

INSERT INTO Students VALUES
(1, 'Amit', 'Delhi', 96.5),
(2, 'Riya', 'Mumbai', 94.2),
(3, 'Rahul', 'Delhi', 97.8),
(4, 'Sneha', 'Mumbai', 98.1),
(5, 'Ankit', 'Chandigarh', 95.6),
(6, 'Pooja', 'Delhi', 93.4),
(7, 'Karan', 'Chandigarh', 96.2);


---Without Case Statement
SELECT CITY , COUNT(*) AS STUDET_COUNT FROM Students 
WHERE percentage> 95
GROUP BY city;


-- WITH CASE STATEMENT
SELECT CITY, SUM(CASE WHEN percentage> 95 THEN 1
ELSE 0 END) AS STUDENT_COUNTS  FROM Students 
GROUP BY city

-- (II)

-- WITHOUT CASE STATEMENT


-- WITH CASE STATEMENT
SELECT CITY, AVG(CASE WHEN PERCENTAGE>95 THEN PERCENTAGE ELSE
NULL END) AS STUDENT_AVG  FROM Students 
GROUP BY city
ORDER BY STUDENT_AVG DESC;



