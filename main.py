import dearpygui.dearpygui as dpg
from dpgex import show_custom_table
# show_demo()
# show_custom_table()

# TODO function - ddl.py -> DDLContainer -> __cast_hive_to_spark_type() not cover all type


if __name__ == '__main__':

    dpg.create_context()


    def show_status_update(sender, statusmessage):
        dpg.set_value("status_text", f"status is: {statusmessage}")

    with dpg.window(label="Tutorial", tag="mainwindow"):
        dpg.add_input_text(label="input1", tag="input1", callback=show_status_update)
        dpg.add_text(tag="status_text", default_value="status is: not value")

    dpg.create_viewport(title='Synthetic Generator', width=1800, height=1100)
    dpg.setup_dearpygui()
    dpg.set_global_font_scale(3)
    dpg.set_primary_window("mainwindow", True)
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
