-- Create the Books table
CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(100),
    Author VARCHAR(100),
    Genre VARCHAR(50),
    PublicationYear INT
);

-- Populate the Books table with sample data
INSERT INTO Books (BookID, Title, Author, Genre, PublicationYear)
VALUES
    (1, 'The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 1925),
    (2, 'To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1960),
    (3, '1984', 'George Orwell', 'Dystopian', 1949),
    (4, 'Pride and Prejudice', 'Jane Austen', 'Romance', 1813),
    (5, 'The Catcher in the Rye', 'J.D. Salinger', 'Coming-of-Age', 1951),
    (6, 'Brave New World', 'Aldous Huxley', 'Dystopian', 1932),
    (7, 'The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 1937),
    (8, 'Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling', 'Fantasy', 1997),
    (9, 'The Da Vinci Code', 'Dan Brown', 'Thriller', 2003),
    (10, 'The Hunger Games', 'Suzanne Collins', 'Dystopian', 2008);

-- Retrieve all columns for books published in the year 2020
SELECT * FROM Books WHERE PublicationYear = 2020;

-- Find the distinct genres available in the Books table
SELECT DISTINCT Genre FROM Books;

-- Alias the column Author as BookAuthor in a query result
SELECT BookID, Title, Author AS BookAuthor, Genre, PublicationYear FROM Books;
