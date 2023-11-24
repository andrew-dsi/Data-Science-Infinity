------------------------------------------------------------------------------------------------------------------------------
-- THE BASIC SELECT STATEMENT
------------------------------------------------------------------------------------------------------------------------------

-- THE SELECT STATEMENT

select 
  * 
  
from
  grocery_db.product_areas;

-- LIMIT

select 
  * 
  
from
  grocery_db.product_areas
  
limit
  3;

-- ORDER BY

select 
  * 
  
from
  grocery_db.customer_details
  
order by
  distance_from_store,
  credit_score;

-- DISTINCT

select
  distinct 
  * 
  
from
  grocery_db.customer_details;
  
select
  distinct 
  gender 
  
from
  grocery_db.customer_details;
  
-- GIVING COLUMNS AN ALIAS

select
  distance_from_store as distance_to_store,
  customer_id as customer_number
  
from
  grocery_db.customer_details;
  

-- CREATING NEW COLUMNS

select
  distance_from_store as distance_to_store,
  customer_id as customer_number,
  1 as new_col,
  distance_from_store * 1.6 as distance_from_store_km
  
from
  grocery_db.customer_details;


  











