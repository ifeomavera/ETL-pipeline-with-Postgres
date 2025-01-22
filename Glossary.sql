--Creating a view for currencies that are depreciated  
CREATE VIEW depreciate AS 
SELECT * 
FROM supportedcurrency
WHERE "Status" = 'DEPRECIATED';

--Creating a view with currencies that are available 
CREATE VIEW available AS 
SELECT * 
FROM supportedcurrency
WHERE "Status" = 'AVAILABLE';

--Checking if there is any other currency that may fall into another category
SELECT * 
FROM supportedcurrency
WHERE "Status" NOT IN ('DEPRECIATED', 'AVAILABLE');

--Glossary for the first analyst
CREATE VIEW glossaryq1 AS 
SELECT * 
FROM supportedcurrency
ORDER BY 1
LIMIT 294;

--Glossary for the second analyst
CREATE VIEW glossaryq2 AS 
SELECT * 
FROM supportedcurrency
ORDER BY 1
LIMIT 295
OFFSET 294;

--Glossary for the third analyst
CREATE VIEW glossaryq3 AS 
SELECT * 
FROM supportedcurrency
ORDER BY 1
LIMIT 294
OFFSET 589;

SELECT * 
FROM glossaryq1

SELECT *
FROM glossaryq2

SELECT *
FROM glossaryq3

SELECT * 
FROM depreciate