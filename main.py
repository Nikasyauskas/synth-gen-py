import dearpygui.dearpygui as dpg

# TODO function - ddl.py -> DDLContainer -> __cast_hive_to_spark_type() not cover all type


if __name__ == '__main__':

    dpg.create_context()
    dpg.create_viewport(title='Synthetic Generator', width=1200, height=1200)
    dpg.set_global_font_scale(3)

    with dpg.window(label="Example Window", tag="fullscreen"):
        dpg.add_text("Hello, world")
        dpg.add_button(label="Save")
        dpg.add_input_text(label="string", default_value="Quick brown fox")
        dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

    dpg.setup_dearpygui()
    dpg.set_primary_window("fullscreen", True)
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


