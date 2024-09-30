import logging as lg

import customtkinter as ctk
import MoreCustomTkinterWidgets as mctk
from CTkMenuBar import CTkMenuBar as mb
from CTkMenuBar import CustomDropdownMenu as cdm
from icecream import ic
import timeit
import config as conf


class App(ctk.CTk):
    #
    def __init__(self) -> None:
        self.theme: str = "dark"
        self.color: str = "blue"
        self.mongo_db = False
        #
        super().__init__()
        conf.app_init(self, "mapibase", 1024, 768)
        conf.appearance(self.theme, self.color, ctk)
        parent, column = conf.create_menu(self, mb, cdm, ctk)
        conf.db_frame(self, ctk, parent, column)
        conf.detect_db(self, self.mongo_db)
        #
        # volame tridy
        self.main_frame: MainFrame = conf.run_and_control(self, MainFrame)
        self.update_idletasks()


class MainFrame(ctk.CTkFrame):
    """Hlavni frame"""

    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent, fg_color="transparent")
        self.pack(side="top", fill="both", expand=True, padx=2, pady=2)
        #
        # volame tridy
        self.header_frame: Header = conf.run_and_control(self, Header)
        self.left_frame: LeftFrame = conf.run_and_control(self, LeftFrame)
        self.playground: PlayGround = conf.run_and_control(self, PlayGround)

        # MainFrame GRID
        self.rowconfigure(0, weight=0, uniform="a")  # Header
        self.rowconfigure(1, weight=1, uniform="b")  # LeftFrame
        self.columnconfigure(0, weight=0, uniform="a")
        self.columnconfigure(1, weight=1, uniform="b")


class Header(ctk.CTkFrame):
    """Horni frame"""

    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent, fg_color="transparent")
        self.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)
        #
        self.logo_frame = ctk.CTkFrame(self, **conf.layout_config)
        self.logo_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 4))
        #
        self.logo_label = ctk.CTkLabel(
            self.logo_frame,
            text="",
            image=conf.pick_logo(),
            width=176,
            height=96,
            compound="center",
        )
        self.logo_label.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        #
        self.choose_and_act = ctk.CTkFrame(self, height=100, **conf.layout_config)
        self.choose_and_act.grid(row=0, column=1, sticky="nsew")
        # Header GRID

        self.columnconfigure(0, weight=0, minsize=180, uniform="a")
        self.columnconfigure(1, weight=1, uniform="b")
        self.rowconfigure(0, weight=0, minsize=100, uniform="a")


class LeftFrame(ctk.CTkFrame):
    """Levy frame"""

    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent, **conf.layout_config)
        self.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

        for name in conf.cfg_frame:
            conf.make_frame_label(self, *conf.cfg_frame[name])
        #
        # LeftFrame GRID

        self.columnconfigure(0, weight=1, minsize=180, uniform="a")


class PlayGround(ctk.CTkFrame):
    """playground"""

    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent, **conf.layout_config)
        self.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)


if __name__ == "__main__":
    app: App = App()
    app.mainloop()
