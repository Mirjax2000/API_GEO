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
        set_mapy_vrstvy: list = geoconf.vrstvy_map["mapy_cz"]
        self.mapy_vrstvy = ctk.CTkOptionMenu(
            self.set_map,
            width=150,
            values=set_mapy_vrstvy,
            font=conf.small_font,
            dynamic_resizing=False,
            text_color=("black", "white"),
            fg_color=(conf.light_color, conf.dark_color),
            command=self.map_vrstva,
        )

        self.mapy_vrstvy.set(set_mapy_vrstvy[0])
        self.mapy_vrstvy.grid(row=0, column=1, sticky="wns", pady=5, padx=5)
        #
        self.mapy_vrstvy.grid_remove()
        # -- google vrstva
        set_google_vrstva: list[str] = geoconf.vrstvy_map["google"]
        self.google_vrstva = ctk.CTkOptionMenu(
            self.set_map,
            width=150,
            values=set_google_vrstva,
            font=conf.small_font,
            dynamic_resizing=False,
            text_color=("black", "white"),
            fg_color=(conf.light_color, conf.dark_color),
            command=self.map_vrstva,
        )

        self.google_vrstva.set(set_google_vrstva[0])
        self.google_vrstva.grid(row=0, column=1, sticky="wns", pady=5, padx=5)
        #
        self.google_vrstva.grid_remove()
        # --
        self.entry = ctk.CTkEntry(
            self.set_map,
            width=350,
            placeholder_text="search",
            placeholder_text_color=("gray", "gray"),
            font=conf.small_font,
        )
        self.entry.grid(row=0, column=2, sticky="nse", padx=5, pady=5)
        # --
        self.home = ctk.CTkButton(
            self.set_map,
            text="HOME",
            fg_color=(conf.btn_light, conf.btn_dark),
            text_color=("black", "white"),
            font=conf.small_font,
            hover_color=(conf.light_color, conf.dark_color),
            command=self.center_home,
        )
        self.home.grid(row=0, column=3, sticky="nse", pady=5, padx=5)
        # ---------------------------------------
        # self.set_map GRID
        self.set_map.rowconfigure(0, weight=0, uniform="a")
        self.set_map.columnconfigure(0, weight=0, uniform="a")
        self.set_map.columnconfigure(1, weight=0, uniform="b")
        self.set_map.columnconfigure(2, weight=1, uniform="c")
        self.set_map.columnconfigure(3, weight=1, uniform="d")
        # --
        # -- Frame pro mapviewer
        self.body = ctk.CTkFrame(self, **conf.layout_config)
        self.body.pack(fill="both", side="top", expand=True)
        # --
        self.map = map.TkinterMapView(self.body)
        self.map.pack(fill="both", side="top", expand=True, pady=2, padx=2)
        # -- mapovy server
        # -- zavolej defaultni mapovy server
        self.call_map("default")
        self.map.set_position(self.lat, self.long)
        self.map.set_zoom(self.zoom)

    def call_map(self, event) -> None:
        """Vyber mapoveho serveru"""
        # defaultni stav
        if self.default_server == geoconf.mapy_cz_server:
            self.mapy_vrstvy.grid()
        elif self.default_server == geoconf.google_normal:
            self.google_vrstva.grid()
        else:
            self.mapy_vrstvy.configure(state="disabled")
            self.google_vrstva.configure(state="disabled")

        match event:
            case "default":
                self.map.set_tile_server(self.default_server)
            case "Mapy.cz":
                self.map.set_tile_server(geoconf.mapy_cz_server)
                if self.google_vrstva.winfo_ismapped():
                    self.google_vrstva.grid_remove()
                    self.mapy_vrstvy.configure(state="normal")
                    self.mapy_vrstvy.grid()
            case "Google":
                self.map.set_tile_server(geoconf.google_normal)
                if self.mapy_vrstvy.winfo_ismapped():
                    self.mapy_vrstvy.grid_remove()
                    self.google_vrstva.configure(state="normal")
                    self.google_vrstva.grid()
            case "OpenStreet map":
                self.map.set_tile_server(geoconf.open_server)
                self.mapy_vrstvy.configure(state="disabled")
                self.google_vrstva.configure(state="disabled")
        # konec funkce

    def center_home(self) -> None:
        """centruj mapu"""
        self.map.set_position(self.lat, self.long)
        self.map.set_zoom(self.zoom)
        # konec funkce

    def map_vrstva(self, event) -> None:
        """switch mapova vrstva"""
        match event:
            case "basic":
                self.map.set_tile_server(geoconf.mapy_cz_server)
            case "winter":
                self.map.set_tile_server(geoconf.mapy_cz_server_winter)
            case "outdoor":
                self.map.set_tile_server(geoconf.mapy_cz_server_outdoor)
            case "aerial":
                self.map.set_tile_server(geoconf.mapy_cz_server_aerial)
            case "normal":
                self.map.set_tile_server(geoconf.google_normal)
            case "sattelite":
                self.map.set_tile_server(geoconf.google_sattelite)
        # konec funkce
