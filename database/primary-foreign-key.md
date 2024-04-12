## **Primary Key and Foreign Key in Relational Databases**

A primary key and a foreign key are both essential concepts in relational databases, playing crucial roles in maintaining data integrity and establishing relationships between tables.

### 1. Primary Key:
- A primary key is a unique identifier for each record in a table.
- It ensures that each row in the table is uniquely identifiable.
- Primary keys are used to enforce entity integrity, ensuring that there are no duplicate records.
- By default, primary keys also enforce referential integrity, meaning they can be referenced by foreign keys in other tables.
- In most database systems, primary keys are implemented using indexes, which allow for efficient searching and retrieval of data.
- Common examples of primary keys include student IDs, order numbers, and product codes.

### 2. Foreign Key:
- A foreign key is a field in a table that establishes a relationship with the primary key of another table.
- It creates a link between two tables, representing a dependency or association between them.
- Foreign keys enforce referential integrity by ensuring that every value in the foreign key field corresponds to a valid value in the primary key field of the related table.
- Foreign keys can be used to implement various types of relationships between tables, such as one-to-one, one-to-many, or many-to-many.
- They facilitate the enforcement of business rules and constraints, such as ensuring that a child record cannot exist without a corresponding parent record.
- Foreign keys play a crucial role in maintaining data consistency and integrity in a relational database environment.

In summary, while a primary key uniquely identifies records within a table, a foreign key establishes relationships between tables, ensuring data consistency and integrity across the database. Together, they form the foundation of relational database design and help maintain the integrity of the data stored within the database.