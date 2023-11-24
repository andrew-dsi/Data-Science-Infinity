------------------------------------------------------------------------------------------------------------------------------
-- PART 2: APPLYING SELECTION CONDITIONS USING THE WHERE STATEMENT
------------------------------------------------------------------------------------------------------------------------------

-- THE WHERE STATEMENT

select
  *
  
from
  grocery_db.customer_details
  
where
  distance_from_store < 2;

-- MULTIPLE CONDITIONS

-- and

select
  *
  
from
  grocery_db.customer_details
  
where
  distance_from_store < 2 and
  gender = 'M';

-- or

select
  *
  
from
  grocery_db.customer_details
  
where
  distance_from_store < 2 or
  gender = 'M';

-- OTHER OPERATORS

/*
Equal to =
Not equal to <>
Greater than/Less than/Equal < > <=
*/

select
  *
  
from
  grocery_db.campaign_data;

-- in

select
  *
  
from
  grocery_db.campaign_data
  
where
  mailer_type in ('Mailer1','Mailer2');

-- like

select
  *
  
from
  grocery_db.campaign_data
  
where
  mailer_type like 'Mailer%';









