import customtkinter as ctk
from icecream import ic
import configs.config as conf


class Mongo(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent, fg_color="white", corner_radius=8)
        self.pack(fill="both", side="top", expand=True)
        ic("mongo aktivovano")
        self.header = ctk.CTkFrame(self, height=104, **conf.layout_config)
        self.header.pack(fill="x", side="top", expand=False, pady=(0, 4))
        #
        self.body = ctk.CTkFrame(self, **conf.layout_config)
        self.body.pack(fill="both", side="top", expand=True)
