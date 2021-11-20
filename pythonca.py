import pyttsx3
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image 

# while (True):
        # texttospeech.say("What Do you want to convert to speech")
def inputAudio(): 
    texttospeech=pyttsx3.init()       
    # answer1=input("Enter Text here ")
    texttospeech.say(getData.get())
    answer = texttospeech.say("do you want to continue then enter some more text otherwise press exit") 
    texttospeech.runAndWait()
    clean()                


def clean():
    getData.set('')

if __name__ == "__main__":
    # inputAudio()
    root=tk.Tk()
    getData = StringVar()
    texttospeech=pyttsx3.init()
    # texttospeech.say("Enter the sentace that you want to convert into speech") 
    texttospeech.runAndWait()
    root.geometry("600x500")
    root.title("Text to speech")
    lbl = Label(root,text = "Text to speech Program",font=('Poppins bold', 30))
    lbl.pack(pady=5)  
    path1 = "voice.png"
    img = (Image.open(path1))
    img = img.resize((150, 150), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(img)
    panel = tk.Label(root, image = new_image)
    panel.pack(side = "top", fill = "both")

    entery1 = Label(root,text  = "Enter your Sentance here",font=('sans', 20))
    entery1.pack(padx=20,pady=20)
    textentry=Entry(root,width=20,bg="white",font=('sans', 20),textvariable=getData)
    textentry.pack()
    
    cnvbtn = Button(root,text="Convert",bg="yellow",command=inputAudio,width=20)
    cnvbtn.pack(pady=30)
    exit_button = Button(root, text="Exit", command=root.destroy,bg="red",width=15)
    exit_button.pack(side='top')
    # textentry.grid(row=1,column=0,sticky=W)
    #Runs the application until we close
    root.mainloop()