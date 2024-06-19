import tkinter as tk
import playsound as p


def amoung_us(event):
    p.playsound("among_us_sound.mp3")


def bruh_v1(event):
    p.playsound("bruh_sound_effect_v1.mp3")

def bruh_v2(event):
    p.playsound("bruh_sound_effect_v2.mp3")


def bruh_v3(event):
    p.playsound("bruh_sound_effect_v3.mp3")

def no_wayyy(event):
    p.playsound("no_wayyyyy.mp3")

def rizz(event):
    p.playsound("rizz_sound_effect.mp3")

def skylar(event):
    p.playsound("skylar.mp3")

win = tk.Tk()
win.attributes('-topmost',True)
l1 = tk.Label(win,text="This button has an event bound by a command")


b1 =  tk.Button(win,text="AMOUNG US!!!",command="playsound")
b1.bind("<Button>",amoung_us)

b2 =  tk.Button(win,text="bruh effect 1",command="playsound")
b2.bind("<Button>",bruh_v1)

b3 =  tk.Button(win,text="bruh effect 2",command="playsound")
b3.bind("<Button>",bruh_v2)

b4 =  tk.Button(win,text="bruh effect 3",command="playsound")
b4.bind("<Button>",bruh_v3)

b5 =  tk.Button(win,text="rizz",command="playsound")
b5.bind("<Button>",rizz)

b6 =  tk.Button(win,text="skylar",command="playsound")
b6.bind("<Button>",skylar)

b7 =  tk.Button(win,text="no_wayyyyy",command="playsound")
b7.bind("<Button>",no_wayyy)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()

win.mainloop()