import dearpygui.dearpygui as dpg

# TODO function - ddl.py -> DDLContainer -> __cast_hive_to_spark_type() not cover all type


if __name__ == '__main__':

    dpg.create_context()

    columns_number = 4

    with dpg.window(label="Tutorial", pos=(200, 200), tag="mainwindow"):
        with dpg.table(header_row=True,
                       resizable=True,
                       policy=dpg.mvTable_SizingStretchProp,
                       borders_outerH=True,
                       borders_innerV=True,
                       borders_innerH=True,
                       borders_outerV=True):

            for i in range(0, columns_number):
                dpg.add_table_column(label=f"Header {i}")

            for i in range(0, 4):
                with dpg.table_row():
                    for j in range(0, columns_number):
                        dpg.add_text(f"Row{i} Column{j}")


    dpg.create_viewport(title='Synthetic Generator', width=1800, height=1100)
    dpg.setup_dearpygui()
    dpg.set_global_font_scale(3)
    dpg.set_primary_window("mainwindow", True)
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


