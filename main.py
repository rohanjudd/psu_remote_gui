# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

import time
import string
import config
from psu import PSU

psu = PSU()


class PSU_Remote(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "PSU Remote")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, ActionPage, GraphPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PSU Remote", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Connect",
                            command=lambda: self.connect())
        button.pack()

    def connect(self):
        if psu.connect():
            self.controller.show_frame(ActionPage)
        else:
            self.controller.show_frame(ActionPage)


class ActionPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PSU Remote", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Turn On",
                            command=lambda: psu.turn_on())
        button.pack()

        button2 = ttk.Button(self, text="Turn Off",
                             command=lambda: psu.turn_off())
        button2.pack()

        button3 = ttk.Button(self, text="Ramp",
                             command=lambda: self.start_ramp())
        button3.pack()

    def start_ramp(self):
        psu.start_ramp(2,3.9,0.1,0.1)
        command=lambda: GraphPage.update()
        self.controller.show_frame(GraphPage)


class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize=(5, 5), dpi=100)
        self.a = f.add_subplot(111)
        self.a.plot(list(psu.results.keys()),list(psu.results.values()))


        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def update(self):
        self.a.plot(list(psu.results.keys()), list(psu.results.values()))
        self.canvas.show()
        print(psu.results)



app = PSU_Remote()
app.mainloop()
