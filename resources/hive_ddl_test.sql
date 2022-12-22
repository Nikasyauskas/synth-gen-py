create table `custom_rozn_producshelf.ft_test` (
	`epk_id` bigint,
	`channel_id` int,
	row_update_time timestamp,
	`row_actual_from` string
)
partitioned by (`row_actual_to` string)
ROW FORMAT SERDE 'parquet.hive.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 'parquet.hive.DeprecatedParquetInputFormat'
OUTPUTFORMAT 'parquet.hive.DeprecatedParquetOutputFormat';