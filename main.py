import tkinter as tk
from tkinter.filedialog import askopenfile
import pandas as pd
import numpy as np

data = pd.ExcelFile("leer.xlsx")
x = pd.read_excel(data)
filex = pd.read_excel(data)

root = tk.Tk()

def klick(x):
    print(x)

def einlesen():
    excelfile = askopenfile(parent=root, mode="rb", title="Wähle Excel-Datei.", filetype=[("Excel file", "*.xlsx")])
    if excelfile:
        data = pd.ExcelFile(excelfile)
        file = pd.read_excel(data)
        textbox.insert(1.0, file)

        # Einzelne Spalten auslesen
        name = file.get("Name")
        verbrauch = file.get("Verbrauch / Liter")
        kilometer = file.get("Kilometer")

        # Den Verbrauch in l/100km umrechnen
        l_100km = []
        for i in range(0, verbrauch.size):
            result = verbrauch.get(i) / kilometer.get(i) * 100
            result = round(result, 3)
            l_100km.append(result)

        # Den Verbrauch aufsteigend sortieren
        sorted_index = np.argsort(l_100km)
        sorted = np.sort(l_100km)

        # Die Namen passend zum Verbrauch sortieren
        names_sort = []
        for i in sorted_index:
            names_sort.append(name.get(i))

        final_array = np.array([names_sort, sorted])
        textbox_best.insert(1.0, final_array[0][0] + " mit einem Verbrauch von " + final_array[1][0] + " l/100km!")

        return file

canvas = tk.Canvas(root, width=1000, height=500)
canvas.grid(columnspan=3, rowspan=6)

title = tk.Label(root, text="Auswertung einer Excel-Tabelle" "\n" "- Niedrigster Spritverbrauch")
title.grid(column=1, row=0)

instructions = tk.Label(root, text="Wähle eine Excel-Datei aus:")
instructions.grid(column=0, row=1)

browse_btn = tk.Button(root, text="Browse", command=lambda x=filex:einlesen(), bg="#20bebe", fg="white", width=15, height=2)
browse_btn.grid(column=0, row=2)

klick_btn = tk.Button(root, text="Klick", command=lambda:klick(x), bg="#20bebe", fg="white", width=15, height=2)
klick_btn.grid(column=0, row=3)

textbox = tk.Text(width=80, height=20, padx=15, pady=15)
textbox.grid(column=1, row=1, rowspan=2)

best = tk.Label(root, text="Der Fahrer mit dem niedrigsten Verbrauch:")
best.grid(column=1, row=4)

textbox_best = tk.Text(width=80, height=1, padx=15, pady=15)
textbox_best.grid(column=1, row=5)

root.mainloop()