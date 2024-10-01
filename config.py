# region Importy
import json
from lib2to3.fixes.fix_next import bind_warning
import logging as lg
import os
from pathlib import Path
from random import choice

import customtkinter as ctk
from customtkinter import filedialog
from icecream import ic
from PIL import Image

# endregion

lg.basicConfig(filename="./app.log", filemode="w", level=lg.INFO)

# region -- VAR --
app_theme: list[str] = [""]
get_modul: list = [""]
dark_color: str = "#4f4f4f"
light_color: str = "#67b5ff"
border_radius: int = 4
menu_font: tuple = ("Helvetica", 18)
small_font: tuple = ("Helvetica", 14)
medium_font: tuple = ("Helvetica", 18)
large_font: tuple = ("Helvetica", 22)
layout_config: dict = {
    "fg_color": "transparent",
    "border_width": 1,
    "corner_radius": border_radius,
}

left_btn_config: dict = {
    "font": medium_font,
    "anchor": "w",
    "compound": "left",
    "height": 80,
    "corner_radius": border_radius,
    "fg_color": "transparent",
    "hover": False,
    "text_color": ("black", "white"),
}


def img_loader(vstup_dir: str, size_img: int):
    """Nahrává obrázky do apky."""
    img = ctk.CTkImage(light_image=Image.open(vstup_dir), size=(size_img, size_img))
    if not img:
        log("Nepodařilo se načíst obrázek z:", "Error", vstup_dir)
        return None
    return img


# endregion
#
# region -- APP --


def appearance(theme: str, color: str, ctk) -> None:
    # nastaveni Theme a scalingu
    #
    ctk.set_appearance_mode(theme)
    ctk.set_default_color_theme(color)
    app_theme[0] = theme
    # --
    ctk.set_widget_scaling(1.0)
    ctk.set_window_scaling(1.0)
    lg.info("Theme: %s, barva: %s", theme, color)
    # konec funkce


def app_init(self, name, width, height) -> None:
    """Nastavy zakladni rozmer appky"""
    #
    self.title(name)
    self.iconbitmap("./assets/ico.ico")
    center_window(self, width, height)
    self.minsize(width, height)
    self.resizable(True, True)
    # konec funkce


def center_window(self, app_width: int, app_height: int) -> None:
    """Centers the window on the screen."""
    #
    self.update_idletasks()
    width: int = app_width
    height: int = app_height
    screen_width: int = self.winfo_screenwidth()
    screen_height: int = self.winfo_screenheight()
    x: int = screen_width // 2 - width // 2
    y: int = screen_height // 2 - height // 2
    self.geometry(f"{width}x{height}+{x}+{y}")
    lg.info("Rozliseni: %s x %s.", width, height)
    # konec funkce


# endregion
#
# region -- MENU --
def create_menu(self, mb, cdm, mongo, ctk) -> None:
    """Vytvor menu bar"""
    #
    menu = mb(self, height=40, padx=10, bg_color=("#dbdbdb", "#2b2b2b"))
    buttons: dict = {
        "system_btn": " System ",
        "settings_btn": " Settings ",
        "info_btn": " Info ",
    }
    column: int = len(buttons)  # pocet menu btns
    # --
    config: dict = {
        "corner_radius": border_radius,
        "font": menu_font,
        "hover_color": (light_color, dark_color),
    }
    # --
    for name, label in buttons.items():
        setattr(self, name, menu.add_cascade(label, **config))
    # end buttony -----------------------
    # --
    # drop menu
    system_drop = cdm(widget=self.system_btn, **config)
    self.system_settings = system_drop.add_option(
        "Settings", command=lambda: change_theme(self, ctk)
    )
    system_drop.add_separator()
    self.konec = system_drop.add_option("Exit", command=self.destroy)
    # --
    settings_drop = cdm(widget=self.settings_btn, **config)
    self.api_settings = settings_drop.add_option("API settings")
    # --
    info_drop = cdm(widget=self.info_btn, **config)
    self.about = info_drop.add_option("About")
    # --
    # end drop menu -------------------------
    # --
    # GRID
    menu.columnconfigure(column, weight=1, uniform="a")
    # --
    # volame frame na detekci databaze
    db_frame(self, ctk, menu, column)
    # detekujeme databazi
    detect_db(self, mongo)
    # --
    # konec funkce


def db_frame(self, ctk, parent, column: int) -> None:
    """vytvor kontrolni frame pro databazi"""
    #
    self.detect_db_frame = ctk.CTkFrame(parent, fg_color="transparent")
    self.detect_db_frame.grid(row=0, column=column, sticky="e", padx=20)
    # --
    self.detect_db_label = ctk.CTkLabel(
        self.detect_db_frame,
        text="",
        font=medium_font,
        text_color=("black", "white"),
        compound="left",
    )
    self.detect_db_label.grid(row=0, column=0, sticky="ew")
    # konec funkce


def detect_db(self, mongo) -> None:
    """detekuj databazi"""
    #
    error_img = img_loader("./assets/error_40.png", 40)
    mongo_img = img_loader("./assets/mongo_40.png", 40)
    match mongo:
        case True:
            self.detect_db_label.configure(
                text="Mongo: connected",
                image=mongo_img,
            )
            log("Mongo: connect", "Info", mongo)
        # --
        case False:
            self.detect_db_label.configure(
                text="Mongo: disconnected", image=error_img, padx=10
            )
            log("Mongo: connect", "Error", mongo)
    # konec funkce


