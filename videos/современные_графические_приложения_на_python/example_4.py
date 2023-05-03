
import tkinter
import webbrowser
import customtkinter


SITES = {
    "option_1": "https://doc.rust-lang.org/book/",
    "option_2": "https://stackoverflow.com/questions/1077347/hello-world-in-python"
}


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("CTk example")
        combobox = customtkinter.CTkOptionMenu(self,
                                       values=list(SITES.keys()),
                                       command=self.optionmenu_callback)
        combobox.pack(padx=20, pady=10)
        combobox.set("option 2")  # set initial value

    def optionmenu_callback(self, choice):
        print("optionmenu dropdown clicked:", choice)
        webbrowser.open(SITES[choice])


app = App()
app.mainloop()





