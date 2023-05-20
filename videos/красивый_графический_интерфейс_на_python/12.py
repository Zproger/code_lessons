import dearpygui.dearpygui as dpg

# Добавление объектов из одного контейнера в другой.
# Есть возможность взаимодействия между разными контейнерами.

dpg.create_context()

def add_buttons():
    global new_button1, new_button2
    new_button1 = dpg.add_button(label="New Button", before="delete_button", tag="new_button1")
    new_button2 = dpg.add_button(label="New Button 2", parent="secondary_window", tag="new_button2")


def delete_buttons():
    dpg.delete_item("new_button1")
    dpg.delete_item("new_button2")


with dpg.window(label="Tutorial", pos=(200, 200)):
    dpg.add_button(label="Add Buttons", callback=add_buttons)
    dpg.add_button(label="Delete Buttons", callback=delete_buttons, tag="delete_button")

with dpg.window(label="Secondary Window", tag="secondary_window", pos=(100, 100)):
    pass

dpg.create_viewport(title='Custom Title', width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
