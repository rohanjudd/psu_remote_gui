import numpy as np
import time
import tkinter as tk

#import matplotlib
#matplotlib.use('TkAgg')

#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import matplotlib.pyplot as plt

from psu import PSU

psu = PSU()

root = tk.Tk()

#fig = plt.figure(1)
#plt.ion()
#plt.margins(0)
#plt.title("SSR Test")
#plt.xlabel('Voltage(V)')
#plt.ylabel('Current (A)')
#plt.axis([2, 4, 0, 11])


#canvas = FigureCanvasTkAgg(fig, master=root)
#plot_widget = canvas.get_tk_widget()

def connect():
    if not psu.connect():
        print("Not Connected")

def disconnect():
    psu.disconnect()

def turn_on():
    psu.turn_on()

def turn_off():
    psu.turn_off()

def get_id():
    print(psu.get_id())

def ramp_up():
    psu.start_ramp(2.2, 3.8, 0.1, 0.04)
    #plt.plot(list(psu.results.keys()), list(psu.results.values()))
    #fig.canvas.draw()

def ramp_down():
    psu.start_ramp(3.8, 3.2, -0.1, 0.04)
    #plt.plot(list(psu.results.keys()), list(psu.results.values()))
    #fig.canvas.draw()

def set_voltage_6_8():
    psu.turn_off()
    time.sleep(0.2)
    psu.set_voltage(6.8)
    time.sleep(0.2)
    psu.turn_on()

def set_voltage_13():
    psu.turn_off()
    time.sleep(0.2)
    psu.set_voltage(13)
    time.sleep(0.2)
    psu.turn_on()

def set_voltage_18_2():
    psu.turn_off()
    time.sleep(0.2)
    psu.set_voltage(18.2)
    time.sleep(0.2)
    psu.turn_on()

def close():
    psu.disconnect()
    exit()

#plot_widget.pack()
label = tk.Label(root, text="PSU Remote")
label.pack(pady=10, padx=10)
tk.Button(root,text="Connect",command=connect).pack()
tk.Button(root,text="Disconnect",command=disconnect).pack()
tk.Button(root,text="Turn On",command=turn_on).pack()
tk.Button(root,text="Turn Off",command=turn_off).pack()
tk.Button(root,text="6.8V",command=set_voltage_6_8).pack()
tk.Button(root,text="13.0V",command=set_voltage_13).pack()
tk.Button(root,text="18.2V",command=set_voltage_18_2).pack()
#tk.Button(root,text="ramp",command=ramp_up).pack()
tk.Button(root,text="Exit",command=close).pack()
root.mainloop()
