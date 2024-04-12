-- Step 1: Create a new MySQL database named "UniversityDB"
CREATE DATABASE UniversityDB;

-- Step 2: Design a table named "Students"
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    Major VARCHAR(50)
);

-- Step 3: Insert sample data into the "Students" table
INSERT INTO Students (StudentID, FirstName, LastName, Age, Major) VALUES
(1, 'John', 'Doe', 20, 'Computer Science'),
(2, 'Jane', 'Smith', 22, 'Biology'),
(3, 'Alice', 'Johnson', 21, 'Psychology'),
(4, 'Bob', 'Williams', 19, 'Engineering'),
(5, 'Emily', 'Brown', 23, 'History');

-- Step 4: Alter the "Students" table to add a new column named "GPA"
ALTER TABLE Students ADD GPA DECIMAL(3, 2);

-- Step 5: Insert GPA values for the existing records in the "Students" table
UPDATE Students SET GPA = 3.5 WHERE StudentID = 1;
UPDATE Students SET GPA = 3.8 WHERE StudentID = 2;
UPDATE Students SET GPA = 3.2 WHERE StudentID = 3;
UPDATE Students SET GPA = 3.9 WHERE StudentID = 4;
UPDATE Students SET GPA = 3.6 WHERE StudentID = 5;

-- Step 6: Rename the table from "Students" to "EnrolledStudents"
ALTER TABLE Students RENAME TO EnrolledStudents;

-- Step 7: Create a new table named "Courses"
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    Instructor VARCHAR(100),
    Credits INT
);

-- Step 8: Insert sample data into the "Courses" table
INSERT INTO Courses (CourseID, CourseName, Instructor, Credits) VALUES
(1, 'Introduction to Computer Science', 'Dr. Smith', 3),
(2, 'Biology 101', 'Prof. Johnson', 4),
(3, 'Psychology of Human Behavior', 'Dr. Brown', 3);

-- Step 9: Drop the "EnrolledStudents" table from the database
DROP TABLE EnrolledStudents;


-- Justification:

-- I used appropriate data types for each column to ensure efficient storage and retrieval of data.
-- Sample data was inserted to populate the tables and demonstrate functionality.
-- The addition of the "GPA" column allows for the storage of GPA values for each student.
-- The table "EnrolledStudents" was renamed to provide a more descriptive name.
-- The "Courses" table was created to store information about courses offered by the university.
-- The "EnrolledStudents" table was dropped as instructed, assuming it is no longer needed.