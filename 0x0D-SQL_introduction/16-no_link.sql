-- lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server no rows without a name value, score and name, sorted by score
-- lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server no rows without a name value, score and name, sorted by score
SELECT score, name FROM second_table WHERE CHAR_LENGTH(name) > 0 ORDER BY score DESC;
