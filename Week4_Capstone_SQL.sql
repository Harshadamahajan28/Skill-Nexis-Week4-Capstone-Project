-- Week 4 SQL Analysis
SELECT category, SUM(total_price) AS total_sales
FROM orders GROUP BY category ORDER BY total_sales DESC;

SELECT year, SUM(total_price) AS total_sales
FROM orders GROUP BY year ORDER BY year;

SELECT customer_name, SUM(total_price) AS total_sales
FROM orders GROUP BY customer_name ORDER BY total_sales DESC LIMIT 10;

SELECT region, SUM(total_price) AS total_sales
FROM orders GROUP BY region ORDER BY total_sales DESC;

SELECT AVG(total_price) AS average_order_line_value FROM orders;
