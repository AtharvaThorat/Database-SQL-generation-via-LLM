import duckdb

# Query: Which coding course has the most students?
# Uses the same week/block matching logic to determine attendance
result = duckdb.sql("""
    SELECT c.title AS course_name,
           COUNT(DISTINCT tm.student_id) AS students
    FROM 'course.csv' c
    JOIN 'courseoffering.csv' co ON c.course_id = co.course_id
    JOIN 'projectsection.csv' ps ON ps.week = co.week AND ps.block = co.block
    JOIN 'team.csv' t ON t.section_id = ps.section_id
    JOIN 'teammember.csv' tm ON tm.team_id = t.team_id
    GROUP BY c.title
    ORDER BY students DESC
    LIMIT 1
""")

print("=" * 60)
print("Q1: Course with Most Number of Students")
print("=" * 60)
result.show()