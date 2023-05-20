import dearpygui.dearpygui as dpg

# Отслеживание событий в граф.оболочке.
# Вывод значений всех редактируемых виджетов.

dpg.create_context()

def print_value(sender):
    sender_name = dpg.get_item_label(sender)
    if not sender_name:
        sender_name = "None"
    print(f"{sender_name}: dpg.get_value(sender)")

with dpg.window(width=300):
    input_txt1 = dpg.add_input_text()
    input_txt2 = dpg.add_input_text(
        label="InputTxt2",
        default_value="This is a default value!",
        callback=print_value
    )

    slider_float1 = dpg.add_slider_float()
    slider_float2 = dpg.add_slider_float(
        label="SliderFloat2",
        default_value=50.0,
        callback=print_value
    )

    dpg.set_item_callback(input_txt1, print_value)
    dpg.set_item_callback(slider_float1, print_value)

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
