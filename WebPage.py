from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import os
import datetime
from subprocess import call
from selenium import webdriver
from time import sleep

if not os.path.exists('data'):
    os.makedirs('data')

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('data/login.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
db.commit()
db.close()

#main Class
class main:
    def __init__(self,master):
    	# Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    #LOG
    def LOG(self):
        currentDT = datetime.datetime.now()
        newpath = r'temp' 
        if not os.path.exists(newpath):
          os.makedirs(newpath)
        if os.path.exists(newpath):
          f=open("temp/LOG.py", "a+")
          f.write("user = {} is login at {}\n".format(self.username.get(),str(currentDT)))


    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('data/login.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        #result
        if result:
            #Cpanel
            def Cpanel():
                driver = webdriver.Chrome()
                driver.get("http://127.0.0.1:3333/")
                sleep(2)
            #start
            def start():
                rc = call("./functions/start.sh", shell=True)
            #stop
            def stop():
                rc = call("./functions/stop.sh", shell=True)
            #clear
            def clear():
                rc = call("./functions/clear.sh", shell=True)
            self.LOG()
            self.logf.pack_forget()
            self.head['text'] = self.username.get() + '\n Loged In'
            self.head['pady'] = 150
            self.head['padx'] = 150
            self.opt = Frame(self.master,padx =10,pady = 10)
            Button(self.opt,text = ' Start ',bd = 3 ,font = ('',15),padx=5,pady=5,command=start, height = 1, width = 5).grid(row=2,column=0)
            Button(self.opt,text = ' Stop ',bd = 3 ,font = ('',15),padx=5,pady=5,command=stop, height = 1, width = 5).grid(row=2,column=1)
            Button(self.opt,text = ' Cpanel ',bd = 3 ,font = ('',15),padx=5,pady=5,command=Cpanel, height = 1, width = 5).grid(row=3,column=0)
            Button(self.opt,text = ' Clear ',bd = 3 ,font = ('',15),padx=5,pady=5,command=clear, height = 1, width = 5).grid(row=4,column=1)
            Button(self.opt,text = ' Exit ',bd = 3 ,font = ('',15),padx=5,pady=5,command=root.destroy, height = 1, width = 5).grid(row=4,column=2)
            self.opt.pack()
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('data/login.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = 'X').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = 'X').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)

    

#create window and application object
root = Tk()
root.title("WebPage")
main(root)
root.mainloop()


