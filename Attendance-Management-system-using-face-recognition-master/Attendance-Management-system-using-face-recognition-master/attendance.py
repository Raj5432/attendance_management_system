import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

# project module
import show_attendance
import takeImage
import trainImage
import automaticAttedance

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = "./TrainingImageLabel/Trainner.yml"
trainimage_path = "./TrainingImage"
if not os.path.exists(trainimage_path):
    os.makedirs(trainimage_path)

# ✅ Corrected path to your student details CSV
studentdetail_path = "C:/Users/yamala raju/Documents/student details.csv"

attendance_path = "Attendance"

window = Tk()
window.title("Face Recognizer")
window.geometry("1280x720")
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
window.configure(background="#1c1c1c")

def del_sc1():
    sc1.destroy()

def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.title("Warning!!")
    sc1.configure(background="#1c1c1c")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="yellow",
        bg="#1c1c1c",
        font=("Verdana", 16, "bold"),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="yellow",
        bg="#333333",
        width=9,
        height=1,
        activebackground="red",
        font=("Verdana", 16, "bold"),
    ).place(x=110, y=50)

def testVal(inStr, acttyp):
    if acttyp == "1":
        if not inStr.isdigit():
            return False
    return True

logo = Image.open("UI_Image/0001.png")
logo = logo.resize((50, 47), Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="#1c1c1c", relief=RIDGE, bd=10, font=("Verdana", 30, "bold"))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="#1c1c1c")
l1.place(x=470, y=10)

titl = tk.Label(window, text="CLASS VISION", bg="#1c1c1c", fg="yellow", font=("Verdana", 27, "bold"))
titl.place(x=525, y=12)

a = tk.Label(
    window,
    text="Welcome to CLASS VISION",
    bg="#1c1c1c",
    fg="yellow",
    bd=10,
    font=("Verdana", 35, "bold"),
)
a.pack()

ri = Image.open("UI_Image/register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=100, y=270)

ai = Image.open("UI_Image/attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=980, y=270)

vi = Image.open("UI_Image/verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=600, y=270)

def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="#1c1c1c")
    ImageUI.resizable(0, 0)

    titl = tk.Label(ImageUI, bg="#1c1c1c", relief=RIDGE, bd=10, font=("Verdana", 30, "bold"))
    titl.pack(fill=X)
    titl = tk.Label(ImageUI, text="Register Your Face", bg="#1c1c1c", fg="green", font=("Verdana", 30, "bold"))
    titl.place(x=270, y=12)

    a = tk.Label(ImageUI, text="Enter the details", bg="#1c1c1c", fg="yellow", bd=10, font=("Verdana", 24, "bold"))
    a.place(x=280, y=75)

    lbl1 = tk.Label(ImageUI, text="Enrollment No", width=10, height=2, bg="#1c1c1c", fg="yellow", bd=5, relief=RIDGE, font=("Verdana", 14))
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(ImageUI, width=17, bd=5, validate="key", bg="#333333", fg="yellow", relief=RIDGE, font=("Verdana", 18, "bold"))
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    lbl2 = tk.Label(ImageUI, text="Name", width=10, height=2, bg="#1c1c1c", fg="yellow", bd=5, relief=RIDGE, font=("Verdana", 14))
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(ImageUI, width=17, bd=5, bg="#333333", fg="yellow", relief=RIDGE, font=("Verdana", 18, "bold"))
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(ImageUI, text="Notification", width=10, height=2, bg="#1c1c1c", fg="yellow", bd=5, relief=RIDGE, font=("Verdana", 14))
    lbl3.place(x=120, y=270)
    message = tk.Label(ImageUI, text="", width=32, height=2, bd=5, bg="#333333", fg="yellow", relief=RIDGE, font=("Verdana", 14, "bold"))
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    takeImg = tk.Button(ImageUI, text="Take Image", command=take_image, bd=10, font=("Verdana", 18, "bold"), bg="#333333", fg="yellow", height=2, width=12, relief=RIDGE)
    takeImg.place(x=130, y=350)

    def train_image():
        trainImage.TrainImage(haarcasecade_path, trainimage_path, trainimagelabel_path, message, text_to_speech)

    trainImg = tk.Button(ImageUI, text="Train Image", command=train_image, bd=10, font=("Verdana", 18, "bold"), bg="#333333", fg="yellow", height=2, width=12, relief=RIDGE)
    trainImg.place(x=360, y=350)

r = tk.Button(window, text="Register a new student", command=TakeImageUI, bd=10, font=("Verdana", 16), bg="black", fg="yellow", height=2, width=17)
r.place(x=100, y=520)

def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)

r = tk.Button(window, text="Take Attendance", command=automatic_attedance, bd=10, font=("Verdana", 16), bg="black", fg="yellow", height=2, width=17)
r.place(x=600, y=520)

def view_attendance():
    show_attendance.subjectchoose(text_to_speech)

r = tk.Button(window, text="View Attendance", command=view_attendance, bd=10, font=("Verdana", 16), bg="black", fg="yellow", height=2, width=17)
r.place(x=1000, y=520)

r = tk.Button(window, text="EXIT", command=quit, bd=10, font=("Verdana", 16), bg="black", fg="yellow", height=2, width=17)
r.place(x=600, y=660)

window.mainloop()
