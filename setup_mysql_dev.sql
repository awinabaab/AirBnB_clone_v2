-- Creates a database hbnb_dev_db
-- Creates a new user hbnb dev in localhost
-- The password of hbnb dev should be set to hbnb_dev_pwd
-- hbnb_dev should have all privileges on only the database hbnb_dev_db
-- hbnb_dev should have SELECT privilege on only the database performance_schema

CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
