# gets the chicago food inspections data and saves it as inspections_raw.csv
#
# python get_inspections.py            -> downloads the REAL data from the city
# python get_inspections.py fake       -> makes FAKE practice data (no internet needed)
import sys
import random
import pandas as pd

url = "https://data.cityofchicago.org/resource/4ijn-s7e5.csv?$limit=50000"

if len(sys.argv) > 1 and sys.argv[1] == "fake":
    # fake data, same columns as the real data. NOT real results!
    random.seed(5)
    zips = ["60601", "60608", "60609", "60614", "60619", "60622", "60629", "60647"]
    types = ["Restaurant", "restaurant", "Grocery Store", "School", "Bakery", "Tavern"]
    results = ["Pass", "Pass", "Pass", "Fail", "Pass w/ Conditions", "No Entry"]
    cities = ["CHICAGO", "Chicago", "chicago", "CHICAGOCHICAGO", None]

    rows = []
    for i in range(5000):
        row = {}
        row["inspection_id"] = 100000 + i
        row["dba_name"] = "PLACE " + str(random.randint(1, 300))
        row["facility_type"] = random.choice(types)
        row["risk"] = random.choice(["Risk 1 (High)", "Risk 2 (Medium)", "Risk 3 (Low)"])
        row["city"] = random.choice(cities)
        z = random.choice(zips)
        if random.random() < 0.05:
            z = None
        elif random.random() < 0.05:
            z = z + ".0"
        row["zip"] = z
        row["inspection_date"] = "202" + str(random.randint(2, 5)) + "-0" + str(random.randint(1, 9)) + "-10T00:00:00.000"
        row["results"] = random.choice(results)
        rows.append(row)

    df = pd.DataFrame(rows)
    df = pd.concat([df, df.head(40)])  # a few duplicate rows
    print("made FAKE data:", len(df), "rows. dont use these results for real conclusions")
else:
    df = pd.read_csv(url, dtype=str)
    print("downloaded REAL data:", len(df), "rows")

df.to_csv("inspections_raw.csv", index=False)
