import dearpygui.dearpygui as dpg

# Реестр элементов.
# Просмотр информации об объекте.

dpg.create_context()

with dpg.window(label="Tutorial"):
    dpg.add_button(label="Apply", width=300)
    btn = dpg.add_button(label="Apply 2")
    dpg.set_item_label(btn, "Button 57")
    dpg.set_item_width(btn, 200)

# Создаем отдельное окно для просмотра информации
dpg.show_item_registry()

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
