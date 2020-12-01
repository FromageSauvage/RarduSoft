import time
from tkinter import *
import webbrowser
import shutil, os
from tkinter.filedialog import askopenfilename
from zipfile import ZipFile
import getpass
import glob
import time

#Bonne chance a l'aventurier qui a ose fourrer ses pattes dans ce trou perdu
#Rip l'encodage

path8 = os.path.join('C:/','Users',getpass.getuser(),'Documents','Arduino','RarduboyBIN')
path9 = os.path.join('C:/','Users',getpass.getuser(),'Documents','arduino-1.8.13','arduino.exe')

def launchBtn1():
    Tk().withdraw() 
    filename = askopenfilename()
    (filepath9, filename9) = os.path.split(filename)
    (basen, extension1) = os.path.splitext(filename9)
    ftype = "*.ino"
    with ZipFile(filename,"r") as zip_ref:
        zip_ref.extractall(path8)

    time.sleep(1)
    path62 = os.path.join('C:/','Users',getpass.getuser(),'Documents','Arduino','RarduboyBIN','*')
    fname = str(glob.glob(path62, recursive=True))[1:-1]
    nfn = fname.strip("'")
    (filepath62, filename62) = os.path.split(nfn)
    path12 = os.path.join('C:/','Users',getpass.getuser(),'Documents','Arduino','RarduboyBIN',filename62,'**/',ftype)
    sortie = str(glob.glob(path12, recursive=True))[1:-1]
    nsor = sortie.strip("'")
    (filepath10, filename10) = os.path.split(nsor)
    (output, extension2) = os.path.splitext(filename10)
    path14 = os.path.join('C:/','Users',getpass.getuser(),'Documents','Arduino','RarduboyBIN',filepath62)
    path15 = os.path.join('C:/','Users',getpass.getuser(),'Documents','Arduino','Rarduboy',output)
    os.rename(path14,path15)
    popup()  
    
def launchBtn2():
    webbrowser.open_new("https://community.arduboy.com/c/games/35")

def launchBtn3():
    os.startfile(path9)

def launchBtn5():
    webbrowser.open_new("https://discord.gg/8X9rjVr")

def launchBtn7():
    webbrowser.open_new("https://rarduboy.wixsite.com/home")

def launchBtn8():
    webbrowser.open_new("https://github.com/FromageSauvage?tab=repositories")

def popup():
    fInfos = Toplevel()
    fInfos.title('popup')
    Button(fInfos, text='Telechargement fini', command=fInfos.destroy,font=("Bahnschrift SemiBold", 20, 'bold')).pack(expand=YES)
    
window = Tk()
window.iconbitmap("logosoft.ico")
window.title("RarduSoft")
window.geometry("400x500")
window.minsize(400, 500)
window.maxsize(400, 500)
window.config(background='#ebebeb')

frame1 = Frame(window, bg='#707070', bd=2)
frame2 = Frame(window, bg='#707070', bd=2)
titre = Label(frame1, text= "                                                                                  Rardusoft                                                                                   ", font=("Bahnschrift SemiBold", 20, 'bold'), bg='#707070', fg='#DADADA')
credits = Label(frame2, text="                                                                                                  FromageSauvage 2020                                                                                                 ", font=("Bahnschrift SemiBold", 10, 'bold'), bg='#707070', fg='#DADADA')
credits.pack()
titre.pack()
frame1.pack(side = TOP)
frame2.pack(side = BOTTOM)

btn2 = Button(window, text="Telecharger les jeux", font=("Bahnschrift SemiBold", 20, 'bold'), bg='#f56342', fg='#707070', command=launchBtn2, bd=0)
btn2.pack(expand=YES)
btn1 = Button(window, text="    Preparer un jeu    ", font=("Bahnschrift SemiBold", 20, 'bold'), bg='#eabfff', fg='#707070', command=launchBtn1, bd=0)
btn1.pack(expand=YES)
btn3 = Button(window, text="     Ouvrir Arduino     ", font=("Bahnschrift SemiBold", 20, 'bold'), bg='#9cff6e', fg='#707070', command=launchBtn3, bd=0)
btn3.pack(expand=YES)
btn5 = Button(window, text="           Discord           ", font=("Bahnschrift SemiBold", 20, 'bold'), bg='#8aadff', fg='#707070', command=launchBtn5, bd=0)
btn5.pack(expand=YES)
btn7 = Button(window, text="       Site internet       ", font=("Bahnschrift SemiBold", 20, 'bold'), bg='#ffab3d', fg='#707070', command=launchBtn7, bd=0)
btn7.pack(expand=YES)
btn8 = Button(window, text="            Github            ", font=("Bahnschrift SemiBold", 20, 'bold'), bg='#2b2b2b', fg='#707070', command=launchBtn8, bd=0)
btn8.pack(expand=YES)
window.mainloop()
