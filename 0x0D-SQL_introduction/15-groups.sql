--  lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server showing score and number sorted by number of records
--  lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server showing score and number sorted by number of records
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
