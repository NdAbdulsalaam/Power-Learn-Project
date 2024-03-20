-- Create the StudentsDB database
CREATE DATABASE IF NOT EXISTS StudentsDB;

-- Use the StudentsDB database
USE StudentsDB;

-- Create the Students table
CREATE TABLE IF NOT EXISTS Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Email VARCHAR(100),
    Major VARCHAR(50)
);
