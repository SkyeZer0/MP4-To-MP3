from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from moviepy import *

class Converter:
    def __init__(self,window):
        window.geometry("300x100")
        window.title("mp4 to mp3")
        window.resizable(False,False)

        Load = Button(window, width=10, text='Load', font=("arial", 8),command=self.Load)
        Convert = Button(window,width=10, text='Convert', font=('arial',8),command=self.Convert)
        Save = Button(window,width=10, text='Save', font=('arial',8),command=self.Save)
        Save.place(y=50, x=200)
        Load.place(y=50, x=20)
        Convert.place(y=50, x=110)
        self.mp4_file = False
        self.save_file = False
        self.mp3_name = ''

    def Load(self):
        self.mp4_file = filedialog.askopenfilename()

    def Convert(self):
        if (self.mp4_file != False) and (self.save_file != False):
            VidFile= AudioFileClip(self.mp4_file)
            VidFile.write_audiofile(self.mp3_name, bitrate="320k")
        else:
            messagebox.showerror(title = "Error!", message="""Конвертация невозможна по следующим причинам:
1) No mp4 file selected for conversion
2) The file path and name have not been selected
3) both points are not fulfilled""")


    def Save(self):
        self.save_file = filedialog.asksaveasfilename()
        self.mp3_name = str(self.save_file)
        self.mp3_name += ".mp3"
        print(self.mp3_name)
        

root = Tk()
app=Converter(root)
root.mainloop()
