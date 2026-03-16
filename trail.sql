CREATE TABLE students(
stud_id int,
student_name text                                          --This is for creating the table "students"
age int
);
ALTER TABLE students
ADD COLUMN course VARCHAR;
ALTER TABLE students
DROPV COLUMN course;

INSERT INTO students(stud_id,student_name,age)
VALUES
(1,'zuena',21),
(2,'twaha',24),
(3,'rahma',28);
SELECT * FROM students;
DROP TABLE students;