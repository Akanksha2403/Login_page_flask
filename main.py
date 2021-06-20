from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


class login_system:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        #all images
        self.bg_icon = ImageTk.PhotoImage(file="Black_Template.jpg")
        self.pass_icon = PhotoImage(file="password2.png")
        self.logo_icon = ImageTk.PhotoImage(file="l.jpg")
        self.man_icon = ImageTk.PhotoImage(file="mman.jpg")
        self.uname = StringVar()
        self.pass_ = StringVar()
        bg_lbl = Label(self.root, image=self.bg_icon).pack()

        title = Label(self.root, text=" Login System", font=("times new roman", 25,"bold"),  bg= "yellow", fg="red", bd=10, relief = GROOVE)
        title.place(x=0, y=0, relwidth=1)

        Login_Frame = Frame(self.root, bg="white")
        Login_Frame.place(x=400,y=150)
        logolbl = Label(Login_Frame,image=self.logo_icon).grid(row=0,columnspan=2,pady=0)
        logouser = Label(Login_Frame, text="Username", image=self.man_icon,compound=LEFT,font=("times new roman", 15, "bold"), bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtuser = Entry(Login_Frame, bd=5, relief=GROOVE, textvariable=self.uname, font=("", 15)).grid(row=1, column=1, padx=20)
        logouser = Label(Login_Frame, text="Password", image=self.pass_icon, compound=LEFT,font=("times new roman", 15, "bold"), bg="white").grid(row=2, column=0, padx=20, pady=10)
        txtpass = Entry(Login_Frame, bd=5, relief=GROOVE,textvariable=self.pass_, font=("", 15)).grid(row=2, column=1, padx=20)

        btn_log=Button(Login_Frame,text="Login",width=15,command=self.login,font=("times new roman", 15, "bold"), bg="yellow", fg="red").grid(row=3, columnspan=2, pady=10)

    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.uname.get() == "Akanksha" or self.pass_.get() == "12345":
            messagebox.showinfo("Successfull", "Welcome")
        else:
            messagebox.showerror("Error","Invalid any one")


root = Tk()
obj = login_system(root)
root.mainloop()
