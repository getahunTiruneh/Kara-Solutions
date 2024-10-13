

with filtered_data as (
    select 
        image_name,
        confidence_score,
        class_name,
        bbox_coordinates,
        result_image_path,
        detection_time
    from "postgres"."public"."detection_results"
)

select 
    image_name,
    confidence_score,
    class_name,
    -- Access the array elements directly
    bbox_coordinates[1] as bbox_xmin,  -- First element renamed
    bbox_coordinates[2] as bbox_ymin,  -- Second element renamed
    bbox_coordinates[3] as bbox_xmax,  -- Third element renamed
    bbox_coordinates[4] as bbox_ymax,   -- Fourth element renamed
    result_image_path,
    detection_time
from filtered_data