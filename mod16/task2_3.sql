SELECT o.order_no, customer.full_name AS customer_name, manager.full_name AS manager_name
FROM "order" o
JOIN customer ON o.customer_id = customer.customer_id
JOIN manager ON manager.manager_id = o.manager_id
WHERE customer.city != manager.city;