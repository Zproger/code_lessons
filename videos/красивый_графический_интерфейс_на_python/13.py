import dearpygui.dearpygui as dpg

# Привязка к тегам и источникам.

dpg.create_context()

with dpg.window(label="Tutorial"):
    dpg.add_checkbox(label="Radio Button1", tag="R1")
    dpg.add_checkbox(label="Radio Button2", source="R1")

    dpg.add_input_text(label="Text Input 1")
    dpg.add_input_text(label="Text Input 2")
    dpg.add_input_text(label="Text Input 3", source=dpg.last_item(), password=True)

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
