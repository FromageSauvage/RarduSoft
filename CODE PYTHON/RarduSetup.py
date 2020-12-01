from tkinter import *
import shutil, os
import getpass
import time
import sys
from zipfile import ZipFile

usern = getpass.getuser()
ex = 0
de = 0

path1 = os.path.join('C:/','Users',getpass.getuser(),'Documents','exe','RarduSoft.lnk')
path11 = os.path.join(os.path.dirname(sys.argv[0]),'exe.zip')
path2 = os.path.join(os.path.dirname(sys.argv[0]),'Arduino15.zip')                       
path3 = os.path.join(os.path.dirname(sys.argv[0]),'arduino-1.8.13')
path7 = os.path.join(os.path.dirname(sys.argv[0]),'README.txt')
path10 = os.path.join('C:/','Users',getpass.getuser(),'Documents','Arduino')
path4 = os.path.join('C:/','Users',getpass.getuser(),'Desktop')
path5 = os.path.join('C:/','Users',getpass.getuser(),'AppData','Local')
path6 = os.path.join('C:/','Users',getpass.getuser(),'Documents')
      
def launchBtn2():
    exit()
    window.destroy()

def launchBtn1():
    time.sleep(0.1)
    btn1.destroy()
    btn2.destroy()
    btn4.destroy()
    label.destroy()
    label3 = Label(window, text="Telechargement en cours ...\nNe fermez pas la fenetre\n   ",font=("Bahnschrift SemiBold", 15, 'bold'), bg='#e8e8e8')
    label3.pack()
    window.update()
    time.sleep(1)
    with ZipFile(path11,"r") as zip_ref:
        zip_ref.extractall(path6)
    l1 = Label(window, text="Etape 1/5 DONE",font=("Bahnschrift SemiBold", 15, 'bold'), bg='#e8e8e8')
    l1.pack()
    window.update()
    time.sleep(1)
    with ZipFile(path2,"r") as zip_ref:
        zip_ref.extractall(path5)
    l2 = Label(window, text="Etape 2/5 DONE",font=("Bahnschrift SemiBold", 15, 'bold'), bg='#e8e8e8')
    l2.pack()
    window.update()
    time.sleep(1)
    shutil.move(path3,path6)
    l3 = Label(window, text="Etape 3/5 DONE",font=("Bahnschrift SemiBold", 15, 'bold'), bg='#e8e8e8')
    l3.pack()
    window.update()
    time.sleep(1)
    if not os.path.exists(path10):
          os.makedirs(path10)
    l4 = Label(window, text="Etape 4/5 DONE",font=("Bahnschrift SemiBold", 15, 'bold'), bg='#e8e8e8')
    l4.pack()
    window.update()
    time.sleep(1)
    shutil.move(path1,path4)
    l5 = Label(window, text="Etape 5/5 DONE",font=("Bahnschrift SemiBold", 15, 'bold'), bg='#e8e8e8')
    l5.pack()
    window.update()
    time.sleep(1)
    label3.destroy()
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()
    l5.destroy()
    label2 = Label(window, text="Telechargement termine .\n Nous vous remercions d'avoir telecharge\n RarduSoft",font=("Bahnschrift SemiBold", 15, 'bold'), bg='#e8e8e8')
    label2.pack()
    btn8 = Button(window, text="       Quitter        ", font=("Bahnschrift SemiBold", 20, 'bold'), bg='#fff347', fg='#333333', command=launchBtn2, bd=0)
    btn8.pack(expand=YES)
    window.mainloop()
    
window = Tk()
window.iconbitmap("logosetup.ico")
window.title("Setup")
window.geometry("500x400")
window.minsize(500, 400)
window.maxsize(500, 400)
window.config(background='#e8e8e8')

frame1 = Frame(window, bg='#707070', bd=2)
frame2 = Frame(window, bg='#707070', bd=2)
titre = Label(frame1, text= "                                                                                  Installeur                                                                                   ", font=("Bahnschrift SemiBold", 20, 'bold'), bg='#e8e8e8', fg='#333333')
credits = Label(frame2, text="                                                                                                  FromageSauvage 2020                                                                                                 ", font=("Bahnschrift SemiBold", 10, 'bold'), bg='#e8e8e8', fg='#333333')
credits.pack()
titre.pack()
frame1.pack(side = TOP)
frame2.pack(side = BOTTOM)

def launchBtn256():
    os.startfile(path7)
    
label = Label(window, text="Ce programme est OpenSource, vous etes libres de le modifer, \n les fichiers .py sont disponibles dans le dossier CODE PYTHON \n ouvrez le fichier texte README pour plus d'informations.",font=("Bahnschrift SemiBold", 12, 'bold'), bg='#e8e8e8')
label.pack(side = TOP)
btn4 = Button(window, text="Ouvrir README", font=("Bahnschrift SemiBold", 20, 'bold'), bg='#34ebe5', fg='#333333', command=launchBtn256, bd=0)
btn4.pack(expand=YES)
btn1 = Button(window, text="       Installer       ", font=("Bahnschrift SemiBold", 20, 'bold'), bg='#04d63c', fg='#333333', command=launchBtn1, bd=0)
btn1.pack(expand=YES)
btn2 = Button(window, text="        Quitter        ", font=("Bahnschrift SemiBold", 20, 'bold'), bg='#d62e04', fg='#333333', command=launchBtn2, bd=0)
btn2.pack(expand=YES)
    
window.mainloop()
