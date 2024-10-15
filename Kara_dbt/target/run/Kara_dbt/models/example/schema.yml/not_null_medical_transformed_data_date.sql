select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select date
from "postgres"."public"."medical_transformed_data"
where date is null



      
    ) dbt_internal_test