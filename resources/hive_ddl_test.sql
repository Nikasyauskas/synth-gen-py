CREATE TABLE IF NOT EXISTS test_schema0.test_table0 (
 epk_id int,
 name string,
 row_update_time timestamp,
 row_actual_from date )
PARTITIONED BY (row_actual_to string)
STORED AS PARQUET
;

CREATE TABLE IF NOT EXISTS test_schema1.test_table1 (
 epk_id int,
 name string,
 cash_amnt float)
PARTITIONED BY (row_actual_to_date string)
STORED AS PARQUET
;

CREATE TABLE IF NOT EXISTS test_schema2.test_table2 (
 epk_id int,
 test_field1 string,
 test_field2 date,
 test_field3 timestamp
 row_update_time timestamp,
 row_actual_from date )
PARTITIONED BY (row_actual_to string)
STORED AS PARQUET
;

