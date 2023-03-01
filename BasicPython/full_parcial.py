
# PARCIAL JUAN BALLEN 1202151
# IR DESCOMENTANDO PUNTO A PUNTO



# ==================================
# ======= PUNTO 1 ===========
# ==================================



# import tkinter as tk
# from tkinter import ttk


# class Imagen(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title('Computer Vision First Example')
#         # self.geometry('320x150')

#         self.python_image = tk.PhotoImage(file='lenna.png')
#         ttk.Label(self, image=self.python_image).pack()

#     def tam(self):
#         print('image size')
#         print(self.python_image.height())
#         print(self.python_image.width())

#     def GetPixel(self, x, y):
#         return self.python_image.get(x, y)

#     def SetPixelText(self, colour, x, y):
#         self.python_image.put(colour, (x, y))

#     def SetPixel(self, r, g, b, x, y):
#         mycolor = '#%02x%02x%02x' % (r, g, b)
#         self.python_image.put(mycolor, (x, y))


# app = Imagen()

# app.tam()
# print(app.GetPixel(19, 10))
# # app.SetPixel('#FF0000',10,10)
# app.SetPixel(255, 255, 255, 10, 10)
# app.mainloop()



# ==================================
# =========== PUNTO 2 ==============
# ==================================



# import tkinter as tk
# from tkinter import ttk
# import numpy as np


# class App(tk.Frame):
#     f = 0
#     c = 0
#     mimatriz = np.zeros((10, 10))

#     def __init__(self, parent, *args, **kwargs):
#         super().__init__(parent, *args, **kwargs)
#         self.count = 0
#         self.button = tk.Button(self, text="Click me!", command=self.click)
#         self.label = tk.Label(self, text="", width=20)

#         self.label.pack(side="top", fill="both", expand=True)
#         self.button.pack(side="bottom", padx=4, pady=4)
#         self.python_image = tk.PhotoImage(file='lenna.png')
#         ttk.Label(self, image=self.python_image).pack()

#         self.f = self.python_image.height()
#         self.c = self.python_image.width()
#         self.mimatriz = np.zeros((self.f, self.c))

#         self.refresh_clicks()

#     def SetPixelText(self, colour, x, y):
#         self.python_image.put(colour, (x, y))

#     def SetPixel(self, r, g, b, x, y):
#         mycolor = "#%02x%02x%02x" % (r, g, b)
#         self.python_image.put(mycolor, (x, y))

#     def Grises(self):
#         for x in range(self.f):
#             for y in range(self.c):
#                 micol = self.python_image.get(x, y)
#                 gris = int((micol[0]+micol[1]+micol[2])/3)
#                 self.mimatriz[x][y] = gris
#                 self.SetPixel(gris, gris, gris, x, y)
#                 # print(micol)

#     def click(self):
#         self.count += 1
#         self.refresh_clicks()

#     def refresh_clicks(self):
#         self.label.configure(text=f"Clicks: {self.count}")

# apps = []
# n = 1
# for i in range(n):
#     window = tk.Tk() if i == 0 else tk.Toplevel()

#     app = App(window)
#     app.pack(fill="both", expand=True)
#     if i == 0:
#         for j in range(100):
#             app.SetPixel(255, 0, 0, 10+j, 10)
#         app.Grises()
#     if i == 1:
#         for j in range(100):
#             app.SetPixel(0, 255, 0, 10+j, 10)
#         app.Grises()
#     if i == 2:
#         for j in range(100):
#             app.SetPixel(0, 0, 255, 10+j, 10)
#         app.Grises()
#     apps.append(app)
# tk.mainloop()



# ==================================
# ============ PUNTO 3 =============
# ==================================



# import tkinter as tk
# from tkinter import ttk
# import numpy as np


# class Imagen(tk.Frame):
#     f = 0
#     c = 0
#     mimatriz = np.zeros((10, 10))
#     filtrada = np.zeros((10, 10))

#     def __init__(self, parent, *args, **kwargs):
#         super().__init__(parent, *args, **kwargs)
#         self.count = 0

