from clockFragment import *
import tkinter as tk

class Clock:

    def __init__(self, root):
        self.fragments = []
        for i in range(6):
            self.fragments.append(ClockFragment())

        self.root = root
        self.w = root.winfo_width()
        self.h = root.winfo_height()
        self.canvas = tk.Canvas(root, width=self.w, height=self.h, borderwidth=0, highlightthickness=0,
                   bg="#575D90")
        self.canvas.place(x = 0, y = 0, width = self.w, height = self.h)
        def _create_circle(self, x, y, r, **kwargs):
            return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
        tk.Canvas.create_circle = _create_circle

        self.lableW = 50
        self.labelOffset = 10
        self.offsetW = 30
        self.offsetH = 10

        self.label = tk.Label(root, bg = "#575D90", fg="#E6F14A")
        self.label.config(font=("Robotic", 44))
        #self.label['bg']='red'
        self.label.place(x = 0, y = self.h - self.lableW - self.labelOffset, width = self.w, height = self.lableW)       

    def update(self, time):
        if(self.recalc(time)):
            self.show(time)

    def recalc(self, time):
        updated = False
        i = 0
        for fragment in self.fragments:
            if(i == 2 or i == 5):
                i += 1
            if(fragment.setNum(int(time[i]))):
                updated = True
            i += 1
        return updated


    def show(self, time):
        fragmentW = (self.w - 2 * self.offsetW) / len(self.fragments)
        fragmentH = self.h - self.lableW - 2 * self.offsetH
        circleSize = min(fragmentW, fragmentH / 4) * 0.9

        for i in range(len(self.fragments)):
            for k in range(4):
                curFill = "#E6F14A"
                if(self.fragments[i].bits[3 - k] == 0):
                    curFill = "#575D90"
                self.canvas.create_circle(self.offsetW + fragmentW * i + circleSize / 2, self.offsetH + k * (fragmentH / 4) + circleSize / 2, circleSize / 2, fill=curFill, outline="#74CC0A", width=3)

        self.label["text"] = time
