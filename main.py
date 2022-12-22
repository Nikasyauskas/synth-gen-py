from simple_ddl_parser import parse_from_file
import pprint


if __name__ == '__main__':
    parse_results = parse_from_file('resources/hive_ddl_test.sql')

    pp = pprint.PrettyPrinter(indent=4)

    pp.pprint(parse_results)

