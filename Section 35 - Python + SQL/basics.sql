/*creating a table */
CREATE TABLE dogs (
    name TEXT,
    breed TEXT,
    age INTEGER
);

/* can just paste code above in terminal in sqlite3 but it will terminate on .exit 

to save in database need to create a file dogs.db and it will create a file in directory.
*/

/* inserting sql */
INSERT INTO dogs (name, breed, age) VALUES ("BLUE", "German Shepherd", 3);

-- bulk insert
INSERT INTO dogs (name, breed, age) VALUES ("CHAMP", "CHIHUAHUA Shepherd", 12);
INSERT INTO dogs (name, breed, age) VALUES ("ROSE", "KORGI", 10);
-- to insert into database, need to open the database file with sqlite3, then use .read basics.sql

/* selecting from sql database - select all columns */
SELECT * FROM dogs;

/*to specify the column, we can do */
SELECT name FROM dogs;

/*select particular dogs that are with name ROSE, or breed korgi or breed not chihuahua */
SELECT * FROM dogs WHERE name IS "ROSE";
SELECT * FROM dogs WHERE breed IS "KORGI";
SELECT * FROM dogs WHERE breed IS "KORGI";
SELECT * FROM dogs WHERE breed IS NOT "CHIHUAHUA"; --AND BREED IS NOT "KORGI"

--select by age
SELECT * FROM dogs WHERE age > 9

--select by name containing something
SELECT * FROM dogs WHERE name LIKE "%gg%"--notice the wildcard any character %
