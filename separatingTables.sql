--Creating the diffrent views for the diffrent analysts 
CREATE VIEW q1 AS
SELECT *
FROM exchangerates
ORDER BY 1
LIMIT 294;

--
CREATE VIEW q2 AS 
SELECT *
FROM exchangerates
ORDER BY 1
LIMIT 295
OFFSET 294;

--
CREATE VIEW q3 AS 
SELECT *
FROM exchangerates
ORDER BY 1
LIMIT 294
OFFSET 589;

SELECT * 
FROM q1

SELECT * 
FROM q2

SELECT * 
FROM q3