CREATE DATABASE `password_manager`;
USE `password_manager`;

-- create user table --
DROP TABLE IF EXISTS `User`;
CREATE TABLE `User`(
       `id` INT AUTO_INCREMENT PRIMARY KEY,
       `username` VARCHAR(20) UNIQUE,
       `password` VARCHAR(100) NOT NULL);

-- create account table --
DROP TABLE IF EXISTS `Account`;
CREATE TABLE `Account`(
       `id` INT AUTO_INCREMENT PRIMARY KEY,
       `user_id` INT ,
       `website` VARCHAR(100) NOT NULL,
       `username` VARCHAR(20) NOT NULL,
       `password` VARBINARY(200) NOT NULL,
       
       CONSTRAINT Fk_User FOREIGN KEY (`user_id`)
       REFERENCES `User`(`id`)
);

SELECT * FROM `User`;
SELECT * FROM `Account`;       