# endregion
#
# region -- LOGO --
def pick_logo():
    """losovani logo img"""
    #
    logo_list: list = []
    adresar: str = "./assets/logo/"
    # --
    for soubor in os.listdir(adresar):
        cesta_k_souboru = os.path.join(adresar, soubor)
        logo_list.append(img_loader(cesta_k_souboru, 80))
    # --
    logo = choice(logo_list)
    # --
    return logo
    # konec funkce


# endregion
#
# region -- LeftFrame --

def 
# left frame buttons
cfg_frame: dict = {
    "api": [
        "api_frame",
        0,
        0,
        "api_label",
        "A.P.I",
        img_loader("./assets/api_40.png", 30),
    ],
    "mongo": [
        "mongo_frame",
        1,
        0,
        "mongo_label",
        "MongoDB",
        img_loader("./assets/mongo_40.png", 30),
    ],
    "geo": [
        "geo_frame",
        2,
        0,
        "geo_label",
        "G.E.O.",
        img_loader("./assets/geo_40.png", 30),
    ],
}
# --


def make_frame_btns(
    self,
    frame_name: str,
    frame_row: int,
    frame_col: int,
    btn_name: str,
    btn_txt: str,
    img,
) -> None:
    """tvorba framu a jeho buttns"""
    #
    frame = ctk.CTkFrame(self)
    setattr(self, frame_name, frame)
    # --
    btn = ctk.CTkButton(
        frame,
        text=btn_txt,
        image=img,
        **left_btn_config,
    )
    setattr(self, btn_name, btn)
    btn.bind("<Button-1>", button_1)
    # --
    frame.grid(row=frame_row, column=frame_col, sticky="ew", padx=2, pady=1)
    btn.pack(fill="x", side="top", expand=True)
    # --
    # aktivace btn pri spusteni apky
    self.default_btn = ".!mainframe.!leftframe.!ctkframe.!ctkbutton"
    self.default_btn_widget = self.parent.nametowidget(self.default_btn)
    self.default_btn_widget.configure(fg_color=(light_color, dark_color))
    # konec funkce


# endregion
#
# region -- FUNKCE --
#


# change theme
def change_theme(self, ctk) -> None:
    """zmena theme"""
    #
    self.theme = "light" if self.theme == "dark" else "dark"
    ctk.set_appearance_mode(self.theme)
    log("Theme zmeneno:", "Info", self.theme)
    app_theme[0] = self.theme
    # konec funkce


def run_and_control(self, trida):
    """funkce na spousteni instanci a kontrola"""
    #
    instance = trida(self)
    # --
    if isinstance(instance, trida):
        log("instance is running.", "Info", instance)
    else:
        log("Instance fail!!!", "Error", instance)
    # --
    return instance
    # konec funkce



def file_loader():
    """ziskani jmeno souboru"""
    #
    file = filedialog.askopenfile(
        initialdir="./data",
        title="Select a file",
        filetypes=[("CSV files", "*.csv"), ("JSON files", "*.json")],
    )
    # --
    if file:
        file_name: str = Path(file.name).name
        log("file name extracted: ", "Info", file_name)
        # --
        return file
    else:
        log("file name extraction: ", "Error", "FAIL")
        # --
        return "No file selected"
    # konec funkce


def file_saver() -> str:
    """ziskani cesty pro ukladani dat"""
    #
    file_path: str = filedialog.asksaveasfilename(
        title="Save Data",
        initialdir="./data",
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv"), ("JSON files", "*.json")],
    )
    # --
    if file_path:
        file: list = list(file_path.split("/"))
        log("path extracted: ", "Info", file[-1])
        # --
        return file_path
    else:
        log("path extraction: ", "Error", "FAIL")
        # --
        return "Soubor nebyl vybran"
    # konec funkce


def button_1(event) -> None:
    """clicknuti mysi"""
    #
    widget = event.widget.master  # label
    widget_text = widget.cget("text")
    ic(widget_text)
    grand_parent = widget.master.master  # cely LeftFrame
    # --
    for frame in grand_parent.winfo_children():
        for label in frame.winfo_children():
            label.configure(fg_color="transparent")
    # --
    widget.configure(fg_color=(light_color, dark_color))
    # konec funkce


# endregion
#
# region -- SERVISNI FUNKCE --
def log(msg: str, stav: str, object):
    """funkce na vypisovani logu"""
    # servisni funkce
    temp: tuple = ("%s %s", msg, object)
    lg.error(*temp) if stav == "Error" else lg.info(*temp)
    # konec funkce


def get_family(self):
    """zjisti vztahy"""
    # servisni funkce
    temp = self.main_frame.left_frame.winfo_children()
    labels: list = [item.winfo_children() for item in temp]
    # konec funkce


def read_settings(vstup):
    """read settings"""
    #
    with open(vstup, "r", encoding="utf-8") as file:
        settings = json.load(file)
    # --
    return settings
    # konec funkce


# endregion
#
if __name__ == "__main__":
    pass
