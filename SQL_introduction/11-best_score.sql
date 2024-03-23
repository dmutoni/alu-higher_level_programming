-- list all records where score >= 10
-- display score and name fields of each record
-- sort rows in descending order

SELECT score, name 
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
