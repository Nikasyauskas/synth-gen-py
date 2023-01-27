import dearpygui.dearpygui as dpg
from dpgex import show_main, show_demo, Gui
# show_demo()
# show_custom_table()
# show_input_output()
# show_main()

# TODO function - ddl.py -> DDLContainer -> __cast_hive_to_spark_type() not cover all type
# TODO function __file_dialog_cancel close application - it should just close file dialog exit code 139

if __name__ == '__main__':
    app = Gui()
    app.run_app()

