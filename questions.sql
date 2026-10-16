-- Q1: how many inspections for each result?
SELECT results, COUNT(*) AS total
FROM inspections
GROUP BY results
ORDER BY total DESC;

-- Q2: which zip codes have the most failed inspections?
SELECT zip, COUNT(*) AS fails
FROM inspections
WHERE results = 'Fail' AND zip IS NOT NULL
GROUP BY zip
ORDER BY fails DESC
LIMIT 10;

-- Q3: what percent of inspections fail in each zip code? (only zips with 50+ inspections)
SELECT zip,
       COUNT(*) AS total,
       ROUND(100.0 * SUM(CASE WHEN results = 'Fail' THEN 1 ELSE 0 END) / COUNT(*), 1) AS fail_percent
FROM inspections
WHERE zip IS NOT NULL
GROUP BY zip
HAVING COUNT(*) >= 50
ORDER BY fail_percent DESC
LIMIT 10;

-- Q4: which facility types fail the most?
SELECT facility_type,
       COUNT(*) AS total,
       ROUND(100.0 * SUM(CASE WHEN results = 'Fail' THEN 1 ELSE 0 END) / COUNT(*), 1) AS fail_percent
FROM inspections
GROUP BY facility_type
HAVING COUNT(*) >= 50
ORDER BY fail_percent DESC;

-- Q5: do high risk places fail more than low risk places?
SELECT risk_level,
       COUNT(*) AS total,
       ROUND(100.0 * SUM(CASE WHEN results = 'Fail' THEN 1 ELSE 0 END) / COUNT(*), 1) AS fail_percent
FROM inspections
WHERE risk_level IS NOT NULL
GROUP BY risk_level
ORDER BY risk_level;
