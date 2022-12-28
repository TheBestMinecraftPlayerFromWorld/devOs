from re import S
from time import sleep
import tkinter as tk
from tkinter import font
import tkinterweb
import threading
import os
import hashlib
import base64
import math
from pathlib import Path
import datetime
moveWindow = None
uapap = []
userOs = ""
osPath = ""
def hash(text):
    H = hashlib.sha256(text).digest()
    H = base64.b64encode(H)
    return H.decode()

def getParent(path, levels = 1):
    common = path
 
    # Using for loop for getting
    # starting point required for
    # os.path.relpath()
    for i in range(levels + 1):
 
        # Starting point
        common = os.path.dirname(common)
 
    # Parent directory upto specified
    # level
    return os.path.relpath(path, common)

from sys import platform
import sys
if platform == "linux" or platform == "linux2":
    userOs = "linux" # linux
elif platform == "darwin":
    userOs = "MacOS" # OS X
elif platform == "win32":
    #Windows
    userOs = "windows"
    osPath = "C:/ddevOs"
    if os.path.exists(osPath):
        if os.path.isdir(osPath):
            with open(f"{osPath}/settings/users.txt","r") as f:
                Uapap = (f.read().split("\n"))
                for d in Uapap:
                    uapap.append(d.split(";"))
                print(uapap)
    else:
        os.mkdir(osPath)
        os.mkdir(f"{osPath}/users")
        os.mkdir(f"{osPath}/settings")
        with open(f"{osPath}/settings/users.txt","w") as f:#create userTable
            f.write("Admin;JAvlGPq9JyTdtvBO6x2llnRI1+gxwIyPqCKAn3THIKk=;admin")
        os.mkdir(f"{osPath}/users/Admin")
        os.mkdir(f"{osPath}/users/Admin/Desktop")

class user:
    name = "Admin"
    perm = "admin"
