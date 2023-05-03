import customtkinter
import webbrowser
import tkinter


customtkinter.set_appearance_mode("light")
app = customtkinter.CTk()
app.geometry("400x300")


def button_click_event():
    dialog = customtkinter.CTkInputDialog(text="Site URL:", title="Test")
    response = dialog.get_input()
    webbrowser.open(response)


button = customtkinter.CTkButton(app, text="Open Dialog", command=button_click_event)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()