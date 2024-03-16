-- a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0
SELECT score, COUNT(*) AS record_count
FROM your_table_name
GROUP BY score
ORDER BY score DESC;
