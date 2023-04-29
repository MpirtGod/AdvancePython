SELECT customer.full_name AS customer_name, o.order_no
FROM "order" o
JOIN customer on customer.customer_id = o.customer_id
WHERE o.manager_id IS NULL;