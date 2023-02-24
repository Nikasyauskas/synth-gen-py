from abc import ABC
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

# TODO ??? make abstract Container class and inherite TableContainer and DictContainer from it ???
# TODO learn gui debugger

class TableContainer:

    def __init__(self, ddl_metadata: Dict):
        self.schema = ddl_metadata["schema"]
        self.table = ddl_metadata["table_name"]
        self.columns = self.__extract_colums(ddl_metadata)
        self.types = self.__extract_types(ddl_metadata)
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


        # data_type_lower = data_type.lower()
        # match data_type_lower:
        #     case "int":  # add "or integer" construction
        #         return IntegerType()
        #     case "string":
        #         return StringType()
        #     case "float":
        #         return FloatType()
        #     case "timestamp":
        #         return TimestampType()
        #     case "date":
        #         return DateType()
        #     case _:
        #         return "not correct"

    def get_columns(self):
        return self.columns

    def __repr__(self):
        ddl_info_repr = self.schema + "." + self.table + '\n'
        for col, type, nullable in zip(self.columns, self.types, self.nullables):
            ddl_info_repr += col + " " + str(type) + " " + str(nullable) + '\n'
        ddl_info_repr += "\n"
        return ddl_info_repr


class DictContainer:

    def __init__(self, table_container_list: List[TableContainer]):
        self.columns = None

    def __common_columns(self, table_container_list: List[TableContainer]):
        # TODO __common_columns not realised
        pass


class DDLContainer:

    def __init__(self, parse_results: List):
        self.table_container_list = [TableContainer(elem) for elem in parse_results]
        self.size = len(self.table_container_list)

    def get_container_size(self):
        return self.size

    def show_containers(self):
        container_info = ""
        for elem in self.table_container_list:
            container_info += elem.__repr__()
        return container_info