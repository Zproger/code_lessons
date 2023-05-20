import dearpygui.dearpygui as dpg

# Создаем несколько окон через контейнеры.

dpg.create_context()

with dpg.window(label="Window1", pos=(0,0)):
    pass

with dpg.window(label="Window2", pos=(100,0)):
    pass

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
