import customtkinter as ctk
from icecream import ic
import config as conf


class Geo(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent, fg_color="lightgreen")
        self.pack(fill="both", side="top", expand=True)
        ic('GEO activovano')

      
