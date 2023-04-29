SELECT customer.full_name AS customer_name, manager.full_name AS manager_name, o.purchase_amount, o.date
FROM "order" o
JOIN customer ON o.customer_id = customer.customer_id
LEFT JOIN manager ON o.manager_id = manager.manager_id OR manager.manager_id IS NULL;