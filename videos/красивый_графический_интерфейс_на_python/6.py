import dearpygui.dearpygui as dpg

# Привязка callback'ов к кнопкам

dpg.create_context()

def button_callback(sender, app_data, user_data):
    print(f"sender is: {sender}")
    print(f"app_data is: {app_data}")
    print(f"user_data is: {user_data}")

with dpg.window(label="Tutorial"):
    dpg.add_button(label="Apply", callback=button_callback, user_data="Some Data")
    btn = dpg.add_button(label="Apply 2")
    dpg.set_item_callback(btn, button_callback)
    dpg.set_item_user_data(btn, "Some Extra User Data")

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