#         self.button = ttk.Button(self, text="Grises", command=self.click)
#         self.button1 = ttk.Button(
#             self, text="Filtro Promedio", command=self.click1)
#         self.label = tk.Label(self, text="", width=20)

#         self.label.pack(side="top", fill="both", expand=True)
#         self.button.pack(side="bottom", padx=4, pady=4)
#         self.button1.pack(side="bottom", padx=4, pady=4)

#         self.python_image = tk.PhotoImage(file="lenna.png")
#         ttk.Label(self, image=self.python_image).pack()

#         self.f = self.python_image.height()
#         self.c = self.python_image.width()
#         self.mimatriz = np.zeros((self.f, self.c))
#         self.filtrada = np.zeros((self.f, self.c))

#         self.refresh_clicks()

#     def SetPixelText(self, colour, x, y):
#         self.python_image.put(colour, (x, y))

#     def SetPixel(self, r, g, b, x, y):
#         mycolor = "#%02x%02x%02x" % (r, g, b)
#         self.python_image.put(mycolor, (x, y))

#     def Grises(self):
#         for x in range(self.f):
#             for y in range(self.c):
#                 micol = self.python_image.get(x, y)
#                 gris = int((micol[0]+micol[1]+micol[2])/3)
#                 self.mimatriz[x][y] = gris
#                 self.SetPixel(gris, gris, gris, x, y)
#                 # print(micol)

#     def Promedio(self):
#         for x in range(1, self.c-1):
#             for y in range(1, self.f-1):
#                 p1 = self.mimatriz[x+1][y+1]
#                 p2 = self.mimatriz[x+1][y-1]
#                 p3 = self.mimatriz[x-1][y+1]
#                 p4 = self.mimatriz[x-1][y-1]
#                 p5 = self.mimatriz[x+1][y]
#                 p6 = self.mimatriz[x-1][y]
#                 p7 = self.mimatriz[x][y+1]
#                 p8 = self.mimatriz[x][y-1]
#                 p9 = self.mimatriz[x][y]
#                 p = (p1+p2+p3+p4+p5+p6+p7+p8+p9)/9
#                 self.filtrada[x][y] = p
#                 self.SetPixel(int(p), int(p), int(p), x, y)
#                 # print(micol[0])

#     def click(self):
#         self.count += 1
#         self.refresh_clicks()
#         self.Grises()
        
#     def click1(self):
#         self.count += 1
#         self.refresh_clicks()
#         self.Promedio()

#     def refresh_clicks(self):
#         self.label.configure(text=f"Clicks: {self.count}")
        
          
# apps = []
# n = 3
# for i in range(n):
#     window = tk.Tk() if i == 0 else tk.Toplevel()

#     app = Imagen(window)
#     app.pack(fill="both", expand=True)
#     if i == 0:
#         pass
#     apps.append(app)
# tk.mainloop()



# ==================================
# ========== PUNTO 4 y 5 ===========
# ==================================



# import tkinter as tk
# from tkinter import ttk
# import numpy as np


# class Imagen(tk.Frame):
#     f = 0
#     c = 0
#     mimatriz = np.zeros((10, 10))
#     filtrada = np.zeros((10, 10))

#     def __init__(self, parent, *args, **kwargs):
#         super().__init__(parent, *args, **kwargs)
#         self.count = 0

#         self.button = ttk.Button(self, text="Negativo (B/N y Color)", command=self.click)
#         self.label = tk.Label(self, text="", width=20)

#         self.label.pack(side="top", fill="both", expand=True)
#         self.button.pack(side="bottom", padx=4, pady=4)

#         self.python_image = tk.PhotoImage(file="lenna.png")
#         ttk.Label(self, image=self.python_image).pack()

#         self.f = self.python_image.height()
#         self.c = self.python_image.width()
#         self.mimatriz = np.zeros((self.f, self.c))
#         self.filtrada = np.zeros((self.f, self.c))

#         self.refresh_clicks()

