Chicago Food Inspections (SQL)

I cleaned real City of Chicago food inspection data and used SQL to answer a few questions about it.

Data: [Food Inspections, City of Chicago Data Portal](https://data.cityofchicago.org/resource/4ijn-s7e5)


`get_inspections.py` downloads the data
`clean_inspections.py` cleans it and saves it in a SQLite database
`questions.sql` has 5 queries, and `run_questions.py` runs them

 Cleaning I did
- removed duplicate rows
- made the city spelling the same everywhere
- fixed zip codes that ended in ".0" and marked the missing ones
- cut the dates down to just the day
- turned the risk text into a number

 How to run
```
pip install pandas
python get_inspections.py
python clean_inspections.py
python run_questions.py
```

Questions
1. How many inspections got each result?
2. Which zip codes have the most failed inspections?
3. Which zip codes fail the highest percent of the time?
4. Which facility types fail the most?
5. Do high-risk places fail more than low-risk places?

 What I found:
 
Schools seemed to have failed the most inspections (23.6%) though there are more school inspections (3,051) than in the other high-fail types like liquor (225). I wonder how it would change with different data pulled in the future.
Liquor establishments failed more often (21.3%) than bakeries (18.6%), though there were far fewer liquor inspections (225 vs. 706), so that rate is less reliable. Shared Kitchen User (Long Term) have one of the lowest failed rates at 4.1% while (Long Term) care facilities are very high at 22.4%. 

Raw Output:

<img width="327" height="281" alt="image" src="https://github.com/user-attachments/assets/c96765b6-de0a-4eb7-a504-21d3120ee7b7" />
<img width="588" height="460" alt="image" src="https://github.com/user-attachments/assets/2b6ff90d-f530-4f65-b579-f77005fe910f" />

Output visualization: 

<img width="766" height="487" alt="image" src="https://github.com/user-attachments/assets/020e47e1-1ff3-45df-84fc-0075ef3a4eee" />

 What I'd do next
- look at how results change over time
- compare the fail rates by neighborhood
- compare the rates properly with how many inspections being consistent

