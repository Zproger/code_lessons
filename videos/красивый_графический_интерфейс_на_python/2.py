import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

# Source:
# https://github.com/hoffstadt/DearPyGui/blob/master/dearpygui/demo.py

# Демонстрация всех виджетов и возможностей

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=800, height=600)

demo.show_demo()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
