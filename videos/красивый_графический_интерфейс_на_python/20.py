import dearpygui.dearpygui as dpg

# Сохранение состояния программы.

dpg.create_context()

def save_init():
    dpg.save_init_file("dpg.ini")

dpg.configure_app(init_file="dpg.ini")  # Файл для сохранения состояния
with dpg.window(label="about", tag="main window"):
    dpg.add_button(label="Save Window pos", callback=lambda: save_init)

with dpg.window(label="about", tag="side window"):
    dpg.add_button(label="Press me")

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
