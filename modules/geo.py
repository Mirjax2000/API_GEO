import customtkinter as ctk
import tkintermapview as map
from icecream import ic
import configs.config as conf
import configs.geo_config as geoconf


class Geo(ctk.CTkFrame):
    """aktivace GEO modulu"""

    def __init__(self, parent) -> None:
        self.parent = parent
        self.lat: float = 49.8038
        self.long: float = 15.4749
        self.zoom: int = 7
        # --
        super().__init__(parent, fg_color="transparent", corner_radius=8)
        self.pack(fill="both", side="top", expand=True)
        ic("GEO activovano")
        # --
        self.header = ctk.CTkFrame(self, height=104, **conf.layout_config)
        self.header.pack(
            fill="x",
            side="top",
            expand=False,
            pady=(0, 4),
        )
        # --
        self.body = ctk.CTkFrame(self, **conf.layout_config)
        self.body.pack(fill="both", side="top", expand=True)
        # --
        self.map = map.TkinterMapView(self.body)
        self.map.pack(fill="both", side="top", expand=True, pady=2, padx=2)
        # -- mapovy server
        self.map.set_tile_server(geoconf.mapy_cz_server)
        # --
        self.map.set_position(self.lat, self.long)
        self.map.set_zoom(self.zoom)
        self.marker_1 = self.map.set_address("Praha", marker=True)
        print(self.marker_1)
