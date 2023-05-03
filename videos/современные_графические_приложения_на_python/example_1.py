import tkinter
import customtkinter

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("light")

# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.geometry("400x240")

def button_function():
    print("button pressed")

button = customtkinter.CTkButton(master=app, text="Subscribe to ZProger", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
app.mainloop()