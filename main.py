import customtkinter as ctk
import MoreCustomTkinterWidgets as mckw
from CTkMenuBar import CTkMenuBar as mb
from CTkMenuBar import CustomDropdownMenu as cdm

import config as conf


class App(ctk.CTk):
    #
    def __init__(self) -> None:
        self.theme: str = "system"
        self.color: str = "blue"
        self.mongo_db: bool = False
        #
        super().__init__()
        conf.app_init(self, "mapibase", 1024, 768)
        conf.appearance_mode(self.theme, self.color, ctk)
        parent, column = conf.create_menu(self, mb, cdm)
        conf.detect_db(self, ctk, parent, column)

        self.update_idletasks()


if __name__ == "__main__":
    app: App = App()
    app.mainloop()
