import tkinter
import customtkinter


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
        self.button_1 = customtkinter.CTkButton(self, text="open toplevel", command=self.open_toplevel)
        self.button_1.pack(side="top", padx=20, pady=20)
        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            # create window if its None or destroyed
            self.toplevel_window = ToplevelWindow(self)
        else:
            # if window exists focus it
            self.toplevel_window.focus()


if __name__ == "__main__":
    app = App()
    app.mainloop()