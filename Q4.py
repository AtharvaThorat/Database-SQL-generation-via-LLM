import duckdb

# Query: List all classes with enrollment counts, sorted by popularity
result = duckdb.sql("""
    SELECT c.title AS class_name,
           co.week || ' ' || co.block AS when_offered,
           COUNT(DISTINCT tm.student_id) AS students_present
    FROM 'courseoffering.csv' co
    JOIN 'course.csv' c ON c.course_id = co.course_id
    JOIN 'projectsection.csv' ps ON ps.week = co.week AND ps.block = co.block
    JOIN 'team.csv' t ON t.section_id = ps.section_id
    JOIN 'teammember.csv' tm ON tm.team_id = t.team_id
    GROUP BY c.title, co.week, co.block
    ORDER BY students_present DESC, c.title
""")

print("=" * 60)
print("Q4: Class Popularity Listing")
print("=" * 60)
result.show()