import duckdb

# Query: Calculate total payment for a specific instructor
instructor_name = "Dr. Alice Johnson"  
result = duckdb.sql(f"""
    SELECT i.full_name,
           3 * COUNT(DISTINCT co.offering_id) * i.teach_rate_cents AS teach_pay_cents,
           3 * COUNT(DISTINCT ps.section_id) * i.supervise_rate_cents AS supervise_pay_cents,
           (3 * COUNT(DISTINCT co.offering_id) * i.teach_rate_cents + 
            3 * COUNT(DISTINCT ps.section_id) * i.supervise_rate_cents) AS total_pay_cents,
           (3 * COUNT(DISTINCT co.offering_id) * i.teach_rate_cents + 
            3 * COUNT(DISTINCT ps.section_id) * i.supervise_rate_cents) / 100.0 AS total_pay_dollars
    FROM 'instructor.csv' i
    LEFT JOIN 'courseoffering.csv' co ON co.instructor_id = i.instructor_id
    LEFT JOIN 'projectsection.csv' ps ON ps.instructor_id = i.instructor_id
    WHERE i.full_name = '{instructor_name}'
    GROUP BY i.instructor_id, i.full_name, i.teach_rate_cents, i.supervise_rate_cents
""")

print("=" * 60)
print(f"Q5: Payment for Instructor: {instructor_name}")
print("=" * 60)
result.show()