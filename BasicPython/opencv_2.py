import tkinter as tk
from tkinter import ttk


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.count = 0
        self.button = tk.Button(self, text="Click me!", command=self.click)
        self.label = tk.Label(self, text="", width=20)

        self.label.pack(side="top", fill="both", expand=True)
        self.button.pack(side="bottom", padx=4, pady=4)
        self.python_image = tk.PhotoImage(file='lenna.png')
        ttk.Label(self, image=self.python_image).pack()
        self.refresh_clicks()

    def SetPixelText(self, colour, x, y):
        self.python_image.put(colour, (x, y))

    def SetPixel(self, r, g, b, x, y):
        mycolor = "#%02x%02x%02x" % (r, g, b)
        self.python_image.put(mycolor, (x, y))

    def click(self):
        self.count += 1
        self.refresh_clicks()

    def refresh_clicks(self):
        self.label.configure(text=f"Clicks: {self.count}")


apps = []
n = 3
for i in range(n):
    window = tk.Tk() if i == 0 else tk.Toplevel()

    app = App(window)
    app.pack(fill="both", expand=True)
    if i == 0:
        for j in range(100):
            app.SetPixel(255, 0, 0, 10+j, 10)
    if i == 1:
        for j in range(100):
            app.SetPixel(0, 255, 0, 10+j, 10)
    if i == 2:
        for j in range(100):
            app.SetPixel(0, 0, 255, 10+j, 10)
    apps.append(app)
tk.mainloop()
