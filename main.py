"""hlavni frame aplikace"""

import customtkinter as ctk
from CTkMenuBar import CTkMenuBar as mb
from CTkMenuBar import CustomDropdownMenu as cdm

import configs.config as conf

# import MoreCustomTkinterWidgets as mctk
# from icecream import ic
# load settings
settings_file: str = "./configs/settings.json"
settings: dict = conf.read_settings(settings_file)


class App(ctk.CTk):
    """hlavni apka"""
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
        # defaultni modul pri startu systemu
        self.modul = "api"
        self.api = conf.run_and_control(self, Api)
        # --

    def mrkni_na_modul(self) -> None:
        """kontroluje zmacknute tlacitko"""

        name: str = (
            str(list(str(self.winfo_children()).strip().split("!"))[-1])
            .replace(">", "")
            .replace("]", "")
        )
        name: str = name[:3]
        if name != self.modul:
            conf.vymaz_deti(self)

            match self.modul:
                case "api":
                    self.api: Api = conf.run_and_control(self, Api)
                    # --
                case "mon":
                    self.mongodb: Mongo = conf.run_and_control(self, Mongo)
                # --
                case "geo":
                    self.geo: Geo = conf.run_and_control(self, Geo)
                # --


if __name__ == "__main__":
    app: App = App()
    app.mainloop()
