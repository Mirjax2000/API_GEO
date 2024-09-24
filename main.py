from turtle import update
import typing

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.style import Bootstyle

import config as conf


class App(ttk.Window):
    def __init__(self) -> None:
        super().__init__(themename='darkly')
        conf.app_init(self, 'API_GEO', 1024,768)
        self.menubar: Menubar = conf.run_and_control(self,Menubar)

        self.rowconfigure(0, weight=0, uniform='a')
        self.columnconfigure(0, weight=1, uniform='a')
        


class Menubar(ttk.Frame):
    def __init__(self, parent) -> None:
        self.parent: typing.Any = parent
        super().__init__(parent,style="primary")
        self.grid(row=0, column=0, sticky=NSEW)

       
 
       
        


        self.update_idletasks()
        

if __name__ == '__main__':
    app:App = App()
    app.mainloop()
