# -*- coding: utf-8 -*-

import tkinter as tk
from database import creat_database
from main_menu_ import main_menu
import tkinter.font as tkFont

if __name__ == "__main__":

    name_db = "resources/database/StudyLoad.db"

    creat_database(name_db)

    root = tk.Tk()
    root.geometry("2000x1000+0+0")

    big_font = tkFont.Font(family="Times New Roman", size=22)
    root.option_add("*Button.Font", big_font)
    root.option_add("*Label.Font", big_font)
    root.option_add("*Entry.Font", big_font)


    try:
        root.iconbitmap(r'resources/img/icon/icon.ico')
    except Exception:
        i=1
    root.deiconify()

    main_menu(root,name_db)

# pyinstaller --onefile --windowed --icon=resources/img/icon/icon.ico main.py