# region Importy
import logging
from tkinter import font
from tkinter.tix import COLUMN
import typing
from pathlib import Path
from tkinter import font
from customtkinter import filedialog
from PIL import Image

# endregion

lg.basicConfig(level=lg.INFO)

# region Promenne
border_radius: int = 4
menu_font: tuple = ("Helvetica", 18)
small_font: tuple = ("Helvetica", 14)
medium_font: tuple = ("Helvetica", 18)
large_font: tuple = ("Helvetica", 22)
good_color: str = "#218909"
error_color: str = "#a75a02"
<<<<<<< HEAD
layout_config: dict = {
    "border_width": 1,
    "border_color": "gray",
    "corner_radius": 4,
}


def img_loader(ctk, vstup_dir: str, size_img: int):
    """Nahrává obrázky do apky."""
    img = ctk.CTkImage(light_image=Image.open(vstup_dir), size=(size_img, size_img))
    if not img:
        lg.error(f"Nepodařilo se načíst obrázek z {vstup_dir}")
        return None
    return img


# endregion
#
# region -- APP --


def appearance_mode(theme: str, color: str, ctk) -> None:
    # nastaveni Theme a scalingu
    ctk.set_appearance_mode(theme)
    ctk.set_default_color_theme(color)
    #
    ctk.set_widget_scaling(1.0)
    ctk.set_window_scaling(1.0)
    logging.info("Theme: %s, barva: %s", theme, color)


def app_init(self, name, width, height) -> None:
    """Nastavy zakladni rozmer appky"""
    self.title(name)
    self.iconbitmap("./assets/ico.ico")
    center_window(self, width, height)
    self.minsize(width, height)
    self.resizable(True, True)


def center_window(self, app_width: int, app_height: int) -> None:
    """Centers the window on the screen."""
    self.update_idletasks()
    width: int = app_width
    height: int = app_height
    screen_width: int = self.winfo_screenwidth()
    screen_height: int = self.winfo_screenheight()
    x: int = screen_width // 2 - width // 2
    y: int = screen_height // 2 - height // 2
    self.geometry(f"{width}x{height}+{x}+{y}")
    logging.info("Rozliseni: %s x %s.", width, height)


# endregion
#
# region MENU
def create_menu(self, mb, cdm) -> tuple:
    menu = mb(self, height=40, padx=10)
    buttons: dict = {
        "system_btn": "System",
        "settings_btn": "Settings",
        "info_btn": "Info",
    }

    config: dict = {"corner_radius": border_radius, "font": menu_font}
    column: int = len(buttons)

    for name, label in buttons.items():
        setattr(self, name, menu.add_cascade(label, **config))

    # end buttony -----------------------

    # drop menu
    system_drop = cdm(widget=self.system_btn, **config)
    self.system_settings = system_drop.add_option("Settings")
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
    menu.columnconfigure(column, weight=1)
    return (menu, column)
    # konec funkce


# endregion
#
# region FUNKCE
<<<<<<< HEAD
#
# region DETECT_DB
def db_frame(self, ctk, parent, column: int) -> None:
    """vytvor kontrolni frame pro databazi"""
    error_img = img_loader(ctk, "./assets/exclamation2.png", 40)
    #
    self.detect_db_frame = ctk.CTkFrame(parent, fg_color=parent._fg_color)
    self.detect_db_frame.grid(row=0, column=column, sticky="e", padx=20)
    #
    self.detect_db_error = ctk.CTkLabel(
        self.detect_db_frame,
        text="",
        image=error_img,
        compound="center",
    )
    self.detect_db_error.grid(row=0, column=0, sticky="ew")
    #
    self.detect_db_label = ctk.CTkLabel(
        self.detect_db_frame, text="", font=medium_font, corner_radius=5
    )
    self.detect_db_label.grid(row=0, column=1, sticky="ew", ipady=5, ipadx=5, padx=5)
    # konec funkce


def detect_db(self, mongo):
    """detekuj databazi"""
    match mongo:
        case True:
            self.detect_db_error.grid_remove()
            self.detect_db_label.configure(
                text="MongoDB: connected", fg_color=good_color
            )
            log("MongoDB: connect", "Info", mongo)

        case False:
            self.detect_db_error.grid()
            self.detect_db_label.configure(
                text="MongoDB: disconnected",
                fg_color=error_color,
            )
            log("MongoDB: connect", "Error", mongo)
    # konec funkce


# endregion


# appearance
def appearance(self, ctk):
    "zmena theme"
    if self.theme == "dark":
        self.theme = "light"
        ctk.set_appearance_mode("light")
        log("Theme zmeneno:", "Info", self.theme)
    else:
        self.theme = "dark"
        ctk.set_appearance_mode("dark")
        log("Theme zmeneno:", "Info", self.theme)
        self.update_idletasks()
    # konec funkce
=======


def test(self) -> None:
    self.flag = True
>>>>>>> parent of 8128e21 (makame)


def run_and_control(self, trida):
    instance = trida(self)

    if isinstance(instance, trida):
        log("instance is running.", "Info", instance)
    else:
        log("Instance fail!!!", "Error", instance)
    return instance


def log(msg: str, stav: str, object):
<<<<<<< HEAD
    """funkce na vypisovani logu"""
    match stav:
        case "Error":
            lg.error("%s %s", msg, object)
        case "Info":
            lg.info("%s %s", msg, object)
    # konec funkce
=======
    match stav:
        case "Error":
            logging.error("%s %s", msg, object)
        case "Info":
            logging.info("%s %s", msg, object)
>>>>>>> parent of 8128e21 (makame)


def file_loader():
    file = filedialog.askopenfile(
        initialdir="./data",
        title="Select a file",
        filetypes=[("CSV files", "*.csv"), ("JSON files", "*.json")],
    )

    if file:
        file_name: str = Path(file.name).name
        log("file name extracted: ", "Info", file_name)
        return file
    else:
        log("file name extraction: ", "Error", "FAIL")
        return "No file selected"


def file_saver() -> str:
    """Ahoj"""

    file_path: str = filedialog.asksaveasfilename(
        title="Save Data",
        initialdir="./data",
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv"), ("JSON files", "*.json")],
    )
    if file_path:
        file: list = list(file_path.split("/"))
        log("path extracted: ", "Info", file[-1])
        return file_path
    else:
        log("path extraction: ", "Error", "FAIL")
        return "Soubor nebyl vybran"


# endregion


if __name__ == "__main__":
    pass
