
-- Use the `ref` function to select from other models

{{config(materialized = "table")}}

with filterd_data as (
    select * from {{source('public','telegram_data')}}
    
)

select 
    message_id,
    date,
    sender,
    channel,
    text    
from filterd_data
