import tkinter as tk
from tkinter import ttk
import cv2
import os
import Script
from datetime import date


def homeWin(root):

        root1 = tk.Frame(root, bg= '#111c14')
        root1.grid()
        #define the label
        tk.Label(root1, text='FACE RECOGNITION ATTENDANCE SYSTEM', font=("Arial", 16), bg='#111c14', fg='white').grid(column=0, row=0, sticky='W', padx=15, pady=10)
        #define font

        #3599c4
        #9dd4d1

        #write in each frame
        tk.Message(root1, width=130, text='Click the button below to add a new students profile',justify='center', font=("Arial", 14), bg='#111c14', fg='white').grid(column=0, row=1, sticky='W', padx=50, pady=40)
        #write in each frame
        tk.Message(root1, width=135, text='Click the button below to start a new class', justify='center', font=("Arial", 14), bg='#111c14', fg='white').grid(column=0, row=1, sticky='W', padx=300, pady=40)

        #button for creating profile
        createProfile = tk.Button(root1, text='Create Student Profile', width=20, command= lambda: [changepage()], bg='green', fg='white')
        createProfile.grid(column=0, row=2, sticky='NW', padx=50, pady=0)

        #button for start sesstion
        startSess = tk.Button(root1, text='Start Session', width=20, command= lambda: [changepage2()], bg='green', fg='white')
        startSess.grid(column=0, row=2, sticky='NW', padx=300, pady=0)

        #define the label
        tk.Label(root1, text='DEPARTMENT OF COMPUTER SCIENCE, FPN', font=("Arial", 11), bg='#111c14', fg='white').grid(column=0, row=3, sticky='W', padx=85, pady=70)

        


#window to create student profile
def profileWin(root):
        
        root2 = tk.Frame(root, bg= '#111c14')#3599c4
        root2.grid()

        #back button
        bacj = tk.Button(root2, text='Back', command= lambda: [back()], bg='red', fg='white')
        bacj.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        tk.Label(root2, text='Create Profile', font=("Arial", 30), bg='#111c14', fg='#3599c4').grid(column=0, row=1, sticky=tk.W, padx=100, pady=0)
        

        #entry for reg No
        tk.Label(root2, text='Registration Number:', font=("Arial", 15), bg='#111c14', fg='white').grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)
        regNo = tk.StringVar(value='Digits only')
        regNumber = ttk.Entry(root2, font=("Arial, 15"), textvariable=regNo)
        regNumber.grid(column=0, row=2, sticky=tk.W, padx=210, pady=10)

        regNo1 = regNo.get()

        
        tk.Label(root2, text='How do you want to add your picture?', font=("Arial", 15), bg='#111c14', fg='#3599c4').grid(column=0, row=4, sticky=tk.W, padx=70, pady=0)

        #button for copying path
        copyPath = tk.Button(root2, text='Paste Path', command= lambda: [pastePath()], bg='red', fg='white')
        copyPath.grid(column=0, row=5, sticky=tk.W, padx=100, pady=30)

        #button for taking Snapshot
        snap = tk.Button(root2, text='Snapshot', command= lambda: [snapShot()], bg='red', fg='white')
        snap.grid(column=0, row=5, sticky=tk.W, padx=350, pady=30)

        #focus the mouse on name 
        regNumber.focus()

        def pastePath():
                f1 = tk.Frame(root2, bg= '#111c14')
                f1.grid(column=0, row=4, sticky='W')
                #to get the picture path
                tk.Label(f1, text='Picture Path:', font=("Arial", 15), bg='#111c14', fg='white').grid(column=0, row=0, sticky=tk.W, padx=10, pady=40)
                picPa = tk.StringVar()
                picturePath = ttk.Entry(f1, font=("Arial, 15"), textvariable=picPa)
                picturePath.grid(column=0, row=0, sticky=tk.W, padx=210, pady=40)
                
                

                def save():
                        regNo1 = regNo.get()
                        picPath = picPa.get()
                        img = cv2.imread(picPath)
                        #cv2.imshow("", img)
                        cur_direc = os.getcwd()

                        path = os.path.join(cur_direc, 'data/faces/')
                        #print(path)
                        #its taking it as a path
                        cv2.imwrite(os.path.join(path, regNo1+'.jpg'), img)
                
                #button done
                done = tk.Button(f1, text='Done', command= lambda: [save(), changepage()], bg='red', fg='white')
                done.grid(column=0, row=1, sticky=tk.W, padx=230, pady=50)
                

        def snapShot():
                regNo1 = regNo.get()
                cam = cv2.VideoCapture(0)
                img = cam.read()[1]
                cv2.imshow("image", img)
                #cv2.imshow("", img)
                cur_direc = os.getcwd()

                path = os.path.join(cur_direc, 'data/faces/')
                #print(path)
                #its taking it as a path
                cv2.imwrite(os.path.join(path, regNo1+'.jpg'), img)
                
                #button for done
                done = tk.Button(root2, text='Done', command= lambda: [changepage()], bg='red', fg='white')
                done.grid(column=0, row=6, sticky=tk.W, padx=230, pady=50)
                
                

 


