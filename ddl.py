from typing import (
    Dict,
    List,
)
from pyspark.sql.types import (
    StringType,
    IntegerType,
    TimestampType,
    FloatType,
    DateType
)


class TableContainer:
    def __init__(self, ddl_metadata: Dict):
        self.schema = ddl_metadata["schema"]
        self.table = ddl_metadata["table_name"]
        self.columns = self.__extract_colums(ddl_metadata)
        self.types = self.__extract_types(ddl_metadata)
        self.nullables = self.__extract_nullable(ddl_metadata)
        self.table_size = len(self.columns)

    def __extract_colums(self, ddl_metadata: Dict):
        columns_list = []
        for elem in ddl_metadata["columns"]:
            columns_list.append(elem["name"])
        return columns_list

    def __extract_types(self, ddl_metadata: Dict):
        types_list = []
        for elem in ddl_metadata["columns"]:
            types_list.append(self.__cast_hive_to_spark_type(elem["type"]))
        return types_list

    def __extract_nullable(self, ddl_metadata: Dict):
        nullable_list = []
        for elem in ddl_metadata["columns"]:
            nullable_list.append(elem["nullable"])
        return nullable_list

    def __cast_hive_to_spark_type(self, data_type):
        # TODO function - ddl.py -> DDLContainer -> __cast_hive_to_spark_type() not cover all type
        data_type_lower = data_type.lower()
        match data_type_lower:
            case "int":  # add "or integer" construction
                return IntegerType()
            case "string":
                return StringType()
            case "float":
                return FloatType()
            case "timestamp":
                return TimestampType()
            case "date":
                return DateType()
            case _:
                return "not correct"
    def __repr__(self):
        return f"""
            {self.schema}.{self.table}
            {self.columns}
            {self.types}
            {self.nullable}
            {self.table_size}"""


class DDLContainer:

    def __init__(self, parse_results: List):
        self.table_container_list = [TableContainer(elem) for elem in parse_results]

    def __repr__(self):
        return [elem for elem in self.table_container_list]