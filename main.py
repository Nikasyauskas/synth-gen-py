import dearpygui.dearpygui as dpg
from dpgex import show_main, show_demo, Gui, show_input_output, show_custom_table
from simple_ddl_parser import parse_from_file
from ddl import DDLContainer
from enum import Enum



if __name__ == '__main__':
    app = Gui()
    app.run_app()
