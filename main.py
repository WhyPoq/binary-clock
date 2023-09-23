import datetime
import tkinter as tk
from clock import *
import threading

closed = False

def main():
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", close)
    root.title("Counting Seconds")
    root.geometry("500x400") 
    root.resizable(False, False) 

    root.update()

    timer = Clock(root)

    while(closed == False):       
        timer.update(datetime.datetime.now().time().strftime("%H:%M:%S"))
        root.update()

    root.destroy(); 
    print("ended")

def close():
    global closed
    closed = True

if __name__ == '__main__':
    main()