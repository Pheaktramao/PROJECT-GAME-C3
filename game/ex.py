#________________________IMPORT FILES______________________
from tkinter import *
from PIL import ImageTk, Image
#_________________________CONSTANTS________________________
WINDOW_WIDTH=1420
WINDOW_HEIGHT=800
#_____________________GLOBAL____________
score=0

#________________MAIN WINDOW________________
window=Tk()
window.geometry(str(WINDOW_WIDTH)+ "x" + str(WINDOW_HEIGHT))
window.title("HANUMAN JUMP")
frame=Frame()
canvas=Canvas(frame)

#____________IMPORT IMAGES____________
bg_default=PhotoImage(file="IMAGE/game_bg.jpg")
#______________HOME PAGE___________
def home():
    canvas.create_image(1,0,image=bg_default,anchor="nw")
window.mainloop()