
import tkinter as tk
from tkinter import ttk
import numpy as np


class Imagen(tk.Frame):
    f = 0
    c = 0
    mimatriz = np.zeros((10, 10))
    filtrada = np.zeros((10, 10))

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.count = 0

        self.button = ttk.Button(self, text="Filtro Derivada", command=self.click)
        self.label = tk.Label(self, text="", width=20)

        self.label.pack(side="top", fill="both", expand=True)
        self.button.pack(side="bottom", padx=4, pady=4)

        self.python_image = tk.PhotoImage(file="lenna.png")
        ttk.Label(self, image=self.python_image).pack()

        self.f = self.python_image.height()
        self.c = self.python_image.width()
        self.mimatriz = np.zeros((self.f, self.c))
        self.filtrada = np.zeros((self.f, self.c))

        self.refresh_clicks()

    def SetPixelText(self, colour, x, y):
        self.python_image.put(colour, (x, y))

    def SetPixel(self, r, g, b, x, y):
        mycolor = "#%02x%02x%02x" % (r, g, b)
        self.python_image.put(mycolor, (x, y))

    def Grises(self):
        for x in range(self.f):
            for y in range(self.c):
                micol = self.python_image.get(x, y)
                gris = int((micol[0]+micol[1]+micol[2])/3)
                self.mimatriz[x][y] = gris
                self.SetPixel(gris, gris, gris, x, y)
                
    def Filtro_Derivada(self):
        # filtro derivada     
        kernel=np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
        print(kernel[1][2])
        for x in range(self.f):
            for y in range(self.c):
                micol = self.python_image.get(x, y)
                r = 255-micol[0]
                g = 255-micol[1]
                b = 255-micol[2]
                self.SetPixel(r, g, b, x, y)
                
                

    def click(self):
        self.count += 1
        self.refresh_clicks()
        self.Filtro_Derivada()

    def refresh_clicks(self):
        self.label.configure(text=f"Clicks: {self.count}")
        
          
apps = []
n = 2
for i in range(n):
    window = tk.Tk() if i == 0 else tk.Toplevel()

    app = Imagen(window)
    app.pack(fill="both", expand=True)
    if i == 0:
        app.Grises()
    apps.append(app)
tk.mainloop()
