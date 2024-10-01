import customtkinter as ctk

import config as conf


class Api(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent, border_width=1, fg_color="transparent")
        self.pack(fill="both", side="top", expand=True, pady=2)
