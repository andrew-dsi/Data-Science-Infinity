------------------------------------------------------------------------------------------------------------------------------
-- TEMP TABLES & CTE FOR MULTIPLE QUERIES
------------------------------------------------------------------------------------------------------------------------------

select * from grocery_db.transactions where customer_id = 1;

--  TEMPORARY TABLES

create temp table cust_transactions as (
select
  customer_id,
  transaction_id,
  sum(sales_cost) as total_sales
  
from
  grocery_db.transactions
  
group by
  customer_id,
  transaction_id

);

select * from cust_transactions;

select
  customer_id,
  avg(total_sales) as avg_transaction_sales
  
from
  cust_transactions
  
group by
  customer_id;

-- COMMON TABLE EXPRESSION (CTE)

with cust_transactions_cte as (
select
  customer_id,
  transaction_id,
  sum(sales_cost) as total_sales
  
from
  grocery_db.transactions
  
group by
  customer_id,
  transaction_id

),

cust_sales_cte as (
select
  customer_id,
  avg(total_sales) as avg_transaction_sales
  
from
  cust_transactions_cte
  
group by
  customer_id
  
)

select max(avg_transaction_sales) as max_avg_sales from cust_sales_cte;
;





















