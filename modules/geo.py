from cgitb import text

import customtkinter as ctk
import requests
import tkintermapview as map
from icecream import ic

import configs.config as conf
import configs.geo_config as geoconf


class Geo(ctk.CTkFrame):
    """aktivace GEO modulu"""

    def __init__(self, parent) -> None:
        self.parent = parent
        self.default_server = geoconf.mapy_cz_server
        self.lat: float = 49.8038
        self.long: float = 15.4749
        self.zoom: int = 7
        # --
        super().__init__(parent, fg_color="transparent", corner_radius=8)
        self.pack(fill="both", side="top", expand=True)
        # --
        self.header = ctk.CTkFrame(self, height=104, **conf.layout_config)
        self.header.pack(
            fill="x",
            side="top",
            expand=False,
            pady=(0, 4),
        )
        # ---------------------------------
        # header children
        self.load_data = ctk.CTkButton(
            self.header,
            text="Load Data",
            image=conf.img_loader("./assets/add_file_40.png", 40),
            command=conf.file_loader,
            **geoconf.header_btn_config,
        )
        self.load_data.grid(row=0, column=0, sticky="nsw", pady=4, padx=4)
        # --
        self.erase_data = ctk.CTkButton(
            self.header,
            text="Erase Data",
            image=conf.img_loader("./assets/eraser-40.png", 40),
            command=conf.file_loader,
            **geoconf.header_btn_config,
        )
        self.erase_data.grid(row=0, column=2, sticky="nse", padx=4, pady=4)
        self.erase_data.configure(state="disabled")
        # ----------------------------------
        # Header GRID
        self.header.rowconfigure(0, weight=0, uniform="a")
        self.header.columnconfigure(0, weight=0, uniform="a")
        self.header.columnconfigure(1, weight=1, uniform="b")
        self.header.columnconfigure(2, weight=0, uniform="a")
        # ----------------------------------
        # -- Frame
        self.set_map = ctk.CTkFrame(self, **conf.layout_config)
        self.set_map.pack(fill="x", side="top", expand=False, pady=(0, 5))
        # --
        set_server_val: list = [
            "Mapy.cz",
            "Google",
            "OpenStreet map",
        ]
        self.vyber_server = ctk.CTkOptionMenu(
            self.set_map,
            width=150,
            values=set_server_val,
            font=conf.small_font,
            dynamic_resizing=False,
            text_color=("black", "white"),
            fg_color=(conf.light_color, conf.dark_color),
            command=self.call_map,
        )

        self.vyber_server.set("Mapy.cz")
        self.vyber_server.grid(row=0, column=0, sticky="w", pady=5, padx=5)

        # -- mapy vrstvy
        set_mapy_vrstvy: list = ["basic", "winter", "outdoor", "aerial"]
        self.mapy_vrstvy = ctk.CTkOptionMenu(
            self.set_map,
            width=150,
            values=set_mapy_vrstvy,
            font=conf.small_font,
            dynamic_resizing=False,
            text_color=("black", "white"),
            fg_color=(conf.light_color, conf.dark_color),
        )

        self.mapy_vrstvy.set(set_mapy_vrstvy[0])
        self.mapy_vrstvy.grid(row=0, column=1, sticky="w", pady=5, padx=5)
        #
        self.mapy_vrstvy.grid_remove()
        # -- google vrstva
        set_google_vrstva: list[str] = ["normal", "sattelite"]
        self.google_vrstva = ctk.CTkOptionMenu(
            self.set_map,
            width=150,
            values=set_google_vrstva,
            font=conf.small_font,
            dynamic_resizing=False,
            text_color=("black", "white"),
            fg_color=(conf.light_color, conf.dark_color),
        )

        self.google_vrstva.set(set_google_vrstva[0])
        self.google_vrstva.grid(row=0, column=1, sticky="w", pady=5, padx=5)
        #
        self.google_vrstva.grid_remove()
        # ---------------------------------------
        # --
        self.body = ctk.CTkFrame(self, **conf.layout_config)
        self.body.pack(fill="both", side="top", expand=True)
        # --
        self.map = map.TkinterMapView(self.body)
        self.map.pack(fill="both", side="top", expand=True, pady=2, padx=2)
        # -- mapovy server
        # --
        self.call_map("default")
        self.map.set_position(self.lat, self.long)
        self.map.set_zoom(self.zoom)

    def call_map(self, event) -> None:
        """Vyber mapoveho serveru"""
        if self.default_server == geoconf.mapy_cz_server:
            self.vrstvy_mapy()

        match event:
            case "default":
                self.map.set_tile_server(self.default_server)
            case "Mapy.cz":
                self.map.set_tile_server(geoconf.mapy_cz_server)
                self.vrstvy_mapy()
            case "Google":
                self.map.set_tile_server(geoconf.google_normal)
                self.vrstvy_google()
            case "OpenStreet map":
                self.map.set_tile_server(geoconf.open_server)

    def vrstvy_mapy(self): ...
    def vrstvy_google(self): ...

    # konec funkce
