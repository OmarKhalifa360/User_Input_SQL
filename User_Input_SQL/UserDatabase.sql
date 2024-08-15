CREATE DATABASE UserDatabase;

USE UserDatabase;

CREATE TABLE Users (
user_id VARCHAR(255) PRIMARY KEY,
first_name VARCHAR(255),
last_name VARCHAR(255),
age INT,
gender VARCHAR(50),
year_of_birth INT
);