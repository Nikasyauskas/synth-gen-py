from typing import (
    Dict,
    List,
)
from pyspark.sql.types import (
    StructType,
    StringType,
    IntegerType,
    TimestampType,
    DateType
)
class DDLContainer:


    def __init__(self, parse_result: List[Dict]):
        self.schema = parse_result["schema"]
        self.table = parse_result["table_name"]
        self.columns = self.__extract_colums(parse_result)
        self.types = self.__extract_types(parse_result)
        self.nullable = self.__extract_nullable(parse_result)
        self.table_size = len(self.columns)
        self.schema_df = self.__constract_schema()


    def __extract_colums(self, ddl_metadata: List[Dict]):
        columns_list = []
        for elem in ddl_metadata["columns"]:
            columns_list.append(elem["name"])
        return columns_list


    def __extract_types(self, ddl_metadata: List[Dict]):
        types_list = []
        for elem in ddl_metadata["columns"]:
            types_list.append(self.__cast_hive_to_spark_type(elem["type"]))
        return types_list


    def __extract_nullable(self, ddl_metadata: List[Dict]):
        nullable_list = []
        for elem in ddl_metadata["columns"]:
            nullable_list.append(elem["nullable"])
        return nullable_list


    def __cast_hive_to_spark_type(self, data_type): #: str
        data_type_lower = data_type.lower()
        match data_type_lower:
            case "int": # add "or integer" construction
                return IntegerType()
            case "string":
                return StringType()
            case "timestamp":
                return TimestampType()
            case "date":
                return DateType()
            case _:
                return "not correct"


    def __constract_schema(self):
        schema = StructType()
        for col, type, nullable in zip(self.columns, self.types, self.nullable):
            schema.add(col, type, nullable)
        return schema


    def getSchema(self):
        return self.schema


    def getTable(self):
        return self.table


    def getColumns(self):
        return self.columns


    def getSchemaDf(self):
        return self.schema_df

    def __repr__(self):
        return f"""
            {self.schema}
            {self.table}
            {self.columns}
            {self.types}
            {self.nullable}
            {self.table_size}
            {self.schema_df}"""
