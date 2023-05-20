import dearpygui.dearpygui as dpg

# Создаем таблицы.
# Больше примеров:
# https://dearpygui.readthedocs.io/en/latest/documentation/tables.html

dpg.create_context()

with dpg.window(label="Tutorial"):

    with dpg.table(header_row=True):
        dpg.add_table_column(label="Header 1")
        dpg.add_table_column(label="Header 2")
        dpg.add_table_column(label="Header 3")

        for i in range(0, 4):
            with dpg.table_row():
                for j in range(0, 3):
                    dpg.add_text(f"Row{i} Column{j}")

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
