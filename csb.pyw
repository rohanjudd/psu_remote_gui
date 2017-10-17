
import time
import tkinter as tk

from psu import PSU

psu = PSU()
root = tk.Tk()

root.minsize(width=180, height = 200)

def connect():
    if not psu.connect():
        print("Not Connected")
    else:
        set_voltage(0)
        set_label("green", "ON")


def disconnect():
    psu.disconnect()

def turn_on():
    psu.turn_on()
    #set_label("green", "ON")

def turn_off():
    psu.turn_off()
    set_label("red", "OFF")
    root.update()

def get_id():
    print(psu.get_id())

def set_voltage(v):
    psu.set_voltage(v)
    set_label("green", "{:.2f}".format(v))

def reset_to_voltage(v):
    turn_off()
    time.sleep(0.2)
    set_voltage(v)
    time.sleep(0.2)
    turn_on()

def delayed_reset(s):
    turn_off()
    set_label("red", "READY?")
    root.update()
    time.sleep(s)
    turn_on()
    set_label("yellow", "NOW")

def startup_voltage_test():
    reset_to_voltage(6.8)
    root.update()
    time.sleep(2)
    reset_to_voltage(18.2)
    root.update()
    time.sleep(2)
    reset_to_voltage(13)

def set_label(col, t):
    indicator.config(bg=col, text=t)

def close():
    psu.disconnect()
    exit()

tk.Label(root, text="PSU Remote").pack(pady=5, padx=20)
indicator = tk.Label(root, text="Not Connected", bg="grey", fg="black", font=("Helvetica", 16))
indicator.pack(fill=tk.X, pady=5)
tk.Button(root,text="Connect",command= lambda: connect()).pack(fill=tk.X, padx= 2)
tk.Button(root,text="Disconnect",command= lambda: disconnect()).pack(fill=tk.X, padx= 2)
tk.Label(root).pack()
tk.Button(root,text="ON",command= lambda: turn_on()).pack(fill=tk.X, padx= 2)
tk.Button(root,text="OFF",command= lambda: turn_off()).pack(fill=tk.X, padx= 2)
tk.Label(root).pack()
tk.Button(root,text="Delayed Reset",command= lambda: delayed_reset(3)).pack(fill=tk.X, padx= 2)
tk.Label(root).pack()
tk.Button(root,text="Startup Voltage Test",command= lambda: startup_voltage_test()).pack(fill=tk.X, padx= 2)
tk.Label(root).pack()
tk.Button(root,text="6.8 V",command= lambda: reset_to_voltage(6.8)).pack(fill=tk.X, padx= 2)
tk.Button(root,text="13.0 V",command= lambda: reset_to_voltage(13)).pack(fill=tk.X, padx= 2)
tk.Button(root,text="18.2 V",command= lambda: reset_to_voltage(18.2)).pack(fill=tk.X, padx= 2)
tk.Label(root).pack()
tk.Button(root,text="Exit",command= lambda: close()).pack(fill=tk.X, padx= 2)
root.mainloop()
