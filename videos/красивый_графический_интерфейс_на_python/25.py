import dearpygui.dearpygui as dpg

# Подсказки при наведении.

dpg.create_context()

with dpg.window(label="Tutorial"):
    dpg.add_text("Hover me", tag="tooltip_parent")

    with dpg.tooltip("tooltip_parent"):
        dpg.add_text("A tooltip")

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
