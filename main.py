from time import sleep
import tkinter as tk
from tkinter import font
import tkinterweb
import threading
moveWindow = None

class user:
    name = ""
    perm = ""

class Os:
    def __init__(self):
        self.path = "C:/ddevOs"
        self.devOSw = tk.Tk()
        self.openedApps = []
        self.devOSw.title("DevOS")
        self.devOSw.geometry("1920x1080")
        
        #track mouse movement and buttons
        self.devOSw.bind("<Motion>", Os.mouseMoved)        
        #self.devOSw.bind("<ButtonRelease-1>", Os.mouseButtonReleased)
        
        self.devOSw.configure(background="black")
        
    def mouseButtonReleased(event):
        print("Release")
        setMoveWindow(None)
    def mouseMoved(event):
        mm2(event)

def mm2(event):
    if moveWindow != None:
        #print(devOs.devOSw.winfo_pointerx())
        moveWindow.window.place(x=devOs.devOSw.winfo_pointerx()-devOs.devOSw.winfo_rootx()-70, y=devOs.devOSw.winfo_pointery()-devOs.devOSw.winfo_rooty())
        #print(moveWindow)



def setMoveWindow(value):
    global moveWindow
    moveWindow = value
from pynput.mouse import *

def on_click(x, y, button, pressed):
    #print(button,type(button),str(button))
    if button == Button.left and pressed == True:
        setMoveWindow(None)
def addListener():
    with Listener(on_click=on_click) as listener:
        listener.join()

t = threading.Thread(target=addListener)
t.start()


devOs = Os()
class devOsAppAPI:
    class window:
        def mmWE(self,event):
            #print(event)
            pass#mouseMoved(self)
        def __init__(self,height,width,name,bgcolor) -> None:
            self.window = tk.Frame(devOs.devOSw,height=height,width=width,bg=bgcolor)
            self.windowMoveBar = tk.Frame(self.window)#,height=200)
            self.moveBtn = tk.Button(self.windowMoveBar,text="Move",command=lambda:setMoveWindow(self))#,width=200)
            #self.moveBtn.bind('<Button-1>', self.mmWE)#
            #self.moveBtn.bind('<ButtonRelease-1>', lambda:setMoveWindow(None))

            self.closeBtn = tk.Button(self.windowMoveBar,text="X",bg="red",command=self.window.destroy)
            self.window.pack_propagate(0)
            #self.windowMoveBar.pack_propagate(0)
            self.windowMoveBar.pack(fill=tk.X,expand=True)#,side="top")
            self.windowMoveBar.place(x=0,width=width)
            self.AppName = tk.Label(self.windowMoveBar,text=name)
            self.moveBtn.pack(side=tk.LEFT)
            self.AppName.place(x=(width/2))
            self.closeBtn.pack(side=tk.RIGHT)
            #self.content = tk.Frame(self.window,height=height-self.windowMoveBar.winfo_height())
            devOs.openedApps.append(self)
            #print(devOs.openedApps)
        def move(self,x,y) -> None:
            self.window.place(x=x,y=y)
            #self.window.move()eeeeeeeeeeeeeeeeeeeeeeeeeee

class taskConfiguration:
    def loadApps(self):
        
        for s in devOs.openedApps:
            print(s.AppName["text"])
    def __init__(self) -> None:
        self.win = devOsAppAPI.window(200,500,"Task Configuration","red")
        self.win.window.pack(expand=True)
        self.loadApps()
        
class explorer:
    def __init__(self,part="C:/devOS/") -> None:
        self.win = devOsAppAPI.window(200,200,"Explorer","red")
        self.win.window.pack(expand=True)
class browser:
    def lw(self):
        url = self.webbar.get()
        if url == "":
            self.website.load_website("https://google.com")
            self.webbar.delete(0,"end")
            self.webbar.insert(0, "https://google.com")
        #elif not url.startswith("http://") and not url.startswith("https://"):
        #    self.website.load_website("https://"+url)
        else:
            self.website.load_website(url)
    def __init__(self,web="https://google.com") -> None:
        self.win = devOsAppAPI.window(480,854,"Browser","white")
        self.win.window.pack(expand=True)
        
        self.webbarF = tk.Frame(self.win.window)
        self.webbar = tk.Entry(self.webbarF,width=120)
        self.webbarSearchBtn = tk.Button(self.webbarF,text="Search",command=self.lw)

        self.webbar.pack(fill=tk.BOTH)
        self.webbarSearchBtn.pack()
        self.webbarF.pack()
        self.webbarF.place(y=20)#,x=360)

        self.website = tkinterweb.HtmlFrame(self.win.window)
        self.lw()
        self.website.pack(fill="both")
        self.website.place(y=60,x=0)
        #print()

class appBar:
    def __init__(self) -> None:
        self.bar = tk.Frame(devOs.devOSw,height=50,width=1000,bg="red",)
        self.bar.pack_propagate(0)
        self.bar.pack(expand=True)
        self.bar.place(x=480,y=900)
        self.loadAvalibleApps()
    def loadAvalibleApps(self):
        self.menu = tk.Button(self.bar,text="Menu")
        self.menu.pack()
        self.menu.place(x=0)
        self.explorer = tk.Button(self.bar,text="Explorer",command=explorer)
        self.explorer.pack()
        self.explorer.place(x=150)
        self.taskConfiguration = tk.Button(self.bar,text="Task Configuration",command=taskConfiguration)
        self.taskConfiguration.pack()
        self.taskConfiguration.place(x=300)
        self.browser = tk.Button(self.bar,text="Browser",command=browser)
        self.browser.pack()
        self.browser.place(x=450)
        #return l
class login:
    def __init__(self) -> None:
        pass

if __name__ == "__main__":
    #explorer()
    #taskConfiguration()
    appBar()
    devOs.devOSw.mainloop()
