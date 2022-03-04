# Eric Liu
# SQL for Async Challenge 2

SELECT First, Last, studentID, Grade, Scantime, Status, Date, CourseSection AS CourseSec, Attendance, Teacher, Period, Parent1Phone, Parent2Phone, parentEmail
FROM
(
SELECT s.First, s.Last, s.studentID, s.Grade, s.ScanTime, s.Status, Date, CourseSection, Attendance, Teacher, Period, b.Parent1Phone, b.Parent2Phone, b.ParentEmail
FROM scan AS s, bio as b
INNER JOIN periodAtt AS p
ON s.studentID=p.studentID AND s.studentID = b.studentID
AND SUBSTR(s.scanTime, 1, 9)=p.date
WHERE Attendance="A"
ORDER BY s.Last ASC) 
AS allCuts
