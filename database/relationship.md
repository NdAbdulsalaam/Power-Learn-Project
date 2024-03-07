Database relationships are fundamental concepts in relational database management systems (RDBMS) that define how data in different tables are related to each other. Three common types of database relationships are One-to-One, One-to-Many, and Many-to-Many. Let's discuss each of them in detail:

1. One-to-One Relationship:
   - In a One-to-One relationship, each record in one table is related to exactly one record in another table, and vice versa.
   - This type of relationship is relatively rare in database design but can be useful for separating sensitive or less frequently accessed data into a separate table.
   - An example of a One-to-One relationship is the relationship between a "Person" table and a "Driver's License" table, where each person has only one driver's license, and each driver's license belongs to only one person.

2. One-to-Many Relationship:
   - In a One-to-Many relationship, each record in the parent table can be related to one or more records in the child table, but each record in the child table is related to only one record in the parent table.
   - This is one of the most common types of relationships in relational databases and is used to model hierarchical or nesting relationships.
   - An example of a One-to-Many relationship is the relationship between a "Department" table and an "Employee" table, where each department can have multiple employees, but each employee belongs to only one department.

3. Many-to-Many Relationship:
   - In a Many-to-Many relationship, each record in the parent table can be related to multiple records in the child table, and vice versa.
   - This type of relationship requires a junction table, also known as an association table or bridge table, to represent the connections between the two related tables.
   - An example of a Many-to-Many relationship is the relationship between a "Student" table and a "Course" table in a university database, where each student can enroll in multiple courses, and each course can have multiple students.
