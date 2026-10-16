# cleans inspections_raw.csv and puts it in a sqlite database
import sqlite3
import pandas as pd

df = pd.read_csv("inspections_raw.csv", dtype=str)
print("rows at start:", len(df))

# remove duplicates
df = df.drop_duplicates()
df = df.drop_duplicates(subset="inspection_id")
print("rows after removing duplicates:", len(df))

# city has different spellings so make them all the same
df["city"] = df["city"].str.upper().str.strip()
df["city"] = df["city"].replace("CHICAGOCHICAGO", "CHICAGO")
df["city"] = df["city"].fillna("CHICAGO")

# facility type
df["facility_type"] = df["facility_type"].str.title()
df["facility_type"] = df["facility_type"].fillna("Unknown")

# zip codes sometimes end in .0
df["zip"] = df["zip"].str.replace(".0", "", regex=False)
print("rows with no zip:", df["zip"].isna().sum())

# fix the date (cut off the time part)
df["inspection_date"] = df["inspection_date"].str[:10]

# risk -> just the number
df["risk_level"] = df["risk"].str[5]

df = df[["inspection_id", "dba_name", "facility_type", "risk_level",
         "city", "zip", "inspection_date", "results"]]

con = sqlite3.connect("inspections.db")
df.to_sql("inspections", con, if_exists="replace", index=False)
con.close()
print("saved", len(df), "rows to inspections.db")
