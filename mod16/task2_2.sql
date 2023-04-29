SELECT customer.full_name
FROM customer
LEFT JOIN "order" o ON o.customer_id = customer.customer_id
WHERE o.order_no IS NULL;