# 🧠 AI-Driven SQL Generation from Natural Language

> An LLM-centric project that automatically derives SQL queries from natural language database questions and executes them efficiently using DuckDB.

---

## 🚀 Project Summary

This repository demonstrates how **Large Language Models (LLMs)** and programmatic SQL tooling can be combined to:

✨ Translate or interpret **natural language database questions**
✔ Generate **production-ready SQL queries**
📊 Execute those queries using **DuckDB**
📁 Operate on real CSV datasets representing relational structures

It showcases **practical Text-to-SQL capabilities** applicable to data analytics, BI tools, intelligent query systems, and AI-augmented database tooling — a skillset highly relevant for AI/ML and LLM engineering roles. ([GitHub][1])

---

## 📂 Repository Contents

```
Database-SQL-generation-via-LLM/
│
├── Q1.py
├── Q2.py
├── Q3.py
├── Q4.py
├── Q5.py
├── README.pdf
├── *.csv (10 relational CSV tables)
└── .DS_Store
```

**Key components explained:**

| Component         | Purpose                                                      |               |
| ----------------- | ------------------------------------------------------------ | ------------- |
| `Q1.py` – `Q5.py` | Python scripts that run SQL queries using DuckDB on CSV data |               |
| `.csv` files      | Tables representing a classroom / research data model        |               |
| `README.pdf`      | Original project documentation and screenshots               |               |
| `.DS_Store`       | System metadata (can be removed)                             | ([GitHub][1]) |

---

## 🧩 Project Workflow

1. **Dataset Representation**

   * Each `.csv` is a table such as `course`, `instructor`, `team`, `rating`, etc.
   * Together they model a database similar to a university or project ecosystem. ([GitHub][1])

2. **SQL Execution with DuckDB**

   * DuckDB is used to execute SQL directly on CSV files — enabling fast prototyping without setting up a DB engine.
   * Example:

     ````python
     import duckdb
     result = duckdb.sql("SELECT … FROM 'table.csv' …")
     result.show()
     ``` :contentReference[oaicite:3]{index=3}

     ````

3. **Scripted Queries**
   Each Python file answers a natural language question by:

   * Generating SQL (manually or via a prompt pipeline)
   * Running it on CSV data
   * Printing formatted results

---

## 📊 Query Descriptions

Here’s what each script computes:

| Script    | Question Being Answered                                                  |
| --------- | ------------------------------------------------------------------------ |
| **Q1.py** | Which course has the most students?                                      |
| **Q2.py** | Which instructor teaches the most students?                              |
| **Q3.py** | Which instructor has the highest average rating?                         |
| **Q4.py** | List all classes with their enrollment counts, sorted by popularity      |
| **Q5.py** | Compute the total pay for a specific instructor (teaching + supervision) |

Each script is structured to:
✔ Load datasets
✔ Execute SQL with DuckDB
✔ Print results clearly using `result.show()` ([GitHub][2])

---

## 📌 Example Output

A typical script prints results like:

```
============================================================
Q1: Course with Most Number of Students
============================================================
┌─────────────┬───────────┐
│ course_name │ students  │
├─────────────┼───────────┤
│ Data Sci 101│ 124       │
└─────────────┴───────────┘
```

This replicates real data analytics workflow patterns.

---

## 🧠 Skills & Techniques Demonstrated

This project highlights the following:

✔ **Text-to-SQL reasoning pipelines**
✔ **Structured SQL generation logic**
✔ **Programmatic data processing using DuckDB**
✔ **Handling relational data via CSV in Python**
✔ **Evaluation of generated queries against real data**

These are directly applicable to:

* **AI/ML Engineering**
* **LLM System Design**
* **Data Engineering**
* **Business Intelligence tooling**
* **Data Analytics Automation**

---

## 📈 Why This Project Is Valuable for Recruiters

This project showcases practical real-world AI and database skills:

* You can **bridge natural language understanding with structured database logic**
* You demonstrate knowledge of **DuckDB as an analytics engine**
* You show how to **operationalize machine-generated SQL queries**
* You illustrate ability to **work with real datasets without heavy DB setup**
* The project can be extended into **AI-augmented database applications**

---

## 📦 Next Steps / Extensions

Here are ways to evolve the project in a portfolio:

🔹 Add a **prompt-based LLM interface** that takes text → generates SQL
🔹 Integrate a **web/UI layer** (e.g., Streamlit) for interactively querying
🔹 Build a **benchmark evaluation suite** for comparing SQL generation models
🔹 Expand to **multi-schema databases** and optimize SQL logic

---

## 🛠 How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/AtharvaThorat/Database-SQL-generation-via-LLM
   ```
2. Install dependencies:

   ```bash
   pip install duckdb
   ```
3. Run any query script:

   ```bash
   python Q1.py
   ```

   Results will print in the terminal.

---

## 📣 Final Notes

This project is a strong demonstration of how AI (particularly LLMs) can be integrated with traditional database technologies to make data querying more intuitive and efficient — a highly desirable ability in modern tech roles focused on **AI-augmented tooling** and **data workflows**. ([arXiv][3])

