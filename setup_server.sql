-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS fantasy_db;
CREATE USER IF NOT EXISTS 'dev'@'localhost' IDENTIFIED BY 'dev_pass';
GRANT ALL PRIVILEGES ON `fantasy_db`.* TO 'dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'dev'@'localhost';
FLUSH PRIVILEGES;