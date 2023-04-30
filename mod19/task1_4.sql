    SELECT group_id, MIN(c_grade) as min, MAX(c_grade) as max, AVG(c_grade) as avg
           FROM ( SELECT group_id, count(grade) as c_grade
                FROM students
                JOIN assignments_grades ON students.student_id = assignments_grades.student_id
                WHERE grade = 0
                GROUP BY students.student_id, group_id)
           GROUP BY group_id