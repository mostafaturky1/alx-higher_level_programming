-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
	state_id INT,
	`name` VARCHAR(256),
	FOREIGN KEY(state_id)
	REFERANCES states(id)
);
