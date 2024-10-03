import logging as lg
from dataclasses import Field, InitVar, dataclass
from tkinter import W

import customtkinter as ctk
import MoreCustomTkinterWidgets as mctk
from CTkMenuBar import CTkMenuBar as mb
from CTkMenuBar import CustomDropdownMenu as cdm
from icecream import ic

import configs.config as conf
from modules.api import Api
from modules.geo import Geo
from modules.mongo import Mongo

# load settings
settings_file: str = "./configs/settings.json"
settings: dict = conf.read_settings(settings_file)


class App(ctk.CTk):
    #
    def __init__(self) -> None:
        self.theme: str = settings["theme"]
        self.mongo_db = True
        # --
        super().__init__()
        conf.app_init(self, "mapibase", 1024, 768)
        conf.appearance(self.theme, ctk)
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
        self.logo_frame: LogoFrame = conf.run_and_control(self, LogoFrame)
        self.left_frame: LeftFrame = conf.run_and_control(self, LeftFrame)
        self.playground: PlayGround = conf.run_and_control(self, PlayGround)
        # --
        # MainFrame GRID
        self.rowconfigure(0, weight=0, uniform="a")  # LogoFrame
        self.rowconfigure(1, weight=1, uniform="b")  # LeftFrame
        # --
        self.columnconfigure(0, weight=0, uniform="a")
        self.columnconfigure(1, weight=1, uniform="b")  # PlayGround


class LogoFrame(ctk.CTkFrame):
    """Horni frame"""

    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent, **conf.layout_config)
        self.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        # --
        self.logo_label = ctk.CTkLabel(
            self,
            image=conf.pick_logo(),
            **conf.logo_label,
        )
        self.logo_label.pack(
            fill="both",
            side="top",
            expand=True,
            padx=2,
            pady=2,
        )


class LeftFrame(ctk.CTkFrame):
    """Levy frame"""

    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent, **conf.layout_config)
        self.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        # --
        conf.btns_maker(self)


class PlayGround(ctk.CTkFrame):
    """playground"""

    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent, fg_color="transparent")
        self.grid(row=0, rowspan=2, column=1, sticky="nsew", padx=2, pady=2)
        # --
        self.modul = "A.P.I."
        self.api = conf.run_and_control(self, Api)

    def mrkni_na_modul(self):
        """aktivace tridy podle tlacitka"""
        if self.modul != self.winfo_children():
            conf.vymaz_deti(self)
            #
        match self.modul:
            case "A.P.I.":
                self.api = conf.run_and_control(self, Api)
            case "MongoDB":
                self.mongo = conf.run_and_control(self, Mongo)
            case "G.E.O.":
                self.geo = conf.run_and_control(self, Geo)


@dataclass()
class Skladiste:
    """jeste nevim"""

    pass


if __name__ == "__main__":
    app: App = App()
    app.mainloop()
