## 2. Joining Three Tables ##

    SELECT tr.track_id,
           tr.name track_name,
           mt.name track_type,
           il.unit_price,
           il.quantity
      FROM invoice_line il 
INNER JOIN track tr ON il.track_id = tr.track_id
INNER JOIN media_type mt ON tr.media_type_id = mt.media_type_id
     WHERE il.invoice_id = 4 

## 3. Joining More Than Three Tables ##

    SELECT tr.track_id,
           tr.name track_name,
           ar.name artist_name,
           mt.name track_type,
           il.unit_price,
           il.quantity
      FROM invoice_line il 
INNER JOIN track tr ON il.track_id = tr.track_id
INNER JOIN media_type mt ON tr.media_type_id = mt.media_type_id
INNER JOIN album al ON tr.album_id = al.album_id
INNER JOIN artist ar ON al.artist_id = ar.artist_id
     WHERE il.invoice_id = 4 

## 4. Combining Multiple Joins with Subqueries ##

    SELECT al.title album,
           ar.name artist,
           COUNT(tr.track_id) tracks_purchased
      FROM invoice_line il 
INNER JOIN track tr ON il.track_id = tr.track_id
INNER JOIN album al ON tr.album_id = al.album_id
INNER JOIN artist ar ON al.artist_id = ar.artist_id
  GROUP BY al.title
  ORDER BY tracks_purchased DESC
     LIMIT 5

## 5. Recursive Joins ##

    SELECT emp.first_name || " " || emp.last_name employee_name,
           emp.title employee_title,
           sup.first_name || " " || sup.last_name supervisor_name,
           sup.title supervisor_title
      FROM employee emp
 LEFT JOIN employee sup ON emp.reports_to = sup.employee_id
  ORDER BY employee_name

## 6. Pattern Matching Using Like ##

SELECT first_name, last_name, phone FROM customer WHERE first_name LIKE "%Belle%"

## 7. Generating Columns With The Case Statement ##

    SELECT cus.first_name || " " || cus.last_name customer_name,
           COUNT(inv.invoice_id) number_of_purchases,
           SUM(inv.total) total_spent,
           CASE 
               WHEN SUM(inv.total) < 40 THEN "small spender"
               WHEN SUM(inv.total) > 100 THEN "big spender"
               ELSE "regular"
               END AS customer_category
      FROM invoice inv
INNER JOIN customer cus ON cus.customer_id = inv.customer_id
  GROUP BY 1
  ORDER BY 1
