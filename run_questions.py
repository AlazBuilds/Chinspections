# runs each query in questions.sql and prints the answers
import sqlite3
import pandas as pd

con = sqlite3.connect("inspections.db")

text = open("questions.sql").read()
queries = text.split(";")

n = 1
for q in queries:
    if "SELECT" not in q:
        continue
    print("---- Q" + str(n) + " ----")
    print(pd.read_sql(q, con).to_string(index=False))
    print()
    n = n + 1

con.close()
