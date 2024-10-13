
  
    

  create  table "postgres"."public"."medical_data__dbt_tmp"
  
  
    as
  
  (
    

select * 
from public.telegram_data
  );
  