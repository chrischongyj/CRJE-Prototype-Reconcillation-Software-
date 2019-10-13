import tkinter as tk
from tkinter import filedialog
import os, time
from stat import ST_SIZE, ST_MTIME


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    st = os.stat(filename)
    filesize = "File size: " + str(st[ST_SIZE]/1000) + " kB"

    lastmodified = "Last modified: " + str(time.asctime(time.localtime(st[ST_MTIME])))

    label = tk.Label(text=filesize)
    label.place(relx = 0.05, rely = 0.5)

    label2 = tk.Label(text=lastmodified)
    label2.place(relx=0.05, rely=0.55)

    label3 = tk.Label(text="Uploaded Successfully!")
    label3.place(relx=0.05, rely=0.3)

def UploadAction2(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    st = os.stat(filename)
    filesize = "File size: " + str(st[ST_SIZE]/1000) + " kB"

    lastmodified = "Last modified: " + str(time.asctime(time.localtime(st[ST_MTIME])))

    label = tk.Label(text=filesize)
    label.place(relx = 0.55, rely = 0.5)

    label2 = tk.Label(text=lastmodified)
    label2.place(relx=0.55, rely=0.55)

    label3 = tk.Label(text="Uploaded Successfully!")
    label3.place(relx=0.55, rely=0.3)

def viewanalysis():
        frame2 = tk.Frame(canvas, bg='lightyellow', height=HEIGHT, width=WIDTH)
        frame2.pack()

        label = tk.Label(frame2, text="Current Assets ✓")
        label.place(relx=0.35, rely=0.2)

        label2 = tk.Label(frame2, text="Investments ✓")
        label2.place(relx=0.35, rely=0.25)

        label3 = tk.Label(frame2, text="Property, Plant and Equipment ✓")
        label3.place(relx=0.35, rely=0.3)

        label4 = tk.Label(frame2, text="Intangible Assets ✓")
        label4.place(relx=0.35, rely=0.35)
        
        label5 = tk.Label(frame2, text="Other Assets ✓")
        label5.place(relx=0.35, rely=0.4)

        button = tk.Button(frame2, text='Back')
        button.place(relx=0.35, rely = 0.5)

def reconcile():
    time.sleep(2)
    label2 = tk.Label(text="Reconcile PASSED")
    label2.place(relx=0.43, rely=0.8)

    time.sleep(1)

    button = tk.Button(canvas, text='View Analysis', command=viewanalysis)
    button.place(relx=0.44, rely = 0.85)


root = tk.Tk()

HEIGHT = 500
WIDTH = 500 

canvas = tk.Canvas(height=HEIGHT, width=WIDTH, bg='lightblue')
canvas.pack()


button = tk.Button(canvas, text='Upload Balance Sheet', command=UploadAction)
button.place(relx=0.2, rely=0.1)

button2 = tk.Button(canvas, text='Upload Source Documents', command=UploadAction2)
button2.place(relx=0.5, rely = 0.1)

button3 = tk.Button(canvas, text='Reconcile', command=reconcile)
button3.place(relx=0.45, rely = 0.65)

button4 = tk.Button(canvas, text='Save to Cloud')
button4.place(relx=0.2, rely = 0.65)

button5 = tk.Button(canvas, text='Reset')
button5.place(relx=0.67, rely = 0.65)



root.mainloop()