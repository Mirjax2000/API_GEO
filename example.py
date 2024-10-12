import customtkinter as ctk
from tkinter import PhotoImage
import tkinter as tk


# Funkce pro otevření nového okna
def open_new_window():
    new_window = ctk.CTkToplevel()  # Vytvoření nového okna
    new_window.title("Nové okno")  # Nastavení názvu nového okna
    new_window.geometry("300x200")  # Nastavení rozměrů nového okna

    # Nastavení ikony nového okna
   

    label = ctk.CTkLabel(new_window, text="Toto je nové okno")
    label.pack(pady=20)

    close_button = ctk.CTkButton(new_window, text="Zavřít", command=new_window.destroy)
    close_button.pack(pady=10)


# Hlavní aplikace
app = ctk.CTk()
app.title("Hlavní aplikace")
app.geometry("400x300")


open_window_button = ctk.CTkButton(
    app, text="Otevřít nové okno", command=open_new_window
)
open_window_button.pack(pady=20)

app.mainloop()
