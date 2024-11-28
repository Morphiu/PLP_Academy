-- Query for total spent per category
SELECT SUM(amount), category FROM expenses
GROUP BY category;

-- Query for average expense per category
SELECT AVG(amount), category FROM expenses
GROUP BY category;

-- Query for top 3 spending categories
SELECT AVG(amount), category FROM expenses
GROUP BY category
ORDER BY AVG(amount) DESC LIMIT 3;
