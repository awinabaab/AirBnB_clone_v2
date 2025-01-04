-- Creates a database hbnb_test_db
-- Creates a new user hbnb_test in localhost
-- The password of hbnb_test should be set to hbnb_test_pwd
-- hbnb_test should have all privileges on only the database hbnb_test_db
-- hbnb_test should have SELECT privilege on only the database performance_schema

CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
