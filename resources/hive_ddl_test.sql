CREATE TABLE IF NOT EXISTS test_schema.test_table (
 epk_id int,
 name string,
 row_update_time timestamp,
 row_actual_from date )
PARTITIONED BY (row_actual_to string)
STORED AS PARQUET
;
