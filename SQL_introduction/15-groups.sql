-- display number of records that share the same score
-- scores should be displayed in descending order

SELECT score, count(score) as 'number'
FROM second_table
GROUP BY score
ORDER BY score DESC;
