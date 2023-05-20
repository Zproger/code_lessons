import dearpygui.dearpygui as dpg

# Установка значений по умолчанию

dpg.create_context()

with dpg.window(width=300):
    dpg.add_slider_int(default_value=15, tag="slider_int")

# Устанавливаем значение 40 в slider_int
dpg.set_value("slider_int", 40)

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
