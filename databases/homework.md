# Eric Liu
#SQL Query for homework

#Practice your homework query here.
#Please save it to your repository.
#It is necessary to complete the homework before the asynchronous work.

sql_query_string = """

--Type your homework query below
SELECT First, Last, studentID, Grade, Scantime, Status, Date, CourseSection AS CourseSec, Attendance, Teacher, (Period=1) AS pd1
FROM
(
SELECT s.First, s.Last, s.studentID, s.Grade, s.ScanTime, s.Status, Date, CourseSection, Attendance, Teacher, Period 
FROM scan AS s
INNER JOIN periodAtt AS p
ON s.studentID=p.studentID AND SUBSTR(s.scanTime, 1, 9)=p.date
WHERE Attendance="A"
ORDER BY s.Last ASC) 
AS allCuts

"""
 
#Exectue the SQL query
result_df = sql_query_to_pd(sql_query_string, db_name='default.db')
result_df
