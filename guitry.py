import numpy as np
import tkinter as tk

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from psu import PSU

psu = PSU()

root = tk.Tk()

fig = plt.figure(1)
plt.ion()
plt.margins(0)
plt.title("SSR Test")
plt.xlabel('Voltage(V)')
plt.ylabel('Current (A)')
#plt.plot([0],[0])


canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()

def connect():
    if not psu.connect():
        print("Not Connected")

def ramp():
    psu.start_ramp(2, 3.9, 0.1, 0.1)
    plt.plot(list(psu.results.keys()), list(psu.results.values()))
    fig.canvas.draw()

plot_widget.pack()
label = tk.Label(root, text="PSU Remote")
label.pack(pady=10, padx=10)
tk.Button(root,text="Connect",command=connect).pack()
tk.Button(root,text="Ramp",command=ramp).pack()
root.mainloop()