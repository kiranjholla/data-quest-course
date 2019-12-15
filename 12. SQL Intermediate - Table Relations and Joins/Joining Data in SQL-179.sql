## 1. Introducing Joins ##

SELECT * FROM facts fc INNER JOIN cities ct ON fc.id = ct.facts_id LIMIT 10 

## 2. Understanding Inner Joins ##

SELECT ct.*, fc.name country_name FROM cities ct INNER JOIN facts fc ON ct.facts_id = fc.id LIMIT 5

## 3. Practicing Inner Joins ##

SELECT fc.name country, ct.name capital_city FROM facts fc INNER JOIN cities ct ON fc.id = ct.facts_id AND ct.capital = 1

## 4. Left Joins ##

SELECT fc.name country, fc.population FROM facts fc LEFT JOIN cities ct ON fc.id = ct.facts_id WHERE ct.id IS NULL

## 6. Finding the Most Populous Capital Cities ##

SELECT ct.name capital_city, fc.name country, ct.population FROM facts fc JOIN cities ct ON fc.id = ct.facts_id AND ct.capital = 1 ORDER BY ct.population DESC LIMIT 10

## 7. Combining Joins with Subqueries ##

  SELECT capital_city,
         fc.name country, 
         c.population 
    FROM facts fc INNER JOIN (SELECT ct.facts_id,
                                     ct.name capital_city, 
                                     population 
                                FROM cities ct 
                               WHERE ct.capital = 1 
                                 AND population > 10000000
                             ) c 
      ON fc.id = c.facts_id 
ORDER BY c.population DESC

## 8. Challenge: Complex Query with Joins and Subqueries ##

  SELECT fc.name country,
         up.urban_pop urban_pop,
         fc.population total_pop,
         CAST(up.urban_pop as float) / CAST(fc.population as float) urban_pct
    FROM facts fc INNER JOIN (SELECT ct.facts_id,
                                     SUM(ct.population) urban_pop
                                FROM cities ct
                            GROUP BY ct.facts_id) up
      ON up.facts_id = fc.id
   WHERE urban_pct > 0.5 
ORDER BY urban_pct ASC