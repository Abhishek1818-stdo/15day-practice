#Create customers, products, orders, and order_items with primary/foreign keys and UNIQUE, NOT NULL, CHECK, and DEFAULT constraints.
#Task 1



CREATE TABLE customers (
    customer_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE products (
    product_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_name TEXT NOT NULL,
    price NUMERIC(12, 2) NOT NULL CHECK (price >= 0)
);

CREATE TABLE orders (
    order_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id BIGINT NOT NULL REFERENCES customers(customer_id),
    order_date TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    status TEXT NOT NULL DEFAULT 'NEW'
);

CREATE TABLE order_items (
    order_id BIGINT NOT NULL REFERENCES orders(order_id),
    product_id BIGINT NOT NULL REFERENCES products(product_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(12, 2) NOT NULL CHECK (unit_price >= 0),
    PRIMARY KEY (order_id, product_id)
);


#Task 2 — Filtering, sorting, and pagination

SELECT order_id, customer_id, order_date, status
FROM orders
WHERE status = 'NEW'
order by order_date DESC, order_id DESC
limit 10
offset 0;


#Task 3 — Joins and customers with no orders

SELECT
    c.customer_id,c.full_name, o.order_id,o.order_date
from customers AS c
left join orders AS o
   on o.customer_id = c.customer_id
order by c.customer_id;

#customers with no orders using not exist
SELECT c.customer_id, c.full_name
from customers AS c
where not exists (
select 1
 from orders AS o
where o.customer_id = c.customer_id
);


#TASK 4 Aggregation and analytics

SELECT
    c.customer_id,
    c.full_name,
   count(o.order_id) AS order_count
FROM customers AS c
left join orders AS o
ON o.customer_id = c.customer_id
group by c.customer_id, c.full_name
order by order_count desc, c.customer_id;


#customers with atleast 2 orders

SELECT
    c.customer_id,
    c.full_name,
    COUNT(o.order_id) AS order_count
from customers AS c
join orders AS o
    on o.customer_id = c.customer_id
group by c.customer_id, c.full_name
having count(o.order_id) >= 2
order by order_count desc;


#task 5  Cte 

WITH customer_totals AS (
    SELECT customer_id, SUM(amount) AS total_spend
FROM orders
 group by customer_id
)
SELECT customer_id, total_spend
from customer_totals
order by total_spend DESC;


#task 6 window function

WITH ranked_orders AS (
    SELECT
    order_id,customer_id,order_date,status,
        row_number() OVER (
        partition by customer_id
         order by order_date DESC, order_id DESC
        ) AS rn
    FROM orders
)
SELECT order_id, customer_id, order_date, status
FROM ranked_orders
where  rn = 1
order by customer_id;

