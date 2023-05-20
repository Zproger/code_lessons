import dearpygui.dearpygui as dpg

# Диалоговые окна.

dpg.create_context()

with dpg.window(label="Delete Files", modal=True, show=False, tag="modal_id", no_title_bar=True):
    dpg.add_text("All those beautiful files will be deleted.\nThis operation cannot be undone!")
    dpg.add_separator()
    dpg.add_checkbox(label="Don't ask me next time")
    with dpg.group(horizontal=True):
        dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("modal_id", show=False))
        dpg.add_button(label="Cancel", width=75, callback=lambda: dpg.configure_item("modal_id", show=False))

with dpg.window(label="Tutorial"):
    dpg.add_button(label="Open Dialog", callback=lambda: dpg.configure_item("modal_id", show=True))

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
