------------------------------------------------------------------------------------------------------------------------------
-- WINDOW FUNCTIONS
------------------------------------------------------------------------------------------------------------------------------

-- WINDOW FUNCTION

select
  *,
  sum(sales_cost) over (partition by transaction_id) as transaction_total_sales,
  sales_cost / sum(sales_cost) over (partition by transaction_id) as transaction_sales_percent
  
from
  grocery_db.transactions;

-- ROW NUMBER & RANK

select
  *,
  row_number() over (partition by customer_id order by transaction_date, transaction_id) as transaction_number
  
from
  grocery_db.transactions;


-- REFERENCE

/*
ROW NUMBER
will give a unique value to each row of data in the set *even* if there are ties in the order by logic


100m time   output
  10s         1       
  10s         2
  10s         3
  11s         4
  12s         5

RANK 
will give ties the same value, then skip to the next value in terms of the number of rows it has seen

100m time   output
  10s         1       
  10s         1
  10s         1
  11s         4
  12s         5

DENSE_RANK 
will do the same as RANK, but will go to the next number in sequence after any ties

100m time   output
  10s         1       
  10s         1
  10s         1
  11s         2
  12s         3
*/

-- NTILE - for deciles/percentiles etc

select
  customer_id,
  customer_loyalty_score,
  ntile(3) over (order by customer_loyalty_score desc) as loyalty_category,
  ntile(10) over (order by customer_loyalty_score desc) as loyalty_category2
  
from
  grocery_db.loyalty_scores;