class Os:
    def __init__(self):
        self.appBar = ""
        self.path = f"{osPath}/users/{user.name}"
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
if userOs == "windows":
    def mm2(event):
        if moveWindow != None:
            #print(devOs.devOSw.winfo_pointerx())
            moveWindow.window.place(x=devOs.devOSw.winfo_pointerx()-devOs.devOSw.winfo_rootx()-80, y=devOs.devOSw.winfo_pointery()-devOs.devOSw.winfo_rooty())
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

                self.closeBtn = tk.Button(self.windowMoveBar,text="X",bg="red",command=self.quitWin)
                self.window.pack_propagate(0)
                #self.windowMoveBar.pack_propagate(0)
                self.windowMoveBar.pack(fill=tk.X,expand=True)#,side="top")
                self.windowMoveBar.place(x=0,width=width)
                self.AppName = tk.Label(self.windowMoveBar,text=name)
                self.name = name
                self.moveBtn.pack(side=tk.LEFT)
                self.AppName.place(x=(width/2))
                self.closeBtn.pack(side=tk.RIGHT)
                #self.content = tk.Frame(self.window,height=height-self.windowMoveBar.winfo_height())
                self.place = len(devOs.openedApps)
                devOs.openedApps.append(self)
                #print(devOs.openedApps)
            def quitWin(self):
                self.window.destroy()
            def move(self,x,y) -> None:
                self.window.place(x=x,y=y)
                #self.window.move()eeeeeeeeeeeeeeeeeeeeeeeeeee
    class taskConfiguration:
        name = "Task Configuration"
        def __init__(self) -> None:
            self.win = devOsAppAPI.window(200,500,self.name,"red")
            self.win.window.pack(expand=True)
            self.btns = []
            self.rl = tk.Button(self.win.window,text="Reload",command=self.loadApps,bg="blue")
            self.rl.place(y=30)
            self.loadApps()
        def loadApps(self):
            for s in self.btns:
                s.destroy()
            self.btns = []
            y = 60
            c = 0
            for s in devOs.openedApps:
                n = s.name
                self.btns.append(tk.Button(self.win.window,text=n,command=lambda j=s, p = c: self.closeApp(j,p)))
                self.btns[len(self.btns)-1].pack()
                self.btns[len(self.btns)-1].place(y=y)
                y += 30
                c+=1
            
        def closeApp(self,app,index):
            app.window.destroy()
            devOs.openedApps.pop(index)
            self.loadApps()
            
    class textPreview:
        name = "Text Preview"
        def __init__(self,path) -> None:
            self.win = devOsAppAPI.window(500,600,self.name,"red")
            self.win.window.pack(expand=True)
            self.text = []
            self.path = path
            self.displayText()
            self.saveBtn = tk.Button(self.win.window,text="Save",command=self.save)
            self.saveBtn.place(y=470)
        def displayText(self):
            with open(self.path,'r',encoding="utf-8") as f:
                t  = f.read()
                self.x = tk.Text(self.win.window, width=74, height=26)
                self.x.place(y=30)
                self.x.delete(1.0,"end")
                self.x.insert(1.0, t)
        def save(self):
            with open(self.path,'w',encoding="utf-8") as f:
                f.write(self.x.get("1.0",tk.END))
    class explorer:
        name = "Explorer"
        def __init__(self,path=f"{osPath}/users/{user.name}/Desktop") -> None:
            self.win = devOsAppAPI.window(400,500,self.name,"red")
            self.win.window.pack(expand=True)
            self.path = path
            self.btns = []
            self.bb = tk.Button(self.win.window,text="<-",command=lambda: self.goBack(),bg="blue")
            self.bb.pack()
            self.bb.place(y=30)
            self.loadFiles()
        def loadFiles(self,path = ""):
            if path == "":
                path = self.path
            items = os.listdir(path)
            print(path)
            self.btns = []
            y = 60
            for item in items:
                x = ""
                c = "white"
                if os.path.isfile(path+"/"+item):
                    x = (item)
                else:
                    x = (item+"/")
                    c = "yellow"
                
                self.btns.append(tk.Button(self.win.window,text=x,command=lambda j=x: self.open(self.path+"/"+j),bg=c))
                self.btns[len(self.btns)-1].pack()
                self.btns[len(self.btns)-1].place(y=y)
                y += 30
        def open(self,newPath):
            print(newPath)
            if os.path.isdir(newPath):
                self.path = newPath
                ct = 0
                for item in self.btns:
                    item.destroy()
                    ct+=1
                self.loadFiles()
            else:
                textPreview(newPath)
                pass #open file
        def goBack(self):
            self.open(os.path.dirname(self.path.rstrip("/")))
                
        
    class mathProblems:
        name = "Math Problems"
        def __init__(self) -> None:
            self.win = devOsAppAPI.window(200,200,self.name,"blue")
            self.win.window.pack(expand=True)

            self.inCmn8 = tk.Button(self.win.window,text="Find in nth. Common with its 8th power.",command=self.inCmn8)
            self.inCmn8.pack()
            self.inCmn8.place(y=20)
        def inCmn8(self):
            return
    class browser:
        name = "Browser"
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
            self.win = devOsAppAPI.window(480,854,self.name,"white")
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
    class menu:
        name = "Menu"
        def __init__(self):
            self.win = devOsAppAPI.window(200,200,self.name,"red")
            self.win.window.pack(expand=True)
            self.win.window.place(x=300,y=700)
            self.loBTN = tk.Button(self.win.window,text="Logout",command=self.logout)
            self.loBTN.pack()
            self.loBTN.place(y=30)
            self.sdBTN = tk.Button(self.win.window,text="Shutdown",command=self.shutdown)
            self.sdBTN.pack()
            self.sdBTN.place(y=60)
        def logout(self):
            for app in devOs.openedApps:
                app.window.destroy()
            if devOs.appBar != "":
                devOs.appBar.destroy()
            login()
        def shutdown(self):
            for app in devOs.openedApps:
                app.window.destroy()
            if devOs.appBar != "":
                devOs.appBar.destroy()
            devOs.devOSw.destroy()
    class Terminal:
        name = "Terminal"
        def listToString(self,s,b):
 
            # initialize an empty string
            str1 = ""
        
            # traverse in the string
            for ele in s:
                str1 += ele+b
        
            # return string
            return str1
        def reload(self):
            print(self.lastLines)
            lst = len(self.lastLines)
            self.txt = ""
            for t in range(22):
                self.txt+=self.lastLines[(lst-22)+t]+"\n"
            self.commands.config(text=self.txt)
        def clear(self):
            self.lastLines = []
            for _ in range(22):
                self.lastLines.append("")
        def __init__(self) -> None:
            self.win = devOsAppAPI.window(430,500,self.name,"red")
            self.win.window.pack(expand=True)
            self.txt = ""
            self.lastLines = []
            self.clear()
            self.path = f"{osPath}/users/{user.name}/Desktop"
            self.commands = tk.Label(self.win.window,text=self.txt,height=22,width=500,anchor='w')
            self.commands.place(y=30)
            self.reload()
            
            self.commandLine = tk.Entry(self.win.window,width=500)
            self.commandLine.place(y=370)
            
            self.execute = tk.Button(self.win.window,text="Execute",command=self.exec)
            self.execute.place(y=400)
        def cmdPro(self):
            cmd = self.commandLine.get()
            self.commandLine.delete(0,"end")
            if cmd.startswith("logout"):
                for app in devOs.openedApps:
                    app.window.destroy()
                if devOs.appBar != "":
                    devOs.appBar.destroy()
                login()
            if cmd.startswith("cd "):
                p = cmd.replace("cd ","")
                if os.path.exists(self.path+"/"+p):
                    self.path+="/"+p
                else:
                    self.lastLines.append("Could not find Path")
            if cmd.startswith("clear"):
                self.clear()
            if cmd.startswith("ls"):
                items = os.listdir(self.path)
                for item in items:
                    x = ""
                    if os.path.isfile(self.path+"/"+item):
                        x = (item)
                    else:
                        x = (item+"/")
                    self.lastLines.append(x)

                self.lastLines.append("-------")
            if cmd.startswith("chgpw"):
                p = (cmd.replace("chgpw ","")).split(" ")
                if user.perm == "admin":
                    newPw = hash(p[1].encode())
                    with open(f"{osPath}/settings/users.txt","w+") as f:
                        global uapap
                        uuapap = []
                        t = ""
                        for d in uapap:
                            c = d
                            if c[0] == p[0]:
                                newUAPAP = f"{c[0]};{newPw};{c[2]}"
                                t+=newUAPAP+"\n"
                                uuapap.append(newUAPAP.split(";"))
                            else:
                                t+=self.listToString(d,";")
                                uuapap.append(c)
                        uapap = uuapap
                        f.write(t)
                    self.lastLines.append(f"Succesfully changed password of user {p[0]}")
            if cmd.startswith("addusr"):
                p = (cmd.replace("addusr ","")).split(" ")
                if user.perm == "admin":
                    newPw = hash(p[1].encode())
                    with open(f"{osPath}/settings/users.txt","w+") as f:
                        t = ""
                        for s in uapap:
                            t+=s[0]+";"+s[1]+";"+s[2]+"\n"
                        x = p[0]+";"+(hash(p[1].encode()))+";"+p[2]
                        uapap.append(x.split(";"))
                        
                        t+=x
                        f.write(t)
                    os.mkdir(f"{osPath}/users/{p[0]}")
                    os.mkdir(f"{osPath}/users/{p[0]}/Desktop")
                    self.lastLines.append(f"Succesfully added User {p[0]}")
            self.reload()
                #os.
        def exec(self):
            self.cmdPro()

    class calculater:
        name = "Calculater"
        def __init__(self):
            self.win = devOsAppAPI.window(240,150,self.name,"red")
            self.win.window.pack(expand=True)
            self.win.window.place(x=300,y=700)
            self.rechnung = ""
            self.rechnungL = tk.Label(self.win.window,text=self.rechnung,height=1,anchor='w')
            self.rechnungL.place(y=30)
            self.ergebnis = tk.Label(self.win.window,text=0,height=1,anchor='w')
            self.ergebnis.place(y=60)
            x = "AC"
            b = tk.Button(self.win.window,text=str(x),command=lambda:self.clearRechnung())
            b.place(x=0,y=90)
            x = "+/-"
            b = tk.Button(self.win.window,text=str(x),command=lambda c = "-":self.addAtBeginning(c))
            b.place(x=30,y=90)
            ct = 1
            for x in range(3):
                for y in range(3):
                    b = tk.Button(self.win.window,text=str(ct),command=lambda c = ct:self.addToRechnung(c))
                    b.place(x=x*30,y=(y+4)*30)
                    ct+=1
            rechenzeichen = ["/","*","-","+"]
            ct = 0
            for y in rechenzeichen:
                b = tk.Button(self.win.window,text=y,command=lambda c = y:self.addToRechnung(c))
                b.place(x=120,y=(ct+3)*30)
                ct+=1
            x = "0"
            b = tk.Button(self.win.window,text=str(x),command=lambda c = x:self.addToRechnung(c))
            b.place(x=0,y=210)
            x = "."
            b = tk.Button(self.win.window,text=str(x),command=lambda c = x:self.addToRechnung(c))
            b.place(x=30,y=210)
            
        def addToRechnung(self,num):
            self.rechnung += str(num)
            self.rechnungL.config(text=self.rechnung)    
            self.ergebnis.config(text=str(eval(self.rechnung)))
        def addAtBeginning(self,num):
            self.rechnung = num + self.rechnung
            self.rechnungL.config(text=self.rechnung)    
            self.ergebnis.config(text=str(eval(self.rechnung)))
        def clearRechnung(self):
            self.rechnung = ""
            self.rechnungL.config(text=self.rechnung)    
            self.ergebnis.config(text=str(eval(self.rechnung)))
    apps = [menu,explorer,browser,taskConfiguration,Terminal,calculater]
    class appBar:
        loadedApps = []
        def returnClock(self):
            now = datetime.datetime.now()
            return f"{now.hour}:{now.minute}"
        def __init__(self) -> None:
            self.bar = tk.Frame(devOs.devOSw,height=50,width=1000,bg="red",)
            self.bar.pack_propagate(0)
            self.bar.pack(expand=True)
            self.bar.place(x=480,y=900)
            devOs.appBar = self.bar
            self.clock = tk.Label(self.bar,text="0:0",bg="red")
            self.loadAvalibleApps()
            self.clock.place(x=966,y=27)
            t1 = threading.Thread(target=self.loadClock)
            t1.start()
        def loadAvalibleApps(self):
            self.loadedApps = []
            co = 0
            for app in apps:
                self.loadedApps.append(tk.Button(self.bar,text=app.name,command=app))
                self.loadedApps[co].pack()
                self.loadedApps[co].place(x=(co+0.5)*(1000/len(apps)))
                co+=1
        def loadClock(self):
            tx = self.returnClock()
            self.clock.config(text=tx)
            sleep(1)
            self.loadClock()
            #return l
    class login:
        def __init__(self) -> None:
            self.l = tk.Frame(devOs.devOSw,height=100,width=200,bg="red",)
            self.l.pack_propagate(0)
            self.l.pack(expand=True)
            self.lU = tk.Entry(self.l)
            self.lU.place(y=5)
            self.lP = tk.Entry(self.l)
            self.lP.place(y=30)
            self.lB = tk.Button(self.l,text="Login",command=lambda:self.login(self.lU.get(),self.lP.get()))
            self.lB.place(y=60)
        def login(self,username,password):
            successful = False
            for Cuser in uapap:
                if Cuser[0] == username:
                    if hash(password.encode()) == Cuser[1]:
                        successful = True
                        user.name = Cuser[0]
                        user.perm = Cuser[2]
            if successful:
                appBar()
                self.l.destroy()
            else:
                self.lP.delete(0,"end")
                self.lP.insert(0, "")
    def start():
        login()
        #appBar()
        devOs.devOSw.mainloop() 
    if __name__ == "__main__":
        start()
