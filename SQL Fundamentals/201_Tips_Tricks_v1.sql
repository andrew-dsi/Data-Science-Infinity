------------------------------------------------------------------------------------------------------------------------------
-- USEFUL TIPS & TRICKS (VOLUME 1)
------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------
-- Using Sub-Queries
----------------------------------------------------------------

select
  product_area_name,
  profit_margin
  
from
  grocery_db.product_areas
  
where
  --profit_margin = (select max(profit_margin) from grocery_db.product_areas)
  profit_margin = (select profit_margin from grocery_db.product_areas order by profit_margin desc limit 1);

--------------------------------------------------------------------------------
-- Using Lead & Lag
--------------------------------------------------------------------------------

create temp table cust_trans as (
select
  distinct
  customer_id,
  transaction_id,
  transaction_date
  
from
  grocery_db.transactions
  
where
  customer_id in (1,2)
  
);

select
  *,
  lag(transaction_date,1) over (partition by customer_id order by transaction_date, transaction_id) as transaction_date_lag1,
  lag(transaction_date,2) over (partition by customer_id order by transaction_date, transaction_id) as transaction_date_lag2,
  lead(transaction_date,1) over (partition by customer_id order by transaction_date, transaction_id) as transaction_date_lead1
  
from
  cust_trans;

--------------------------------------------------------------------------------
-- Rounding Data
--------------------------------------------------------------------------------

select
  *,
  round(sales_cost,1) as sales_cost_round1,
  round(sales_cost,0) as sales_cost_round0
  
from
  grocery_db.transactions
  
where
  customer_id = 1;

--------------------------------------------------------------------------------
-- Random Sampling
--------------------------------------------------------------------------------

select
  *
  
from
  grocery_db.customer_details
  
order by
  random()
  
limit
  100;

--------------------------------------------------------------------------------
-- Extracting parts of a date
--------------------------------------------------------------------------------

select
  distinct
  transaction_date,
  date_part('day',transaction_date) as day,
  date_part('month',transaction_date) as month,
  date_part('year',transaction_date) as year,
  date_part('dow',transaction_date) as dow
  
from
  grocery_db.transactions
  
order by
  transaction_date;

--------------------------------------------------------------------------------
-- Working with Strings/Text
--------------------------------------------------------------------------------

select
  product_area_name,
  upper(product_area_name) as pan_upper,
  lower(product_area_name) as pan_lower,
  char_length(product_area_name) as pan_length,
  concat(product_area_name, ' - ', 'Department') as pan_concat,
  substring(product_area_name,3,6) as pan_substring,
  repeat(product_area_name,2) as pan_repeat
  
from
  grocery_db.product_areas;

















