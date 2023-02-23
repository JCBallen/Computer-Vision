import tkinter as tk
from tkinter import ttk


class Imagen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Computer Vision First Example')
        # self.geometry('320x150')

        self.python_image = tk.PhotoImage(file='lenna.png')
        ttk.Label(self, image=self.python_image).pack()

    def tam(self):
        print('image size')
        print(self.python_image.height())
        print(self.python_image.width())

    def GetPixel(self, x, y):
        return self.python_image.get(x, y)

    def SetPixelText(self, colour, x, y):
        self.python_image.put(colour, (x, y))

    def SetPixel(self, r, g, b, x, y):
        mycolor = '#%02x%02x%02x' % (r, g, b)
        self.python_image.put(mycolor, (x, y))


app = Imagen()

app.tam()
print(app.GetPixel(19, 10))
# app.SetPixel('#FF0000',10,10)
app.SetPixel(255, 255, 255, 10, 10)
app.mainloop()