def success(root):
        root3 = tk.Frame(root, bg= '#111c14')
        root3.grid()

        tk.Label(root3, text='Profile Created Successfully', font=("Arial", 30), bg='#111c14', fg='#3599c4').grid(column=0, row=0, sticky='NSWE', pady=100)

        #def exit():
                #root.destroy()
        
        close = tk.Button(root3, text='Back', font=("Arial", 10), bg='red', fg='white', command=lambda: [changepage()])
        close.grid(column=0, row=1, sticky=tk.W, padx=230, pady=50)



def details(root):
        def sess():
                things = []
                courseCode = courCo.get()
                courseTitle = courTi.get()
                
                things.append(courseCode)
                things.append(courseTitle)
                things.append(str(datee))
                
                Script.main()
                Script.ccsv(things)
        
       
        root4 = tk.Frame(root, bg= '#111c14')
        root4.grid()

        #back button
        bacj = tk.Button(root4, text='Back', command= lambda: [back()], bg='red', fg='white')
        bacj.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        tk.Label(root4, text='Computer Science', font=("Arial", 30), bg='#111c14', fg='#3599c4').grid(column=0, row=1, sticky=tk.W, padx=50, pady=0)

        #entry for course code
        tk.Label(root4, text='Course Title:', font=("Arial", 15), bg='#111c14', fg='white').grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

        courTi = tk.StringVar()
        courTite = ttk.Entry(root4, font=("Arial, 15"), textvariable=courTi)
        courTite.grid(column=0, row=2, sticky=tk.W, padx=210, pady=10)

        #entry for course title
        tk.Label(root4, text='Course Code:', font=("Arial", 15), bg='#111c14', fg='white').grid(column=0, row=3, sticky=tk.W, padx=10, pady=10)

        courCo = tk.StringVar()
        courCod = ttk.Entry(root4, font=("Arial, 15"), textvariable=courCo)
        courCod.grid(column=0, row=3, sticky=tk.W, padx=210, pady=10)

        datee = date.today()

        tk.Label(root4, text='Date: ' + str(datee), font=("Arial", 15), bg='#111c14', fg='white').grid(column=0, row=4, sticky=tk.W, padx=10, pady=10)

        
        
        start = tk.Button(root4, text='Start', font=("Arial", 10), bg='red', fg='white', command=lambda: [sess(), changepage2()])
        start.grid(column=0, row=5, sticky=tk.W, padx=230, pady=50)


def back():
        global pagenum, root
        for widget in root.winfo_children():
                widget.destroy()

        
        pagenum = 1
        homeWin(root)


def changepage():
        global pagenum, root
        for widget in root.winfo_children():
                widget.destroy()
        if pagenum == 1:
                pagenum = 2
                profileWin(root)
                

        elif pagenum == 2:
                pagenum = 3
                success(root)
                
                
        elif pagenum == 3:
                pagenum = 1
                homeWin(root)
                
                

def changepage2():
        global pagenum, root
        for widget in root.winfo_children():
                widget.destroy()
        if pagenum == 1:
                pagenum = 2
                details(root)
                
        else:
                pagenum = 1
                homeWin(root)
                
#creating a window
pagenum = 1
root = tk.Tk()
root['bg'] = '#111c14'
root.title("Face Recognition")
root.geometry("500x350")
root.resizable(False, False)
homeWin(root)


#call the function
root.mainloop()


