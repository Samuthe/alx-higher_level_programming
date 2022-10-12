-- display a list of the same records from second_table

SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
