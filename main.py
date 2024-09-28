import customtkinter as ctk
import MoreCustomTkinterWidgets as mckw
from CTkMenuBar import CTkMenuBar as mb
from CTkMenuBar import CustomDropdownMenu as cdm
import logging as lg

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
        parent, column = conf.create_menu(self, mb, cdm, ctk)
        conf.db_frame(self, ctk, parent, column)
        conf.detect_db(self, self.mongo_db)
        #
        # volame tridy
        self.main_frame = conf.run_and_control(self, MainFrame)

        self.update_idletasks()


class MainFrame(ctk.CTkFrame):
    """Hlavni frame"""

    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent, fg_color=parent._fg_color)
        self.pack(side="top", fill="both", expand=True)
        #
        # volame tridy
        self.header_frame = conf.run_and_control(self, Header)
        self.left_frame = conf.run_and_control(self, LeftFrame)
        self.playground = conf.run_and_control(self, PlayGround)

        # MainFrame GRID
        self.rowconfigure(0, weight=0, uniform="a")
        self.rowconfigure(1, weight=1, uniform="b")
        self.columnconfigure(0, weight=0, uniform="a")
        self.columnconfigure(1, weight=1, uniform="b")


class Header(ctk.CTkFrame):
    """Horni frame"""

    def __init__(self, parent):
        self.parent = parent
        super().__init__(
            parent, height=100, fg_color=parent._fg_color, **conf.layout_config
        )
        self.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)
        #


class LeftFrame(ctk.CTkFrame):
    """Levy frame"""

    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent, fg_color=parent._fg_color, **conf.layout_config)
        self.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)


class PlayGround(ctk.CTkFrame):
    """Levy frame"""

    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent, fg_color=parent._fg_color, **conf.layout_config)
        self.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)


if __name__ == "__main__":
    app: App = App()
    app.mainloop()
