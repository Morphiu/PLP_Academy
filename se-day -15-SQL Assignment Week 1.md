Assignment Questions
1. State and Explain the components of a DBMS(Database Management System)

>1.	Hardware: It includes HDDs, SSDs and other storage media to store actual data. Powerful computers to run the DBMS software and process user requests. Routers and switches to enable communication between different DBMS components.
>2.	Software: The core software that manages the database, database engine, query processor and transaction manager. The underlying OS that provides the environment to run the DBMS. Other programs that help in DB administration, backup and recovery.
>3.	Data: Tables that store data in rows and columns. Individual rows in a table represent specific entities (Records). Fields, columns in a table, representing specific attributes of an entity.
>4.	Procedures: Stored procedures that are precompiled blocks of SQL code that can be executed to perform specific tasks. Triggers which are automatically executed procedures in response to events such as data insertion and deletion
>5.	Database Access Language (DAL): SQL, the most common language used to interact with DBs allowing users to query, insert, update, insert, update and delete data. Other languages like PL/SQL, T-SQL or NoSQL query languages.

2. What is a relational database? Give 4 examples.

>It is a type of database that organizes data into tables with rows and columns. These tables are interconnected through relationships, allowing you to efficiently store and retrieve data.   
>Here are 4 common examples of relational databases:
>1.	E-commerce Database:
>>1.	Customers table: customer_id, name, email, address   
>>2.	Orders table: order_id, customer_id, order_date, total_amount
>>3.	Products table: product_id, name, price, quantity_in_stock   
>>4.	Order_Items table: order_id, product_id, quantity, price   
>2.	Library Database:
>>1.	Books table: book_id, title, author, publication_year
>>2.	Members table: member_id, name, address, phone_number
>>3.	Loans table: loan_id, book_id, member_id, loan_date, due_date
>3.	School Database:
>>1.	Students table: student_id, name, age, grade
>>2.	Courses table: course_id, course_name, instructor
>>3.	Enrollments table: enrollment_id, student_id, course_id, grade
>4.	Hospital Database:
>>1.	Patients table: patient_id, name, age, address
>>2.	Doctors table: doctor_id, name, specialization   
>>3.	Appointments table: appointment_id, patient_id, doctor_id, date, time


3. State and Explain three classifications of SQL?

>1. Data Definition Language (DDL): Used to define the database schema, including creating, modifying, and deleting database objects like tables, indexes, and views. Common DDL Commands include: 
>>1.	CREATE TABLE: Creates a new table.
>>2.	ALTER TABLE: Modifies an existing table.
>>3.	DROP TABLE: Deletes a table.
>>4.	CREATE INDEX: Creates an index 1 to improve query performance.   
>>5.	DROP INDEX: Deletes an index.
>2. Data Manipulation Language (DML): Used to manipulate data within the database, including inserting, updating, and deleting records. Common DML Commands include: 
>>1.	INSERT INTO: Inserts new records into a table.
>>2.	UPDATE: Modifies existing records in a table.
>>3.	DELETE FROM: Deletes records from a table.
>>4.	SELECT: Retrieves data from one or more tables.
>3. Data Control Language (DCL): Used to control access to the database and manage user privileges. Common DCL Commands include: 
>>1.	GRANT: Grants privileges to users or roles.
>>2.	REVOKE: Revokes privileges from users or roles.

4. What is the difference between a Primary Key and a Foreign Key?

>Primary Key(PK) Foreign Key(FK)
> A PK is unique identifier for each record in a table while a FK has column(s) in one table that refers to the primary key of another table. 
> A PK ensures that each row is distinct while a FK	establishes relationships between tables.
> A PK cannot contain null values while A FK can be null, but not often to maintain data integrity.

5. What is an Entity-Relationship Diagram (ERD)?

> An ERD is a graphical representation of a database schema. It illustrates how entities (objects or concepts) relate to each other.
> It's a visual tool used in database design to plan the structure of a database.
> Key Components of an ER Diagram:
>1.	Entities: Represented by rectangles. Entities are objects or concepts about which you want to store information. Examples: Customers, Products, Orders, Employees   
>2.	Attributes: Represented by ovals connected to entities.  Attributes are the properties of an entity. Examples: Customer ID, Customer Name, Product Name, Price   
>3.	Relationships: Represented by lines connecting entities. Relationships show how entities are related to each other. Types of Relationships: 
>>1.	One-to-One: One instance of an entity is related to exactly one instance of another entity. (Example: One person can have one passport)   
>>2.	One-to-Many: One instance of an entity is related to many instances of another entity. (Example: One author can write many books)   
>>3.	Many-to-Many: Many instances of one entity are related to many instances of another entity. (Example: Many students can enrol in many courses)   


6. What are the advantages of relational databases?

>1.	Data Integrity: They adhere to ACID (Atomicity, Consistency, Isolation, Durability) to ensure data is trustworthy and consistent.
>2.	Data Consistency: Data is organized into tables with well-defined relationships, reducing redundancy and inconsistencies. Changes made to one table can be automatically propagated to related tables.
>3.	Data Security: User permissions can be defined to restrict access to sensitive data and Data can be encrypted to protect it from unauthorized access.
>4.	Data Validation: Constraints like primary keys, foreign keys and unique constraints can be enforced to maintain data accuracy.

7. State four types of data type used to store data in tables?

>1.	Integer: Used to store whole numbers. 
>>•	Examples: INT, SMALLINT, BIGINT
>2.	Float/Decimal: Used to store numbers with decimal points. 
>>•	Examples: FLOAT, DOUBLE, DECIMAL
>3.	Character/String: Used to store text data. 
>>•	Examples: CHAR, VARCHAR
>4.	Date/Time: Used to store date and time values. 
>>•	Examples: DATE, TIME, DATETIME, TIMESTAMP

8. What is the purpose of a database management system (DBMS)?

>1.	Data Storage: Stores large amounts of structured data in a systematic and organized manner to ensure data integrity and consistency.   
>2.	Data Retrieval: Provides efficient methods to retrieve specific data based on various criteria by supporting complex queries and data analysis.
>3.	Data Manipulation: Allows users to modify, update, and delete data within the database by providing tools for data entry, editing, and deletion.   
>4.	Data Security: Implements security measures to protect data from unauthorized access through ccontroling user permissions and access to sensitive information.   
>5.	Data Integrity: Ensures data accuracy and consistency through validation rules and constraints.   
>6.	Data Backup and Recovery: Provides mechanisms for creating regular backups to safeguard data to enable efficient data recovery in case of system failures or data corruption.

