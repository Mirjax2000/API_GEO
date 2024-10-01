import logging as lg
from tkinter import W

import customtkinter as ctk
import MoreCustomTkinterWidgets as mctk
from CTkMenuBar import CTkMenuBar as mb
from CTkMenuBar import CustomDropdownMenu as cdm
from icecream import ic
import config as conf
from api import Api
from mongo import Mongo
from geo import Geo


class App(ctk.CTk):
    #
    def __init__(self) -> None:
        self.theme: str = "dark"
        self.color: str = "blue"
        self.mongo_db = False
        # --
        super().__init__()
        conf.app_init(self, "mapibase", 1024, 768)
        conf.appearance(self.theme, self.color, ctk)
        conf.create_menu(self, mb, cdm, self.mongo_db, ctk)
        # --
        # volame tridy
        self.main_frame: MainFrame = conf.run_and_control(self, MainFrame)
        self.update_idletasks()


class MainFrame(ctk.CTkFrame):
    """Hlavni frame"""

    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent, fg_color="transparent")
        self.pack(side="top", fill="both", expand=True, padx=2, pady=2)
        # --
        # volame tridy
        self.header_frame: LogoFrame = conf.run_and_control(self, LogoFrame)
        self.left_frame: LeftFrame = conf.run_and_control(self, LeftFrame)
        self.playground: PlayGround = conf.run_and_control(self, PlayGround)
        # --
        # MainFrame GRID
        self.rowconfigure(0, weight=0, uniform="a")  # Header
        self.rowconfigure(1, weight=1, uniform="b")  # LeftFrame
        self.columnconfigure(0, weight=0, uniform="a")
        self.columnconfigure(1, weight=1, uniform="b")


class LogoFrame(ctk.CTkFrame):
    """Horni frame"""

    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent, **conf.layout_config)
        self.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        # --
        self.logo_label = ctk.CTkLabel(
            self,
            text="",
            image=conf.pick_logo(),
            width=180,
            height=100,
            compound="center",
        )
        self.logo_label.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        # --
        self.columnconfigure(0, weight=0, minsize=180, uniform="a")
        self.rowconfigure(0, weight=0, minsize=100, uniform="a")


class LeftFrame(ctk.CTkFrame):
    """Levy frame"""

    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent, **conf.layout_config)
        self.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        # --
        for name in conf.cfg_frame:
            conf.make_frame_label(self, *conf.cfg_frame[name])
        # --
        # LeftFrame GRID
        self.columnconfigure(0, weight=1, minsize=180, uniform="a")


class PlayGround(ctk.CTkFrame):
    """playground"""

    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent, fg_color="transparent")
        self.grid(row=0, rowspan=2, column=1, sticky="nsew", padx=2, pady=2)
        # --


if __name__ == "__main__":
    app: App = App()
    app.mainloop()
