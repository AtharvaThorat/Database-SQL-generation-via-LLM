import duckdb

# Query: Which instructor teaches the most students?
result = duckdb.sql("""
    SELECT i.full_name,
           COUNT(DISTINCT tm.student_id) AS students_taught
    FROM 'instructor.csv' i
    JOIN 'projectsection.csv' ps ON ps.instructor_id = i.instructor_id
    JOIN 'team.csv' t ON t.section_id = ps.section_id
    JOIN 'teammember.csv' tm ON tm.team_id = t.team_id
    GROUP BY i.instructor_id, i.full_name
    ORDER BY students_taught DESC
    LIMIT 1
""")

print("=" * 60)
print("Q2: Most Popular Instructor (By Student Count)")
print("=" * 60)
result.show()