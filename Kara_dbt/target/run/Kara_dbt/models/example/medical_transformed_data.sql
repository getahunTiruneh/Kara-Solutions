
  
    

  create  table "postgres"."public"."medical_transformed_data__dbt_tmp"
  
  
    as
  
  (
    -- Use the `ref` function to select from other models



with filterd_data as (
    select * from "postgres"."public"."telegram_data"
    
)

select 
    message_id,
    date,
    sender,
    channel,
    text    
from filterd_data
  );
  