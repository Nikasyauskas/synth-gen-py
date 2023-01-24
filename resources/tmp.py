from simple_ddl_parser import parse_from_file
from pyspark.sql import SparkSession
from ddl import DDLContainer

parse_results = parse_from_file('resources/hive_ddl_test.sql')
ddlContainer = DDLContainer(parse_results[0])
print(ddlContainer)

spark = SparkSession.builder.getOrCreate()
emptyRDD = spark.sparkContext.emptyRDD()
df = spark.createDataFrame(emptyRDD, ddlContainer.getSchemaDf())
df.write.parquet("resources/parquet_storage", "overwrite")
df2 = spark.read.parquet("resources/parquet_storage")
df2.show()