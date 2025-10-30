import duckdb

# Query: Which instructor has the highest rating?
result = duckdb.sql("""
    SELECT i.full_name,
           ROUND(AVG(r.stars), 2) AS avg_stars,
           COUNT(*) AS ratings_received
    FROM 'rating.csv' r
    JOIN 'instructor.csv' i ON i.instructor_id = r.target_id
    WHERE r.target_type = 'INSTRUCTOR'
    GROUP BY i.instructor_id, i.full_name
    ORDER BY avg_stars DESC, ratings_received DESC
    LIMIT 1
""")

print("=" * 60)
print("Q3: Most Popular Instructor (By Highest Rating)")
print("=" * 60)
result.show()