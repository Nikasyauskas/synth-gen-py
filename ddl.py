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
from collections import Counter

# TODO ??? make abstract Container class and inherite TableContainer and DictContainer from it ???
# TODO learn gui debugger



class TableContainer:

    def __init__(self, ddl_metadata: Dict):
        self.schema = ddl_metadata["schema"]
        self.table = ddl_metadata["table_name"]
        self.columns = self.__extract_colums(ddl_metadata)
        self.types = self.__extract_types(ddl_metadata)
        self.partitions_col = self.__extract_partitions_columns(ddl_metadata)
        self.partitions_types = self.__extract_partitions_types(ddl_metadata)
        self.spark_types = self.__cast_hive_to_spark_type(self.types)
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
            types_list.append(elem["type"])
        return types_list

    def __extract_nullable(self, ddl_metadata: Dict):
        nullable_list = []
        for elem in ddl_metadata["columns"]:
            nullable_list.append(elem["nullable"])
        return nullable_list

    def __extract_partitions_columns(self, ddl_metadata: Dict):
        part_columns_list = []
        for elem in ddl_metadata["partitioned_by"]:
            part_columns_list.append(elem["name"])
        return part_columns_list

    def __extract_partitions_types(self, ddl_metadata: Dict):
        part_types_list = []
        for elem in ddl_metadata["partitioned_by"]:
            part_types_list.append(elem["type"])
        return part_types_list

    def __cast_hive_to_spark_type(self, data_type: List):
        # TODO function - ddl.py -> DDLContainer -> __cast_hive_to_spark_type() not cover all type
        spark_types_list = []
        for ELEM in data_type:
            elem = ELEM.lower()
            match elem:
                case "int":  # add "or integer" construction
                    return spark_types_list.append(IntegerType())
                case "string":
                    return spark_types_list.append(StringType())
                case "float":
                    return spark_types_list.append(FloatType())
                case "timestamp":
                    return spark_types_list.append(TimestampType())
                case "date":
                    return spark_types_list.append(DateType())
                case _:
                    return "not correct"
        return spark_types_list

    def get_columns(self):
        return self.columns

    def __repr__(self):
        ddl_info_repr = "table: " + self.schema + "." + self.table + '\n'
        for col, type, nullable in zip(self.columns, self.types, self.nullables):
            ddl_info_repr += '\t' + col + " " + str(type) + " " + str(nullable) + '\n'
        for col, type in zip(self.partitions_col, self.partitions_types):
            ddl_info_repr += "partitions: " + col + " " + type + '\n'
        ddl_info_repr += "\n"
        return ddl_info_repr


class DictContainer:

    def __init__(self, table_container_list: List[TableContainer]):
        self.columns = self.__common_columns(table_container_list)

    def __common_columns(self, table_container_list: List[TableContainer]):
        columns_collector = []
        for container in table_container_list:
            for col in container.get_columns():
                columns_collector.append(col)
        count_columns = Counter(columns_collector)
        common_columns = [key for key, val in count_columns.items() if val > 1]
        return common_columns

    def get_columns(self):
        return self.columns

    def is_common_columns(self):
        return len(self.columns) > 0


class DDLContainer:

    def __init__(self, parse_results: List):
        self.table_container_list = [TableContainer(elem) for elem in parse_results]
        self.dict_container = DictContainer(self.table_container_list)

    def get_containers(self):
        container_info = ""
        for elem in self.table_container_list:
            container_info += elem.__repr__()
        return container_info

    def get_common_columns(self):
        return self.dict_container.get_columns()

    def is_common_columns(self):
        return self.dict_container.is_common_columns()
