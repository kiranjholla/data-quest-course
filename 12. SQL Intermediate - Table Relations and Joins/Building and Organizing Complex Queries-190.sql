## 3. The With Clause ##

WITH playlist_tracks AS
    (SELECT pl.playlist_id,
            pl.name playlist_name,
            tr.name track_name,
            tr.milliseconds / 1000 track_seconds
       FROM playlist pl
  LEFT JOIN playlist_track pt ON pl.playlist_id = pt.playlist_id
  LEFT JOIN track tr ON tr.track_id = pt.track_id)
  SELECT playlist_id,
         playlist_name,
         COUNT(track_name) number_of_tracks,
         SUM(track_seconds) length_seconds
    FROM playlist_tracks
GROUP BY playlist_id
ORDER BY playlist_id

## 4. Creating Views ##

CREATE VIEW chinook.customer_gt_90_dollars AS
    SELECT cus.*
      FROM customer cus
INNER JOIN invoice inv ON cus.customer_id = inv.customer_id
  GROUP BY cus.customer_id
    HAVING SUM(inv.total) > 90;
    

SELECT * FROM chinook.customer_gt_90_dollars


## 5. Combining Rows With Union ##

SELECT * FROM customer_usa
UNION
SELECT * FROM customer_gt_90_dollars

## 6. Combining Rows Using Intersect and Except ##

    SELECT emp.first_name || " " || emp.last_name employee_name,
           COUNT(cusa90.customer_id) customers_usa_gt_90
      FROM employee emp
 LEFT JOIN (SELECT * FROM customer_usa
            INTERSECT
            SELECT * FROM customer_gt_90_dollars
            ) cusa90 ON emp.employee_id = cusa90.support_rep_id
WHERE emp.title = "Sales Support Agent"
GROUP BY employee_name

## 7. Multiple Named Subqueries ##

WITH customers_india AS (SELECT *
           FROM customer
          WHERE country = 'India'
        ),
        
    customer_totals AS
        (SELECT inv.customer_id,
                SUM(inv.total) total_purchases
           FROM invoice inv
       GROUP BY inv.customer_id
        )
        
    SELECT cind.first_name || " " || cind.last_name customer_name,
           ctl.total_purchases
      FROM customers_india cind
LEFT JOIN customer_totals ctl ON cind.customer_id = ctl.customer_id
  ORDER BY customer_name

## 8. Challenge: Each Country's Best Customer ##

WITH 
    customer_purchases AS
        (
            SELECT cus.customer_id,
                   cus.first_name || " " || cus.last_name customer_name,
                   cus.country,
                   SUM(inv.total) total_purchased
              FROM customer cus
         LEFT JOIN invoice inv ON cus.customer_id = inv.customer_id
          GROUP BY cus.customer_id
        ),
        
    max_purchases AS
        (
            SELECT country,
                   MAX(total_purchased) max_purchase
              FROM customer_purchases cp
          GROUP BY country
        )
    SELECT cp.country, 
           cp.customer_name, 
           cp.total_purchased 
      FROM customer_purchases cp
INNER JOIN max_purchases mp ON cp.country = mp.country AND cp.total_purchased = mp.max_purchase
  ORDER BY cp.country