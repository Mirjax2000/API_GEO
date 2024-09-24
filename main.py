import tkinter as tk
import config as conf

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class App(ttk.Window):
    def __init__(self) -> None:
        super().__init__(themename='darkly')
        conf.app_init(self, 'API_GEO', 1024,768)


class Menubar(ttk.Frame):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent,style="")


if __name__ == '__main__':
    app:App = App()
    app.mainloop()
