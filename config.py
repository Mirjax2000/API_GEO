from PIL import Image
import typing
from tkinter import filedialog
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

# region Promenne
font_big: tuple[str, int, str] = ("Arial", 30, "normal")
font_normal: tuple[str, int, str] = ("Arial", 20, "normal")
font_small: tuple[str, int, str] = ("Arial", 10, "normal")


def img_loader(ctk, vstup_dir: str) -> Any:
    """Nahrává obrázky do apky."""
    img: Any = ctk.CTkImage(light_image=Image.open(vstup_dir), size=(25, 25))
    if not img:
        logging.error(f"Nepodařilo se načíst obrázek z {vstup_dir}")
        return None
    return img


# endregion
#
# region -- APP --

ahoj:bool = True
def app_init(self, name: str) -> None:
    self.title(name)
    self.iconbitmap("./assets/ico.ico")
    center_window(self, 1024, 768)
    self.minsize(width=1024, height=768)
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


# endregion
#
# region FUNKCE


def test(self) -> None:
    self.flag = True


def run_and_control(self, trida):
    instance = trida(self)

    if isinstance(instance, trida):
        log("instance is running.", "Info", instance)
    else:
        log("Instance fail!!!", "Error", instance)
    return instance


def log(msg: str, stav: str, object):
    match stav:
        case "Error":
            logging.error("%s %s", msg, object)
        case "Info":
            logging.info("%s %s", msg, object)


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
