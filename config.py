# region Importy
import logging
from tkinter import font
from tkinter.tix import COLUMN
import typing
from pathlib import Path
<<<<<<< HEAD
import customtkinter as ctk
=======

>>>>>>> parent of 8128e21 (makame)
from customtkinter import filedialog
from PIL import Image

# endregion

<<<<<<< HEAD
lg.basicConfig(filename="./app.log", filemode="w", level=lg.INFO)
=======
logging.basicConfig(level=logging.INFO)
>>>>>>> parent of 8128e21 (makame)

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
    "fg_color": "transparent",
    "border_width": 1,
    "border_color": "gray",
    "corner_radius": 4,
}
=======
>>>>>>> parent of 8128e21 (makame)

left_label_config: dict = {
    "font": medium_font,
    "anchor": "w",
    "compound": "left",
    "height": 60,
    "corner_radius": 4,
}


def img_loader(ctk, vstup_dir: str, size_img: int):
    """Nahrává obrázky do apky."""
    img = ctk.CTkImage(light_image=Image.open(vstup_dir), size=(size_img, size_img))
    if not img:
<<<<<<< HEAD
        log("Nepodařilo se načíst obrázek z:", "Error", vstup_dir)
=======
        logging.error(f"Nepodařilo se načíst obrázek z {vstup_dir}")
>>>>>>> parent of 8128e21 (makame)
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


# endregion
#
# region DETECT_DB
def detect_db(self, ctk, parent, column: int) -> None:
    error_img = img_loader(ctk, "./assets/exclamation2.png", 40)
    #
    detect_db_frame = ctk.CTkFrame(parent, fg_color=parent._fg_color)
    detect_db_frame.grid(row=0, column=column, sticky="e", padx=20)
    #
    detect_db_error = ctk.CTkLabel(
        detect_db_frame,
        text="",
        image=error_img,
        compound="center",
    )
    detect_db_error.grid(row=0, column=0, sticky="ew")
    #
    detect_db_label = ctk.CTkLabel(
        detect_db_frame, text="", font=medium_font, corner_radius=5
    )
    detect_db_label.grid(row=0, column=1, sticky="ew", ipady=5, ipadx=5, padx=5)
    #
    match self.mongo_db:
        case True:
            detect_db_error.grid_remove()
            detect_db_label.configure(text="MongoDB: connected", fg_color=good_color)
            logging.info("MongoDB: connected")

        case False:
            detect_db_error.grid()
            detect_db_label.configure(
                text="MongoDB: disconnected",
                fg_color=error_color,
            )

            logging.error("MongoDB: disconnected!")


# endregion
#
# region LeftFrame
def make_frame_label(
    self,
    frame_name: str,
    frame_row: int,
    frame_col: int,
    label_name: str,
    label_txt: str,
) -> None:
    frame = ctk.CTkFrame(self, **layout_config)
    setattr(self, frame_name, frame)

    label = ctk.CTkLabel(
        frame,
        text=label_txt,
        **left_label_config,
    )
    setattr(self, label_name, label)

    frame.grid(row=frame_row, column=frame_col, sticky="ew", padx=1)

    label.pack(fill="x", side="top", expand=True, pady=1)
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
    self.detect_db_frame = ctk.CTkFrame(parent, fg_color="transparent")
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


def detect_db(self, mongo) -> None:
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
def appearance(self, ctk) -> None:
    "zmena theme"
    self.theme = "light" if self.theme == "dark" else "dark"
    ctk.set_appearance_mode(self.theme)

    log("Theme zmeneno:", "Info", self.theme)
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
    temp: tuple = ("%s %s", msg, object)
    lg.error(*temp) if stav == "Error" else lg.info(*temp)

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
