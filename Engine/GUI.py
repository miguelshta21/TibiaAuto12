import pyautogui
import tkinter as tk
from PIL import Image, ImageTk

from Engine.Defaults import *

rgb = Defaults()


class GUI:
    def __init__(self, windowID, name):
        self.windowID = windowID
        self.name = name

    def MainWindow(self, size):
        screenSize = pyautogui.size()
        size = [f'{int(size[0])}', f'{int(size[1])}']
        locationOfSpawnWindow = [(screenSize[0] - int(size[0])) / 2,
                                 (screenSize[1] - int(size[1])) / 2.36]
        self.windowID = tk.Tk()
        self.windowID.title(self.name)
        self.windowID.geometry(
            '%dx%d+%d+%d' % (int(size[0]), int(size[1]), locationOfSpawnWindow[0], locationOfSpawnWindow[1]))
        self.windowID.resizable(width=False, height=False)
        self.windowID.configure(background='#000', takefocus=True)

    def DefaultWindow(self, BackgroundImage):
        self.windowID = tk.Toplevel()
        self.windowID.focus_force()
        self.windowID.grab_set()
        w = 348
        h = 546
        sw = self.windowID.winfo_screenwidth()
        sh = self.windowID.winfo_screenheight()
        x = (sw - w) / 1.325
        y = (sh - h) / 2.36
        self.windowID.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.windowID.title(self.name)
        self.windowID.resizable(width=False, height=False)
        self.windowID.configure(background='#000', takefocus=True)
        image = Image.open('images/' + BackgroundImage + '.jpg')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.windowID, image=photo, bg='#000')
        label.image = photo
        label.pack()

    def loop(self):
        self.windowID.mainloop()
    
    def destroyWindow(self):
        self.windowID.destroy()

    def addButton(self, textOfButton, action, sizes, bgColor, aBgColor):
        buttonID = tk.Button(self.windowID,
                             text=textOfButton,
                             font=('Microsoft Sans Serif', 10),
                             bg=rgb.rgb((bgColor[0], bgColor[1], bgColor[2])),
                             fg='white',
                             command=action,
                             activebackground=rgb.rgb((aBgColor[0], aBgColor[1], aBgColor[2])))
        buttonID.place(w=sizes[0], h=sizes[1], x=sizes[2], y=sizes[3])
        return buttonID

    def addCheck(self, variable, position, bgColor, selected, textOfButton="", image=None):
        buttonID = tk.Checkbutton(self.windowID,
                                  bg=rgb.rgb((bgColor[0], bgColor[1], bgColor[2])),
                                  text=textOfButton,
                                  variable=variable,
                                  onvalue=True,
                                  offvalue=False,
                                  image=image)
        buttonID.place(x=position[0], y=position[1])
        if selected == 1:
            buttonID.select()
        else:
            buttonID.deselect()

    def addLabel(self, textOfLabel, bgColor, position):
        labelID = tk.Label(self.windowID,
                           text=textOfLabel,
                           bg=rgb.rgb((bgColor[0], bgColor[1], bgColor[2])),
                           fg='white')
        labelID.place(x=position[0], y=position[1])
        return labelID

    def addEntry(self, position):
        entryID = tk.Entry(self.windowID)
        entryID.place(x=position[0], y=position[1])
        return entryID

