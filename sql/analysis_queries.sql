-- ============================================
-- STUDENT CAREER PREFERENCE ANALYSIS
-- SQL ANALYSIS
-- ============================================

USE student_career_analysis;


-- QUERY 1: Total number of students

SELECT COUNT(*) AS total_students
FROM student_career_data;


-- QUERY 2: View first 10 records

SELECT *
FROM student_career_data
LIMIT 10;


-- QUERY 3: Table structure

DESCRIBE student_career_data;


-- QUERY 4: Students by preferred career sector

SELECT Preferred_Sector,
       COUNT(*) AS Total_Students
FROM student_career_data
GROUP BY Preferred_Sector;


-- QUERY 5: Sector preference percentage

SELECT Preferred_Sector,
       COUNT(*) AS Total_Students,
       ROUND(
           COUNT(*) * 100.0 /
           (SELECT COUNT(*) FROM student_career_data),
           2
       ) AS Percentage
FROM student_career_data
GROUP BY Preferred_Sector
ORDER BY Percentage DESC;