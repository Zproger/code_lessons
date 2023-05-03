import tkinter
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("CTk example")
        self.button = customtkinter.CTkButton(self, text="Subscribe to ZProger", command=self.button_click)
        self.button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def button_click(self):
        print("button click")


app = App()
app.mainloop()