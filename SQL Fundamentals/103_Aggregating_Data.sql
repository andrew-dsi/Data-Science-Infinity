------------------------------------------------------------------------------------------------------------------------------
-- AGGREGATION OUR DATA
------------------------------------------------------------------------------------------------------------------------------

-- AGGREGATION FUNCTIONS

select
  sum(sales_cost) as total_sales,
  avg(sales_cost) as avg_sales,
  min(sales_cost) as min_sales,
  max(sales_cost) as max_sales,
  count(*) as num_rows,
  count (distinct transaction_id) as num_transactions
  
from
  grocery_db.transactions;

-- THE GROUP BY STATEMENT

select
  transaction_date,
  sum(sales_cost) as total_sales,
  sum(num_items) as total_items,
  count (distinct transaction_id) as num_transactions
  
from
  grocery_db.transactions
  
group by
  transaction_date
  
order by
  transaction_date;
  

-- GROUPING MY MULTIPLE VARIABLES

select
  product_area_id,
  transaction_date,
  sum(sales_cost) as total_sales,
  sum(num_items) as total_items,
  count (distinct transaction_id) as num_transactions
  
from
  grocery_db.transactions
  
group by
  product_area_id,
  transaction_date
  
order by
  product_area_id,
  transaction_date;


-- THE HAVING CLAUSE

select
  product_area_id,
  sum(sales_cost) as total_sales
  
from
  grocery_db.transactions
  
group by
  product_area_id
  
having
  sum(sales_cost) > 200000;













