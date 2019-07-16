-- create states in usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id int NOT NULL UNIQUE AUTO_INCREMENT,
    name varchar(256) NOt NULL,
    PRIMARY KEY (ID)
);
