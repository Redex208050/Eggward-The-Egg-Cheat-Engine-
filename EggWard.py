import subprocess, os, time
from tkinter import *
from PIL import ImageTk, Image


def switchToHack(hackDll):
    os.rename('c:/Program Files (x86)/Steam/steamapps/common/EGG/Egg_Data/Managed/Assembly-CSharp.dll', 'c:/Program Files (x86)/Steam/steamapps/common/EGG/Egg_Data/Managed/No_hack.dll')
    os.rename("c:/Program Files (x86)/Steam/steamapps/common/EGG/Egg_Data/Managed/" + hackDll, 'c:/Program Files (x86)/Steam/steamapps/common/EGG/Egg_Data/Managed/Assembly-CSharp.dll')


def switchToOriginal(hackDll):
    os.rename("c:/Program Files (x86)/Steam/steamapps/common/EGG/Egg_Data/Managed/Assembly-CSharp.dll", "c:/Program Files (x86)/Steam/steamapps/common/EGG/Egg_Data/Managed/" + hackDll)
    os.rename("c:/Program Files (x86)/Steam/steamapps/common/EGG/Egg_Data/Managed/No_hack.dll", 'c:/Program Files (x86)/Steam/steamapps/common/EGG/Egg_Data/Managed/Assembly-CSharp.dll')


def launchHack(hack):
    global status, skinStr, backgroundStr
    skinStr = 'Default'
    backgroundStr = 'Default'
    status.set('Skin: ' + skinStr + "\nBackground: " + backgroundStr)
    try:
        if hack == 'Instant_Win_hack.dll':
            subprocess.run("c:\Program Files (x86)\Steam\Steam.exe steam://rungameid/2784840")
            time.sleep(10)
        else:
            subprocess.run("c:/Program Files (x86)/Steam/steamapps/common/EGG/Egg.exe")
        switchToOriginal(hack)
    except:
        switchToOriginal(hack)
        return 0 #add new window with error


def switchLaunchHack(hack='Instant_Win_hack.dll'):
    switchToHack(hack)
    launchHack(hack)


def pSkin():
    new_window.destroy()
    global skin, status, skinStr, backgroundStr
    skin = 0
    skinStr = 'St Patricks'
    status.set('Skin: ' + skinStr + "\nBackground: " + backgroundStr)


def vSkin():
    new_window.destroy()
    global skin, status, skinStr, backgroundStr
    skin = 1
    skinStr = 'Valentines'
    status.set('Skin: ' + skinStr + "\nBackground: " + backgroundStr)


def pBackground():
    new_window.destroy()
    global background, status, skinStr, backgroundStr
    background = 0
    backgroundStr = 'St Patricks'
    status.set('Skin: ' + skinStr + "\nBackground: " + backgroundStr)


def vBackground():
    new_window.destroy()
    global background, status, skinStr, backgroundStr
    background = 1
    backgroundStr = 'Valentines'
    status.set('Skin: ' + skinStr + "\nBackground: " + backgroundStr)


def skinSelectionMenu():
    global new_window, root
    new_window = Toplevel()
    new_window.title("Skins")
    new_window.geometry(f"250x100+{root.winfo_x()+40}+{root.winfo_y()+110}")
    new_window.configure(background='black')
    new_window.iconbitmap("Resources/eggy.ico")
    new_window.resizable(False,False)

    Button(new_window, text="St. Patrick's Day", command=pSkin, width=15, height=3, bg="#ff7f27").place(x = 10, y = 20)
    Button(new_window, text="Valentine's Day", command=vSkin, width=15, height=3, bg="#ff7f27").place(x = 130, y = 20)


def backgroundSelectionMenu():
    global new_window, root
    new_window = Toplevel()
    new_window.title("Backgrounds")
    new_window.geometry(f"250x100+{root.winfo_x()+40}+{root.winfo_y()+180}")
    new_window.configure(background='black')
    new_window.iconbitmap("Resources/eggy.ico")
    new_window.resizable(False,False)

    Button(new_window, text="St. Patrick's Day", command=pBackground, width=15, height=3, bg="#ff7f27").place(x = 10, y = 20)
    Button(new_window, text="Valentine's Day", command=vBackground, width=15, height=3, bg="#ff7f27").place(x = 130, y = 20)


def checkCustomizationAndRun():
    global skin, background
    combo = (skin, background)
    skin = None
    background = None
    match combo:
        case (None, None):
            subprocess.run("c:/Program Files (x86)/Steam/steamapps/common/EGG/Egg.exe")
        case (0, None):
            switchLaunchHack('St_Patties_skin_hack.dll')
        case (1, None):
            switchLaunchHack('Valentines_skin_hack.dll')
        case (None, 0):
            switchLaunchHack('St_Patties_background_hack.dll')
        case (None, 1):
            switchLaunchHack('Valentines_background_hack.dll')
        case (0, 0):
            switchLaunchHack('St_Patties_hack.dll')
        case (1, 0):
            switchLaunchHack('St_Patties_skin_Valentines_background_hack.dll')
        case (1, 1):
            switchLaunchHack('Valentines_hack.dll')
        case (0, 1):
            switchLaunchHack('Valentines_skin_St_Patties_background_hack.dll')


def mainMenu():
    global root
    root = Tk()
    root.geometry("500x300")
    root.title("EggWard (Egg Cheatpack)")
    root.iconbitmap("Resources/eggy.ico")
    root.configure(background='black')
    root.resizable(False,False)

    global status, skinStr, backgroundStr
    status = StringVar()
    skinStr = 'Default'
    backgroundStr = 'Default'
    status.set('Skin: ' + skinStr + '\nBackground: ' + backgroundStr)
    Label(root, textvariable=status, fg="white", bg="black", justify="left").place(x=350, y=25)

    #Cheat button #1
    Button(root, text="Instant Win", command=switchLaunchHack, width=40, height=3, bg="#ff7f27").place(x=20, y=40)
    #Cheat button #2
    Button(root, text="Skins", command=skinSelectionMenu, width=40, height=3, bg="#ff7f27").place(x=20, y=120)
    #Cheat button #3
    Button(root, text="Backgrounds", command=backgroundSelectionMenu, width=40, height=3, bg="#ff7f27").place(x=20, y=200)
    #Launch button
    Button(root, text="Launch", command=checkCustomizationAndRun, width=15, height=2, bg="#ff7f27").place(x=350, y=250)
    #OrangeMan
    art = ImageTk.PhotoImage(Image.open("Resources/img1.png"))
    Label(root, image = art, bg="black").place(x=340, y=80)

    root.mainloop()


def main ():
    global skin, background
    skin = None
    background = None
    mainMenu()
    return 0

if __name__ == "__main__":
    main()