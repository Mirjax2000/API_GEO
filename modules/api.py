import customtkinter as ctk
import requests
from icecream import ic

import configs.api_config as apiconf
import configs.config as conf


class Api(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent, fg_color="transparent", corner_radius=8)
        self.pack(fill="both", side="top", expand=True)
        # ------------------------------------
        self.header = ctk.CTkFrame(self, height=104, **conf.layout_config)
        self.header.pack(
            fill="x",
            side="top",
            expand=False,
            pady=(0, 4),
        )
        # ----------------------------------
        # header children
        self.load_data = ctk.CTkButton(
            self.header,
            text="Load Data",
            image=conf.img_loader("./assets/add_file_40.png", 40),
            command=conf.file_loader,
            **apiconf.conf.header_btn_config,
        )
        self.load_data.grid(row=0, column=0, sticky="nsw", pady=4, padx=4)
        # --
        self.save_data = ctk.CTkButton(
            self.header,
            text="Save Data: Empty",
            image=conf.img_loader("./assets/icons8-save-close-40.png", 40),
            state="disabled",
            **apiconf.conf.header_btn_config,
        )
        self.save_data.grid(row=0, column=2, sticky="nse", pady=4, padx=4)
        # ---------------------------------------------
        # Header GRID
        self.header.rowconfigure(0, weight=0, uniform="a")
        self.header.columnconfigure(0, weight=0, uniform="a")
        self.header.columnconfigure(1, weight=1, uniform="b")
        self.header.columnconfigure(2, weight=0, uniform="a")
        # --
        # -- api choose Frame
        self.set_api = ctk.CTkFrame(self, **conf.layout_config)
        self.set_api.pack(fill="x", side="top", expand=False, pady=(0, 5))
        # --
        set_api_val: list = [
            "P.S.C. + mesto",
            "P.S.C.",
            "A.P.I. - I",
            "A.P.I. - II",
            "A.P.I. - III",
        ]
        self.vyber_api = ctk.CTkOptionMenu(
            self.set_api,
            values=set_api_val,
            **conf.menu_options_config,
            command=self.call_api,
        )

        self.vyber_api.set(set_api_val[0])
        self.vyber_api.grid(row=0, column=0, sticky="w", pady=5, padx=5)
        # --
        self.psc = Psc(self)
        self.psc_mesto = PscMesto(self)
        self.psc.pack_forget()
        self.psc_mesto.pack_forget()

    def call_api(self, event) -> None:
        match event:
            case "P.S.C.":
                self.psc_mesto.pack_forget()
                self.psc.pack(fill="both", side="top", expand=True)
            case "P.S.C. + mesto":
                self.psc.pack_forget()
                self.psc_mesto.pack(fill="both", side="top", expand=True)


class Psc(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent, **conf.layout_config)
        self.pack(fill="both", side="top", expand=True)
        self.label = ctk.CTkLabel(self, text="psc")
        self.label.pack()


class PscMesto(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent, **conf.layout_config)
        self.pack(fill="both", side="top", expand=True)
        self.label = ctk.CTkLabel(self, text="psc mesto")
        self.label.pack()
