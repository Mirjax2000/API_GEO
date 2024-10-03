import customtkinter as ctk
from icecream import ic

import configs.api_config as apiconf
import configs.config as conf


class Api(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent, fg_color="transparent", corner_radius=8)
        self.pack(fill="both", side="top", expand=True)
        # --
        ic("apik aktivovano")
        self.header = ctk.CTkFrame(self, height=104, **conf.layout_config)
        self.header.pack(
            fill="x",
            side="top",
            expand=False,
            pady=(0, 4),
        )
        # --
        self.load_data = ctk.CTkButton(
            self.header,
            text="Load Data",
            fg_color=(conf.btn_light, conf.btn_dark),
            text_color=("black", "white"),
            font=conf.small_font,
            hover_color=(conf.light_color, conf.dark_color),
            compound="top",
            image=conf.img_loader("./assets/add_file_40.png", 40),
            command=conf.file_loader,
        )
        self.load_data.grid(row=0, column=0, sticky="nsw", pady=4, padx=4)
        # --
        self.save_data = ctk.CTkButton(
            self.header,
            text="Save Data",
            fg_color=(conf.btn_light, conf.btn_dark),
            text_color=("black", "white"),
            font=conf.small_font,
            hover_color=(conf.light_color, conf.dark_color),
            compound="top",
            image=conf.img_loader("./assets/icons8-save-close-40.png", 40),
            state="disabled",
        )
        self.save_data.grid(row=0, column=2, sticky="nse", pady=4, padx=4)
        # --
        # Header GRID
        self.header.rowconfigure(0, weight=0, uniform="a")
        self.header.columnconfigure(0, weight=0, uniform="a")
        self.header.columnconfigure(1, weight=1, uniform="b")
        self.header.columnconfigure(2, weight=0, uniform="a")
        # --
        self.body = ctk.CTkFrame(self, **conf.layout_config)
        self.body.pack(fill="both", side="top", expand=True)
        # --