#     def SetPixelText(self, colour, x, y):
#         self.python_image.put(colour, (x, y))

#     def SetPixel(self, r, g, b, x, y):
#         mycolor = "#%02x%02x%02x" % (r, g, b)
#         self.python_image.put(mycolor, (x, y))

#     def Grises(self):
#         for x in range(self.f):
#             for y in range(self.c):
#                 micol = self.python_image.get(x, y)
#                 gris = int((micol[0]+micol[1]+micol[2])/3)
#                 self.mimatriz[x][y] = gris
#                 self.SetPixel(gris, gris, gris, x, y)
                
#     def Negativo(self):        
#         for x in range(self.f):
#             for y in range(self.c):
#                 micol = self.python_image.get(x, y)
#                 r = 255-micol[0]
#                 g = 255-micol[1]
#                 b = 255-micol[2]
#                 self.SetPixel(r, g, b, x, y)
                
                

#     def click(self):
#         self.count += 1
#         self.refresh_clicks()
#         self.Negativo()

#     def refresh_clicks(self):
#         self.label.configure(text=f"Clicks: {self.count}")
        
          
# apps = []
# n = 2
# for i in range(n):
#     window = tk.Tk() if i == 0 else tk.Toplevel()

#     app = Imagen(window)
#     app.pack(fill="both", expand=True)
#     if i == 0:
#         app.Grises()
#     apps.append(app)
# tk.mainloop()




# ==================================
# ============ PUNTO 6 =============
# ==================================



# import tkinter as tk
# from tkinter import ttk
# import numpy as np


# class Imagen(tk.Frame):
#     f = 0
#     c = 0
#     mimatriz = np.zeros((10, 10))
#     filtrada = np.zeros((10, 10))

#     def __init__(self, parent, *args, **kwargs):
#         super().__init__(parent, *args, **kwargs)
#         self.count = 0

#         self.button = ttk.Button(self, text="Brillo (+50)", command=self.click)
#         self.label = tk.Label(self, text="", width=20)

#         self.label.pack(side="top", fill="both", expand=True)
#         self.button.pack(side="bottom", padx=4, pady=4)

#         self.python_image = tk.PhotoImage(file="lenna.png")
#         ttk.Label(self, image=self.python_image).pack()

#         self.f = self.python_image.height()
#         self.c = self.python_image.width()
#         self.mimatriz = np.zeros((self.f, self.c))
#         self.filtrada = np.zeros((self.f, self.c))

#         self.refresh_clicks()

#     def SetPixelText(self, colour, x, y):
#         self.python_image.put(colour, (x, y))

#     def SetPixel(self, r, g, b, x, y):
#         mycolor = "#%02x%02x%02x" % (r, g, b)
#         self.python_image.put(mycolor, (x, y))

#     def Grises(self):
#         for x in range(self.f):
#             for y in range(self.c):
#                 micol = self.python_image.get(x, y)
#                 gris = int((micol[0]+micol[1]+micol[2])/3)
#                 self.mimatriz[x][y] = gris
#                 self.SetPixel(gris, gris, gris, x, y)
                
#     def brillo(self):
#         for x in range(self.f):
#             for y in range(self.c):
#                 micol = self.python_image.get(x, y)
#                 r = micol[0] + 50 if micol[0] + 50 <= 255 else 255
#                 g = micol[1] + 50 if micol[1] + 50 <= 255 else 255
#                 b = micol[2] + 50 if micol[2] + 50 <= 255 else 255
#                 self.SetPixel(r, g, b, x, y)
    


#     def click(self):
#         self.count += 1
#         self.refresh_clicks()
#         self.brillo()

#     def refresh_clicks(self):
#         self.label.configure(text=f"Clicks: {self.count}")
        
          
# apps = []
# n = 3
# for i in range(n):
#     window = tk.Tk() if i == 0 else tk.Toplevel()

#     app = Imagen(window)
#     app.pack(fill="both", expand=True)
#     if i == 0:
#         app.Grises()
#     apps.append(app)
# tk.mainloop()





