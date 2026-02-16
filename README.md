
# 🚀 AI-Powered SQL Generation from Natural Language

### Turning Human Questions into Executable SQL using LLMs + DuckDB

---

<p align="center">
  <b>Natural Language ➜ LLM ➜ SQL ➜ DuckDB ➜ Structured Insights</b>
</p>

---

## 🧠 Project Vision

Modern data systems require technical expertise to write SQL.

This project explores how **Large Language Models (LLMs)** can bridge the gap between:

🗣 Human language
and
🗄 Structured database queries

The system demonstrates how natural language questions can be transformed into **accurate SQL queries**, executed on real relational datasets using **DuckDB**.

---

## 🎯 Core Objective

Build a lightweight AI-driven pipeline that:

✔ Accepts database-related questions
✔ Converts them into SQL queries
✔ Executes them on structured CSV tables
✔ Returns formatted analytical results

---

## 🏗️ System Architecture

```text
          ┌─────────────────────────┐
          │  Natural Language Query │
          │  "Which course has the  │
          │   most students?"       │
          └─────────────┬───────────┘
                        │
                        ▼
          ┌─────────────────────────┐
          │      LLM Reasoning      │
          │  (Text ➜ SQL Mapping)   │
          └─────────────┬───────────┘
                        │
                        ▼
          ┌─────────────────────────┐
          │     Generated SQL       │
          │ SELECT ... GROUP BY ... │
          └─────────────┬───────────┘
                        │
                        ▼
          ┌─────────────────────────┐
          │       DuckDB Engine     │
          │  (Executes on CSV Data) │
          └─────────────┬───────────┘
                        │
                        ▼
          ┌─────────────────────────┐
          │   Structured Results    │
          │  Tabular Output / KPI   │
          └─────────────────────────┘
```

---

## 📂 Repository Structure

```
Database-SQL-generation-via-LLM/
│
├── Q1.py
├── Q2.py
├── Q3.py
├── Q4.py
├── Q5.py
│
├── course.csv
├── instructor.csv
├── team.csv
├── rating.csv
├── student.csv
├── and other relational CSV tables
│
└── README.pdf
```

---

## 📊 Example Analytical Questions Solved

| Script | Business Question                                        |
| ------ | -------------------------------------------------------- |
| Q1     | Which course has the highest enrollment?                 |
| Q2     | Which instructor teaches the most students?              |
| Q3     | Which instructor has the highest average rating?         |
| Q4     | List courses ranked by popularity                        |
| Q5     | What is the total compensation of a specific instructor? |

Each script:

• Loads relational CSV tables
• Executes SQL via DuckDB
• Prints structured results

---

## 🔍 Example Query Flow

### 🗣 Input Question:

> "Which instructor has the highest average rating?"

### 🤖 LLM-Generated SQL:

```sql
SELECT instructor_name, AVG(rating) AS avg_rating
FROM rating
GROUP BY instructor_name
ORDER BY avg_rating DESC
LIMIT 1;
```

### 📈 Output:

```
Instructor A | 4.92
```

---

## 🧩 Technical Stack

| Component            | Purpose                             |
| -------------------- | ----------------------------------- |
| 🐍 Python            | Query execution layer               |
| 🦆 DuckDB            | Fast analytical SQL engine          |
| 📁 CSV Tables        | Relational data source              |
| 🧠 LLM Reasoning     | Natural language to SQL translation |
| 📊 Structured Output | Tabular analytical results          |

---

## 💡 Why DuckDB?

DuckDB allows:

✔ Direct SQL execution on CSV files
✔ Zero database setup
✔ Fast analytical performance
✔ Embedded lightweight architecture

Perfect for rapid AI-data experimentation.

---

## 🔬 What This Project Demonstrates

### 🧠 LLM Skills

* Structured query generation
* Schema reasoning
* Deterministic SQL formatting
* Text-to-SQL transformation

### 📊 Data Skills

* Relational modeling
* Aggregation logic
* Joins and grouping
* Analytical query optimization

### 🏗 Engineering Skills

* Programmatic SQL execution
* Data pipeline thinking
* Reproducible experimentation
* Clean script modularization

---

## 📈 Practical Applications

This project simulates real-world systems such as:

• AI-powered BI assistants
• Natural language analytics tools
• AI database copilots
• Chat-based enterprise data querying
• LLM-augmented SQL IDEs

---

## 🛠 How to Run

```bash
git clone https://github.com/AtharvaThorat/Database-SQL-generation-via-LLM
cd Database-SQL-generation-via-LLM
pip install duckdb
python Q1.py
```

---

## 🚀 Future Enhancements

🔹 Integrate live LLM API (OpenAI / Ollama)
🔹 Add evaluation benchmark for SQL accuracy
🔹 Build Streamlit interface
🔹 Add schema-aware prompt engineering
🔹 Add hallucination detection layer

---

## 📌 Why This Project Stands Out

Recruiter Perspective:

This is not just SQL scripting.

It demonstrates:

✔ AI + Data integration
✔ Real LLM application
✔ Structured reasoning
✔ Analytical engineering mindset
✔ Practical implementation capability

This is the type of foundational system used in:

* AI copilots
* Enterprise data assistants
* Modern analytics platforms

---

## 👨‍💻 Author

**Atharva Thorat**
AI | ML | LLM Engineering | Applied Intelligence Systems

